#!/usr/bin/env python3
"""Gera o RPX PT-BR a partir do RPX EUR original e dos MSBTs revisados.

Não distribui o RPX do jogo: o usuário fornece sua própria cópia original.
"""

from __future__ import annotations

import argparse
import hashlib
import struct
import zlib
from pathlib import Path


EXPECTED_ORIGINAL_SHA256 = "19eb66c3141143901282f1ca1ceac97a7f941702ff9671dcd5b270c93a452fac"
DATA_SECTION = 5
TABLE_IN_DATA = 0x24F980 - 0x194240
SECTION_HEADER_SIZE = 40


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def section(blob: bytes, index: int) -> tuple[int, tuple[int, ...]]:
    table = struct.unpack_from(">I", blob, 32)[0]
    count = struct.unpack_from(">H", blob, 48)[0]
    if index >= count:
        raise ValueError("RPX não possui a seção .data esperada.")
    header = table + index * SECTION_HEADER_SIZE
    return header, struct.unpack_from(">10I", blob, header)


def parse_lfmo(data: bytes) -> list[str]:
    files = struct.unpack_from(">I", data, 8)[0]
    info = struct.unpack_from(">I", data, 16)[0]
    names, cursor = [], info
    for _ in range(files):
        offset = struct.unpack_from(">I", data, cursor + 8)[0]
        cursor += 12
        end = data.index(b"\0", offset)
        names.append(data[offset:end].decode("ascii", "replace"))
    return names


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("original_rpx", type=Path)
    parser.add_argument("output_rpx", type=Path)
    parser.add_argument("--msbt-dir", type=Path, required=True)
    parser.add_argument("--lfmo", type=Path, required=True)
    args = parser.parse_args()

    if args.output_rpx.exists():
        raise SystemExit(f"Saída já existe: {args.output_rpx}")
    if sha256(args.original_rpx) != EXPECTED_ORIGINAL_SHA256:
        raise SystemExit("RPX não corresponde ao executável EUR original aceito; nada foi gerado.")

    blob = bytearray(args.original_rpx.read_bytes())
    header_offset, data_header = section(blob, DATA_SECTION)
    data_offset, packed_size = data_header[4], data_header[5]
    packed = bytes(blob[data_offset : data_offset + packed_size])
    raw_size = struct.unpack(">I", packed[:4])[0]
    raw = bytearray(zlib.decompress(packed[4:]))
    if len(raw) != raw_size:
        raise SystemExit("Falha ao descomprimir a seção .data do RPX.")

    names = parse_lfmo(args.lfmo.read_bytes())
    usen = [name.rsplit("/", 1)[-1] for name in names if name.upper().startswith("/TEXT/USEN/") and name.upper().endswith(".MSBT")]
    if len(usen) != 120:
        raise SystemExit(f"LFMO inesperado: esperava 120 MSBTs USEN, recebeu {len(usen)}.")
    for index, filename in enumerate(usen):
        patch = args.msbt_dir / filename
        if not patch.is_file():
            raise SystemExit(f"MSBT ausente: {patch}")
        struct.pack_into(">I", raw, TABLE_IN_DATA + index * 8, patch.stat().st_size)

    replacement = struct.pack(">I", len(raw)) + zlib.compress(raw, level=6)
    next_offsets = []
    count = struct.unpack_from(">H", blob, 48)[0]
    for index in range(count):
        _, candidate = section(blob, index)
        if candidate[4] > data_offset:
            next_offsets.append(candidate[4])
    limit = min(next_offsets) - data_offset
    if len(replacement) > limit:
        raise SystemExit("A seção .data recompilada não cabe antes da próxima seção.")

    blob[data_offset : data_offset + len(replacement)] = replacement
    struct.pack_into(">I", blob, header_offset + 20, len(replacement))
    args.output_rpx.write_bytes(blob)
    print(f"RPX gerado: {args.output_rpx} ({len(blob):,} bytes; 120 tamanhos atualizados)")


if __name__ == "__main__":
    main()
