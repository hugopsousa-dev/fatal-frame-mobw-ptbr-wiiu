# Fatal Frame: Maiden of Black Water — PT-BR (Wii U)

Tradução não oficial para Português do Brasil de *Fatal Frame: Maiden of Black Water* / *Project Zero: Maiden of Black Water* para Nintendo Wii U.

> **Status:** tradução aplicada e validada em Wii U real (Aroma + SDCafiine). A revisão atual restaura diacríticos PT-BR e mantém uma cópia de segurança do RPX original antes da instalação.

| | |
|---|---|
| Plataforma | Nintendo Wii U (Aroma + SDCafiine) |
| Região-base | EUR |
| Title ID | `00050000101D3F00` |
| Idioma | Inglês → Português do Brasil |
| Modpack | `PTBR` |

## O que este projeto faz

O jogo guarda os textos em arquivos **MSBT** dentro de `archive00.lnk`, um arquivo LNS5 comprimido. A tradução substitui os MSBTs em um archive redirecionado pelo SDCafiine.

O executável `lens5_cafe.rpx` também possui uma tabela de tamanhos dos MSBTs. Como a revisão PT-BR altera o tamanho de parte dos textos, essa tabela é atualizada no RPX e o arquivo precisa ser instalado diretamente no armazenamento do jogo com FTPiiU Everywhere.

## Instalação — visão geral

1. Use um Wii U com **Aroma**, **SDCafiine** e **FTPiiU Everywhere**.
2. Coloque o archive PT-BR em:
   `sd:/wiiu/sdcafiine/00050000101d3f00/PTBR/content/archive00.lnk`
3. Ative o modpack `PTBR` pelo SDCafiine.
4. Faça backup do `code/lens5_cafe.rpx` instalado no Wii U.
5. Envie o RPX compatível com o archive pelo FTPiiU Everywhere, valide o hash e reinicie o console normalmente.

O SDCafiine redireciona `content/` e `aoc/`; ele **não** substitui o RPX que fica em `code/`. Por esse motivo, copiar um RPX para o cartão SD não é suficiente.

Leia o procedimento completo em [docs/INSTALACAO.md](docs/INSTALACAO.md) e a explicação do formato em [docs/TECNICO.md](docs/TECNICO.md).

## Automação e validação

Os scripts em `tools/` foram feitos para reduzir etapas manuais e impedir erros comuns:

- `validate_layout.py` valida a estrutura LNS5 e o cabeçalho ELF do RPX antes do deploy.
- `rebuild_rpx_data_section.py` recompõe somente a seção `.data` do RPX depois de atualizar a tabela de tamanhos MSBT.

Eles não incluem texto do jogo, dumps, chaves ou arquivos originais.

## Legal

Este repositório não distribui ROMs, dumps, executáveis originais, `archive00.lnk`, fontes do jogo ou qualquer outro ativo protegido. Ele documenta o processo e fornece ferramentas para aplicar a tradução a partir de uma cópia legítima do jogo.

*Fatal Frame*, *Project Zero* e *Maiden of Black Water* são marcas de seus respectivos detentores. Este projeto de fã não possui afiliação ou endosso oficial.

## Créditos

Tradução, engenharia reversa e testes em Wii U real: Hugo (Huguera).

Canal / novos projetos: <https://www.youtube.com/channel/UCJcKIDhtlBCZ_6YjnmoWXCQ>
