#!/usr/bin/env python3
"""Reempacota somente a seção .data comprimida de um RPX Wii U.

O patch de tamanhos de MSBT fica nessa seção. O programa preserva todo o
restante do RPX e só aceita um resultado que caiba no espaço originalmente
reservado, para evitar deslocar seções ou gerar um executável inconsistente.
"""

from __future__ import annotations

import argparse
import struct
import zlib
from pathlib import Path


SECTION_DATA = 5
ELF_HEADER_SECTION_OFFSET = 32
ELF_HEADER_SECTION_COUNT = 48
SECTION_HEADER_SIZE = 40
SECTION_FILE_OFFSET_FIELD = 16
SECTION_SIZE_FIELD = 20


def section_header(blob: bytes, index: int) -> tuple[int, tuple[int, ...]]:
    section_table = struct.unpack_from(">I", blob, ELF_HEADER_SECTION_OFFSET)[0]
    count = struct.unpack_from(">H", blob, ELF_HEADER_SECTION_COUNT)[0]
    if index >= count:
        raise ValueError(f"RPX tem apenas {count} seções; esperava a seção {index}.")
    offset = section_table + index * SECTION_HEADER_SIZE
    return offset, struct.unpack_from(">10I", blob, offset)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("original_rpx", type=Path)
    parser.add_argument("patched_drpx", type=Path)
    parser.add_argument("output_rpx", type=Path)
    args = parser.parse_args()

    original = bytearray(args.original_rpx.read_bytes())
    drpx = args.patched_drpx.read_bytes()

    original_header_offset, original_section = section_header(original, SECTION_DATA)
    _, drpx_section = section_header(drpx, SECTION_DATA)
    original_offset, original_size = original_section[4], original_section[5]
    drpx_offset, drpx_size = drpx_section[4], drpx_section[5]

    packed = bytes(original[original_offset : original_offset + original_size])
    if len(packed) < 6:
        raise ValueError("Seção .data do RPX está curta demais.")
    expected_size = struct.unpack(">I", packed[:4])[0]
    unpacked = zlib.decompress(packed[4:])
    if len(unpacked) != expected_size or len(unpacked) != drpx_size:
        raise ValueError("Tamanho da .data descomprimida não confere com o DRPX.")

    replacement = drpx[drpx_offset : drpx_offset + drpx_size]
    encoded = struct.pack(">I", len(replacement)) + zlib.compress(replacement, level=6)

    next_offsets = []
    for index in range(struct.unpack_from(">H", original, ELF_HEADER_SECTION_COUNT)[0]):
        _, header = section_header(original, index)
        candidate = header[4]
        if candidate > original_offset:
            next_offsets.append(candidate)
    available = min(next_offsets) - original_offset if next_offsets else len(original) - original_offset
    if len(encoded) > available:
        raise ValueError(
            f".data recompilada ({len(encoded)}) não cabe no espaço seguro ({available})."
        )

    original[original_offset : original_offset + len(encoded)] = encoded
    struct.pack_into(">I", original, original_header_offset + SECTION_SIZE_FIELD, len(encoded))
    args.output_rpx.write_bytes(original)

    print(f".data: {original_size} -> {len(encoded)} bytes (limite seguro {available})")
    print(f"RPX salvo: {args.output_rpx}")


if __name__ == "__main__":
    main()
