#!/usr/bin/env python3
"""
LNS5 patcher (zlib) — injeta TODOS os .msbt traduzidos COMPRIMIDOS em zlib.

Formato confirmado (fatal_frame.bms + deteccao):
  ficheiro ZIP!=0 = sequencia de chunks ate montar SIZE bytes:
    cada chunk = [u32 BE cabecalho][dados] ; alinhado a 0x10
    cabecalho & 0x8000 -> COMPRIMIDO (baixos 15 bits = tam comprimido), zlib
    senao -> RAW (copia tam bytes)
  bloco descomprimido = 0x4000 (16 KB); compressao = zlib padrao (78 9c)

Estrategia: comprime cada bloco de 16 KB em zlib, anexa no fim e repointa a
entrada (relocacao, como no DXHR). So mexe nos .msbt; o resto fica intacto.
Faz AUTOTESTE (descomprime de volta e compara) antes de terminar.

Uso: python3 lns5_patch_zlib.py /Volumes/GUITARRA/archive00.lnk
"""
import argparse
import struct, zlib
from pathlib import Path

BLOCK = 0x4000     # 16 KB por bloco (confirmado)
ALIGN10 = 0x10

def parse_lfmo(data):
    files = struct.unpack('>I', data[8:12])[0]
    info  = struct.unpack('>I', data[16:20])[0]
    out, pos = [], info
    for _ in range(files):
        no = struct.unpack('>I', data[pos+8:pos+12])[0]; pos += 12
        end = data.index(b'\x00', no)
        out.append(data[no:end].decode('ascii', 'replace'))
    return out

def build_zlib_chunks(data):
    out = bytearray()
    for i in range(0, len(data), BLOCK):
        block = data[i:i+BLOCK]
        comp = zlib.compress(block, 6)          # 78 9c ...
        if len(comp) > 0x7FFF:                   # nao deve acontecer com 16 KB
            raise RuntimeError("bloco comprimido > 0x7FFF")
        out += struct.pack('>I', 0x8000 | len(comp))
        out += comp
        while len(out) % ALIGN10:
            out.append(0)
    return bytes(out)

def read_file_like_game(f, off, size):
    """Mimica o leitor do .bms: le chunks ate montar 'size' bytes."""
    f.seek(off)
    out = bytearray()
    while len(out) < size:
        hdr = struct.unpack('>I', f.read(4))[0]
        clen = hdr & 0x7FFF
        blob = f.read(clen)
        out += zlib.decompress(blob) if (hdr & 0x8000) else blob
        pos = f.tell()
        f.seek(pos + ((-pos) % ALIGN10))
    return bytes(out)

def main(archive_path, msbt_dir, lfmo_path):
    names = parse_lfmo(lfmo_path.read_bytes())
    index = {n: i for i, n in enumerate(names)}
    msbt_files = sorted(p for p in msbt_dir.iterdir()
                        if p.suffix.lower() == '.msbt')
    print(f"[msbt dir] {msbt_dir} | [lfmo] {len(names)} nomes | [msbt] {len(msbt_files)} ficheiros\n")

    injected = []   # (idx, name, off, size, src_bytes)
    with open(archive_path, 'r+b') as f:
        hdr = f.read(32)
        assert hdr[:4] == b'LNS5', "base nao e LNS5"
        size0 = struct.unpack('>Q', hdr[16:24])[0]
        align = struct.unpack('>Q', hdr[24:32])[0]
        print(f"[base] size={size0:,} align=0x{align:x}")

        f.seek(0, 2)
        if f.tell() > size0:
            f.seek(size0); f.truncate()
        cur = size0
        f.seek(cur)
        cur += (-cur) % align
        f.seek(cur)

        done = skip = 0
        for p in msbt_files:
            internal = '/TEXT/USEN/' + p.name
            idx = index.get(internal)
            if idx is None:
                skip += 1; continue
            src = p.read_bytes()
            chunks = build_zlib_chunks(src)
            f.seek(cur); f.write(chunks)
            end = f.tell(); end += (-end) % align
            f.seek(32 + idx*32)
            f.write(struct.pack('>QQQQ', cur, len(src), len(chunks), 1))
            injected.append((idx, p.name, cur, len(src), src))
            cur = end; f.seek(cur); done += 1

        f.seek(16); f.write(struct.pack('>Q', cur))

    print(f"✅ {done} .msbt comprimidos+injetados ({skip} ignorados)")
    print(f"   tamanho final: {cur:,}\n")

    # AUTOTESTE: descomprime de volta os primeiros 5 e compara byte-a-byte
    print("=== AUTOTESTE (descompressao) ===")
    ok = True
    with open(archive_path, 'rb') as f:
        for idx, name, off, size, src in injected[:5]:
            got = read_file_like_game(f, off, size)
            good = (got == src)
            ok = ok and good
            print(f"  {name:22s} {'✅ OK' if good else '❌ FALHOU'} ({len(got)}/{size})")
    print("\n" + ("✅ AUTOTESTE PASSOU — pode ir pro deploy." if ok
                  else "❌ AUTOTESTE FALHOU — nao faca deploy, me avisa."))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Injeta MSBTs PT-BR em um archive LNS5.")
    parser.add_argument("archive", type=Path, help="cópia de trabalho de archive00.lnk")
    parser.add_argument("--msbt-dir", type=Path, required=True)
    parser.add_argument("--lfmo", type=Path, required=True)
    args = parser.parse_args()
    main(args.archive, args.msbt_dir, args.lfmo)
