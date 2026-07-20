# Patch baixável

O arquivo de Release contém um **patch construtor**, não arquivos do jogo. É necessário Python 3 e espaço livre para uma cópia adicional de aproximadamente 3,7 GB.

## Arquivos de entrada

Da sua cópia EUR legítima, informe:

- `archive00.lnk` do `content/`;
- `lens5_cafe.rpx` original do `code/`.

O script só aceita o SHA-256 conhecido do RPX EUR original. Isso evita aplicar a tabela de tamanhos em uma versão ou região errada.

## Gerar os arquivos PT-BR

No terminal, dentro da pasta extraída da Release:

```bash
python3 tools/build_patch.py \
  "/caminho/para/archive00.lnk" \
  "/caminho/para/lens5_cafe.rpx" \
  "./saida-ptbr"
```

O resultado será:

```text
saida-ptbr/archive00.lnk
saida-ptbr/lens5_cafe.rpx
```

Valide os dois com:

```bash
python3 tools/validate_layout.py ./saida-ptbr/archive00.lnk ./saida-ptbr/lens5_cafe.rpx
```

Depois siga [INSTALACAO.md](INSTALACAO.md). O `archive00.lnk` vai para o SD via SDCafiine; o RPX vai para o armazenamento do Wii U por FTPiiU Everywhere.
