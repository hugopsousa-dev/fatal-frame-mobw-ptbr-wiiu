# Notas técnicas

## LNS5 e MSBT

`archive00.lnk` usa o contêiner LNS5. A ordem interna de arquivos é definida por `lfm_order.bin`; substituir um MSBT sem respeitar essa ordem ou a tabela do archive causa carregamento incorreto.

O fluxo de trabalho é:

1. Extrair os MSBTs `TEXT/USEN`.
2. Editar os textos em UTF-16 big-endian preservando os controles `{{...}}`.
3. Reconstruir os MSBTs, injetá-los no LNS5 e descomprimir amostras para autoteste.
4. Atualizar no RPX a tabela de tamanhos de 120 MSBTs, iniciada no offset `0x24F980` do RPX descomprimido.

## Por que o RPX muda

Cada entrada da tabela ocupa oito bytes: um `uint32` big-endian de tamanho e quatro bytes zero. Se um texto traduzido cresce ou diminui, o jogo precisa receber o novo tamanho; caso contrário, pode ocorrer tela preta ou texto corrompido.

No RPX comprimido, a tabela está na seção `.data`. A ferramenta `rebuild_rpx_data_section.py` descomprime somente essa seção, aplica um DRPX previamente validado, comprime com zlib nível 6 e recusa resultados que não caibam no espaço seguro antes da próxima seção.

## Acentuação e fontes

As fontes de diálogo `GALANT` e `VIVIENE` possuem cobertura completa dos caracteres PT-BR comuns. A fonte de sistema tem cobertura mais limitada para algumas maiúsculas; por isso toda revisão visual deve testar menus e mensagens além dos diálogos.

## Limites de distribuição

Arquivos LNS5, RPX, MSBT compilados e BFFNT contêm dados do jogo e não são publicados neste repositório. A publicação se limita a documentação e ferramentas reproduzíveis.
