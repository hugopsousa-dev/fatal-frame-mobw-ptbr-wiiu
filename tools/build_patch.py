#!/usr/bin/env python3
"""Gera os dois arquivos PT-BR sem distribuir ativos originais do jogo."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"
PATCH_DATA = ROOT / "patch_data"


def run(*args: str) -> None:
    subprocess.run([sys.executable, *args], check=True)


parser = argparse.ArgumentParser()
parser.add_argument("archive_original", type=Path)
parser.add_argument("rpx_original", type=Path)
parser.add_argument("output_dir", type=Path)
args = parser.parse_args()

if not args.archive_original.is_file() or not args.rpx_original.is_file():
    raise SystemExit("Informe o archive00.lnk e o lens5_cafe.rpx originais existentes.")
if args.output_dir.exists():
    raise SystemExit(f"A saída já existe: {args.output_dir}")

args.output_dir.mkdir(parents=True)
archive_out = args.output_dir / "archive00.lnk"
rpx_out = args.output_dir / "lens5_cafe.rpx"
shutil.copyfile(args.archive_original, archive_out)

run(
    str(TOOLS / "lns5_patch_zlib.py"), str(archive_out),
    "--msbt-dir", str(PATCH_DATA / "reaccent_msbt"),
    "--lfmo", str(PATCH_DATA / "lfm_order.bin"),
)
run(
    str(TOOLS / "patch_rpx_msbt_sizes.py"), str(args.rpx_original), str(rpx_out),
    "--msbt-dir", str(PATCH_DATA / "reaccent_msbt"),
    "--lfmo", str(PATCH_DATA / "lfm_order.bin"),
)
print(f"Patch pronto em: {args.output_dir}")
