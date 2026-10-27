# Fatal Frame: Maiden of Black Water / Project Zero — tradução PT-BR para Wii U

**v1.2: gere os arquivos pelo navegador, sem executar scripts baixados.**

- [ABRIR ASSISTENTE NO NAVEGADOR](https://hugopsousa-dev.github.io/assistente/?jogo=fatal-frame)
- [Como instalar, passo a passo](COMO_INSTALAR.md)
- [Baixar os deltas e guias](https://github.com/hugopsousa-dev/fatal-frame-mobw-ptbr-wiiu/releases/latest/download/FatalFrame-MOBW_PTBR_WiiU_Patch.zip)

Região **EUR** · Title ID `00050000101D3F00`. Requer os arquivos da sua própria cópia do jogo. O site baixa somente dados de patch, processa os originais localmente e salva uma pasta nova com sua permissão. O fluxo usa Chrome/Edge com File System Access API.

Os atalhos .command/.cmd da v1.1 foram retirados do ZIP v1.2. Não é necessário instalar Python, desativar o Gatekeeper ou remover quarentena.

**Fatal Frame exige também instalar o RPX compatível no Wii U por FTP.** O conteúdo vai ao SD; siga o guia para fazer backup e instalar o executável.

## Fontes e validação

O [motor web](https://github.com/hugopsousa-dev/hugopsousa-dev.github.io/tree/main/assistente) usa os mesmos deltas BPS da v1.1, com verificações SHA-256/CRC. Os arquivos em `instalador/` são os dados e guias do pacote público. O aplicador Python para manutenção está em `tools/instalar_avancado.py`; ele é uma opção técnica fora do ZIP principal.

[Testes e limitações](VALIDACAO.md). A documentação técnica anterior está em `docs/`. Tradução, engenharia reversa e testes históricos: Hugo (Huguera). Projeto de fã, sem afiliação oficial.
