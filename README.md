# Log Dumper
Log Dumper é um key logger simples que joga todas as informações do alvo online.

## Features
- **Keyboard log**: O script coleta todas a teclas apertadas no teclado, mesmo com a janela do programa fora de foco.
- **Screenshot**: O script captura a tela do alvo a cada vez que um clique acontece. A imagem é salva em formato JPEG em Base64 em uma pasta chamada `imgs` dentro da URL principal
- **Dump Online**: O script coloca todas as informações disponíveis online, no Dontpad através de uma URL customizável. Isso facilita a coleta dos dados após a infecção.

O script separa os dumps por nome da máquina. Dessa forma  possível guardar vários dumps ao mesmo tempo de máquinas diferentes. Além disso, o script apenas concatena novas informaçes caso algo já esteja escrito na página em questão. Isso impede que informações velhas sejam perdidas por novas execuções do programa.

## Instalação
O script requer algumas dependências. Se não as tiver, execute os seguintes comandos:
```bash
$ sudo apt install python3-xlib
$ pip3 install mss
```
## Execução
Após a instalação, basta executar o arquivo `key.py`
```bash
$ python3 key.py
```
O script atualmente funciona apenas em linux com X.

### Término
Para terminar a execução do script corretamente, basta escrever `stop listening` em qualquer lugar (mesmo que não esteja com o foco em um programa que aceita input textual).

## Exemplo
Para testar o programa, rodei o key logger na URL [dontpad.com/:](http://dontpad.com/:). Os resultados dos testes ainda estão lá para ver a formatação entre outras coisas.

## Disclaimer
Esse script foi feito como parte da matéria de Segurança da UFRJ 2017.1 e não deve ser usado para fins maliciosos.

