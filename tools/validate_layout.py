#!/usr/bin/env python3
"""Valida cabeçalhos LNS5 e RPX sem modificar arquivos."""

from __future__ import annotations

import argparse
import struct
from pathlib import Path


def validate_archive(path: Path) -> None:
    with path.open("rb") as stream:
        header = stream.read(32)
    if len(header) != 32 or header[:4] != b"LNS5":
        raise SystemExit(f"ERRO: {path} não é um archive LNS5.")
    entries = struct.unpack(">Q", header[8:16])[0]
    declared = struct.unpack(">Q", header[16:24])[0]
    alignment = struct.unpack(">Q", header[24:32])[0]
    padding = declared - path.stat().st_size
    if padding < 0 or padding >= 0x800:
        raise SystemExit("ERRO: tamanho físico incompatível com o cabeçalho LNS5.")
    print(f"OK LNS5: {entries} entradas; alinhamento 0x{alignment:x}; padding virtual {padding} bytes")


def validate_rpx(path: Path) -> None:
    with path.open("rb") as stream:
        magic = stream.read(4)
    if magic != b"\x7fELF":
        raise SystemExit(f"ERRO: {path} não tem cabeçalho ELF/RPX.")
    print(f"OK RPX: {path.stat().st_size:,} bytes")


parser = argparse.ArgumentParser()
parser.add_argument("archive", type=Path)
parser.add_argument("rpx", type=Path)
args = parser.parse_args()
validate_archive(args.archive)
validate_rpx(args.rpx)
