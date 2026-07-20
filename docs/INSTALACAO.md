# Instalação segura

## Antes de começar

- Use a versão EUR, Title ID `00050000101D3F00`.
- Faça backup do cartão SD e mantenha uma cópia do RPX original fora do console.
- Desligue o Wii U pelo menu normal; não interrompa a alimentação durante uma gravação.

## Archive pelo SDCafiine

1. Copie o archive PT-BR para:
   `wiiu/sdcafiine/00050000101d3f00/PTBR/content/archive00.lnk`
2. Ejete o cartão corretamente e insira-o no Wii U.
3. Inicie pelo Aroma e aplique o modpack `PTBR` no SDCafiine.

## RPX pelo FTPiiU Everywhere

O RPX não é lido do SD pelo SDCafiine. No Wii U, abra **FTPiiU Everywhere** e conecte-se ao IP/porta exibidos.

O caminho EUR normalmente é:

```
/storage_usb/usr/title/00050000/101d3f00/code/lens5_cafe.rpx
```

Procedimento recomendado:

1. Baixe o RPX atual como backup.
2. Envie o novo arquivo com um nome temporário.
3. Baixe o temporário e compare o SHA-256 com o arquivo local.
4. Renomeie o RPX atual para um nome de backup.
5. Renomeie o temporário para `lens5_cafe.rpx`.
6. Saia do FTPiiU Everywhere e reinicie o Wii U normalmente.
7. Depois do reboot, baixe o RPX novamente e confirme o SHA-256 antes de abrir o jogo.

## Se algo der errado

Restaure o archive anterior no SD e o RPX salvo no backup. Não misture um archive revisado com um RPX cuja tabela de tamanhos foi gerada para outra revisão.
