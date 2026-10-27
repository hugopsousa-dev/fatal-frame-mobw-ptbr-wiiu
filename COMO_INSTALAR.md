# Fatal Frame: Maiden of Black Water / Project Zero — instalação PT-BR v1.2

Região: **EUR**. Title ID: `00050000101D3F00`. Guia revisado em 27/10/2026.

## 1. Abra o assistente no navegador

1. No computador, abra o **Google Chrome ou Microsoft Edge atualizado**. Use o [assistente Huguera](https://hugopsousa-dev.github.io/assistente/?jogo=fatal-frame). A página informará se o navegador não tem os recursos necessários. Safari e Firefox não oferecem a mesma seleção de pasta para este fluxo.
2. Você também pode baixar e extrair o ZIP. Dentro dele, abra `ABRIR_ASSISTENTE.html` e clique no link para o assistente. O ZIP contém os deltas e os guias; não contém executáveis para instalar no computador.
3. O processamento acontece no navegador. Seus arquivos do jogo ficam no computador: o site baixa apenas os dados do patch e não envia os originais para um servidor.

**Não é necessário Python, Terminal ou abrir arquivos .command/.cmd.** A geração usa as permissões de arquivos e pastas do navegador.

## 2. Separe os arquivos da sua cópia do jogo

Um dump é a cópia dos arquivos do seu próprio jogo. Se ainda não a tem, consulte o [Dumpling oficial](https://github.com/emiyl/dumpling). Este assistente usa arquivos extraídos em pastas; não aceita WUP/ISO/WUX diretamente.

Na região indicada acima, selecione os dois arquivos originais, nesta ordem:

- `content/archive00.lnk`
- `code/lens5_cafe.rpx`

Use os originais, sem tradução anterior. Confira as subpastas quando houver nomes iguais. Os hashes identificam a revisão compatível; trocar nomes ou o número da pasta não converte outra região. Reserve pelo menos **4 GB livres**, além do espaço do dump. Compatibilidade com outras atualizações ou DLC não é anunciada.

## 3. Escolha uma pasta para salvar e gere

1. Crie uma pasta vazia chamada **HUGUERA** no computador, por exemplo dentro de Downloads.
2. Na página, clique em **Selecionar pasta HUGUERA…** e escolha somente essa pasta.
3. O navegador solicitará permissão para gravar nessa pasta. Autorize apenas a pasta de saída escolhida; não selecione a pasta dos seus originais, o disco inteiro ou diretamente o SD.
4. Clique em **GERAR TRADUÇÃO**. Aguarde a conferência e a gravação. Fatal Frame tem um arquivo de aproximadamente 3,7 GB e pode levar vários minutos. Mantenha a aba aberta e espaço livre suficiente.
5. Ao terminar, aparecerá uma nova pasta com nome começando por **SAIDA_FatalFrame_PTBR_…**. O nome também será mostrado na página. Ela contém `wiiu`, `COMO_INSTALAR.html`, `RELATORIO.json` e `PRONTO_PARA_INSTALAR.txt`.
6. Só instale após a mensagem de conclusão e a presença de `PRONTO_PARA_INSTALAR.txt`. Uma pasta com `NAO_INSTALAR_EM_GERACAO.txt` ainda não está pronta.

Se cancelar ou ocorrer uma falha, o assistente tenta remover somente a pasta parcial criada por ele. Os originais não são substituídos. Se fechar a aba durante a geração, pode restar uma pasta incompleta: não a instale. Se um arquivo for recusado, confira região e revisão antes de tentar novamente.

## 4. Sobre o aviso do Mac e preparar o Wii U

O atalho `.command` da v1.1 não era assinado e autenticado pela Apple. Isso explica o aviso de que a Apple não podia verificá-lo; o aviso não é um diagnóstico de vírus. A orientação da Apple está em [Abrir apps com segurança no Mac](https://support.apple.com/pt-br/102445).

**Os atalhos foram retirados da v1.2. Use o navegador; não é necessário desativar o Gatekeeper, remover quarentena ou abrir exceções de segurança para um script.**

Antes de instalar no console, faça backup do SD e tenha Aroma com o plugin SDCafiine instalado e ativado. Ele não acompanha necessariamente toda instalação de Aroma. Veja o [SDCafiine oficial](https://github.com/wiiu-env/sdcafiine_plugin).

## 5. Copiar a tradução para o cartão

1. Com o Wii U desligado, conecte o SD ao computador.
2. Abra a nova pasta `SAIDA_…`. Dentro dela estará a pasta `wiiu`.
3. “Raiz do SD” é a primeira tela que aparece ao abrir o cartão, antes de entrar em qualquer pasta.
4. A meta é acrescentar o mod em `SD:/wiiu/sdcafiine/`. Não deixe `SD:/SAIDA_…/wiiu/` nem `SD:/wiiu/wiiu/`.
5. Se `wiiu` e `sdcafiine` já existirem, **entre nelas e copie apenas a pasta do jogo/mod indicada abaixo**. Se o sistema oferecer juntar/mesclar pastas, pode usar essa opção. Se oferecer substituir a pasta `wiiu` inteira, cancele e copie a subpasta manualmente. Preserve os outros jogos e plugins.
6. Se o mesmo mod já estiver instalado, guarde sua pasta anterior no computador e coloque a nova pasta do mod no lugar. Não misture arquivos de revisões diferentes.
7. Ejete o SD pelo sistema antes de retirar. Recoloque no Wii U.


Confira o caminho final deste jogo:

- `SD:/wiiu/sdcafiine/00050000101D3F00/PTBR/content/archive00.lnk`


## 6. Fatal Frame: instalar também o executável no Wii U

**Esta etapa é necessária neste jogo.** O SDCafiine redireciona `content` e `aoc`; ele não carrega o executável `code/lens5_cafe.rpx` do SD. Por isso, copiar apenas a pasta `wiiu` não conclui a instalação do Fatal Frame.

O assistente separa os destinos:

- `SAIDA_…/wiiu/…/content/archive00.lnk`: vai para o SD.
- `SAIDA_…/INSTALAR_NO_WII_U/code/lens5_cafe.rpx`: vai para a instalação do jogo, por FTP.

O executável original aceito tem SHA-256:

```
19eb66c3141143901282f1ca1ceac97a7f941702ff9671dcd5b270c93a452fac
```

### Conectar ao jogo instalado

1. Mantenha o jogo fechado. Deixe o Wii U e o computador na mesma rede local.
2. No Aroma, use o [FTPiiU oficial](https://github.com/wiiu-env/ftpiiu_plugin). Abra o menu de plugins com **L + baixo + menos**, entre em FTPiiU e anote o IP e a porta mostrados. Para acessar a instalação do jogo, habilite temporariamente **Allow access to system files**. Ao terminar, desabilite essa opção novamente.
3. Abra seu cliente FTP no computador, escolha conexão **FTP** e informe o IP e a porta do Wii U. No plugin oficial, as credenciais podem ficar vazias. Não exponha esse serviço à internet.
4. Localize a instalação EUR do jogo. Em armazenamento USB, o final do caminho costuma ser `storage_usb/usr/title/00050000/101d3f00/code/`; na memória interna, `storage_mlc/usr/title/00050000/101d3f00/code/`. O plugin pode mostrar um prefixo como `/fs/vol/` antes de `storage_usb` ou `storage_mlc`.
5. **Não adivinhe a unidade e não altere todas as pastas.** Escolha a instalação que você realmente usa. Se houver atualização em `usr/title/0005000e/101d3f00/code/` com outro RPX, ela pode ser a camada ativa. Só prossiga se o RPX dessa camada for aceito pelo assistente; se não for, peça suporte com a versão. Não tente contornar a verificação.

### Guardar o original e enviar a cópia traduzida

1. Baixe o `lens5_cafe.rpx` dessa instalação para o computador e guarde como backup fora de a nova pasta `SAIDA_…`. Esse deve ser o mesmo original aceito pelo assistente. Se ainda não gerou a tradução com ele, volte à etapa 3 e gere novamente com esse arquivo.
2. Na mesma pasta `code` do jogo, envie o novo RPX com nome temporário `lens5_cafe.rpx.ptbr-novo`. Não substitua o original ainda.
3. Baixe esse temporário de volta ao computador. Compare seu SHA-256 com o SHA-256 da saída RPX em `RELATORIO.json`. No Mac: `shasum -a 256` seguido do caminho do arquivo. No Windows PowerShell: `Get-FileHash -Algorithm SHA256` seguido do caminho. **Se os hashes não forem iguais, não ative o arquivo.**
4. Após a conferência, renomeie o RPX original do console para `lens5_cafe.rpx.original-backup`. Preserve também a cópia no computador. Se já existir esse backup, guarde-o antes e não o sobrescreva.
5. Renomeie `lens5_cafe.rpx.ptbr-novo` para `lens5_cafe.rpx`.
6. Desative o acesso a arquivos de sistema do FTPiiU. Reinicie o Wii U normalmente. Mantenha a alimentação durante as gravações.
7. Abra Fatal Frame EUR com o console em inglês. Se houver seleção de mods, escolha **PTBR**. Confira menus, legendas e acentos. O archive e o RPX devem ser os dois produzidos na mesma geração.

### Como voltar ao estado anterior

Com o jogo fechado, restaure pelo FTP o `lens5_cafe.rpx` original salvo no computador e retire do SD somente a pasta `wiiu/sdcafiine/00050000101D3F00/PTBR`. Se você já usava outra revisão da tradução, restaure **o par** anterior de archive e RPX. Não apague as pastas de outros jogos.


## 7. Conferir e pedir ajuda

O arquivo `RELATORIO.json` na saída lista os hashes e os arquivos produzidos. “Arquivos gerados” confirma a reconstrução no computador; a conferência visual no seu console ainda precisa ser feita.

Se continuar em inglês: confirme a região/Title ID, o idioma inglês do console, o plugin ativado e o caminho sem `wiiu` duplicado. Se houver apenas um mod, o SDCafiine pode aplicá-lo sem mostrar menu. As configurações do plugin são acessíveis com **L + direcional para baixo + botão menos** no GamePad.

Se aparecer “arquivo incompatível”, não force o patch: envie a mensagem de erro, região, versão base/atualização e nome do arquivo em **Issues** do repositório. Não envie o jogo, chaves, licenças ou saves. Este pacote aceita apenas a revisão identificada em `manifesto.json`; não declara compatibilidade com toda atualização ou DLC.

## Créditos e referências

Tradução, pesquisa e testes anteriores em console: Hugo (Huguera). Esta revisão padroniza o instalador e a distribuição; não é uma nova tradução integral nem uma nova validação de toda a campanha. Limitações de tradução anteriores permanecem.

Código novo do assistente: licença MIT, em `LICENCA_ASSISTENTE.txt`. Deltas não concedem direitos sobre o jogo original. Não venda a tradução nem distribua os arquivos gerados junto com o jogo.

- [Canal Huguera](https://www.youtube.com/channel/UCJcKIDhtlBCZ_6YjnmoWXCQ)
- [Estrutura oficial de mods do SDCafiine](https://github.com/wiiu-env/sdcafiine_plugin#installation-of-the-mods)
- [FTPiiU para Aroma](https://github.com/wiiu-env/ftpiiu_plugin#usage-information-and-settings)
