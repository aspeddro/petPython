# Introdução

## Instalando Python

### Windows

1) Baixe uma versão menor que 3.7. Versões maiores que 3.6.9 possui novas palavras chaves. Isso está quebrando/impossibilitando o uso de alguns pacotes. [Download Python 3.6.8](https://www.python.org/downloads/release/python-368/).
2) Baixe o arquivo `.exe`, *executable installer*.
3) [Tutorial para Instalação no Windows](https://python.org.br/instalacao-windows/)
4) Marque a opção `Add Python to PATH` durante a instalação.
5) Ao finalizar a instalação, procure por `cmd` ou `Prompt  de Comando` no menur iniciar. Ao abrir digite `python --version` e pressione __Enter__.
6) Se aparecer uma mensagem monstrando a versão do python, então tudo ocorreu bem.

## Executando Online

[Python Online Compiler, IDE, Editor, Interpreter and REPL](https://repl.it/languages/python3)

## IDLE

IDLE é um Ambiente de Desenvolvimento e Aprendizagem Integrado, ele facilita a criação, modificação e execução de scripts. Há diversas IDLE para trabalhar, Python instala uma por padrão, __Python Shell__. É possível executar python no Terminal no modo interativo.

Para entrar no modo interativo acesse __Prompt Comando__ no Windows ou o __Terminal__ no Linux e siga os passos abaixo:

1) Digite `python` e pressione __Enter__
   
```bash
C:\Users\UserName>python
```

2) Agora você está no modo interativo.

```bash
Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

1) Você pode realiazer algumas operações básicas, como somar dois números.

```bash
Python 3.6.9 (default, Apr 18 2020, 01:56:04) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 2+2
4
>>>
```

4) Para sair do modo interativo use o comando `exit()`.