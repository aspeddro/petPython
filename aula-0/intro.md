# Introdução

## Por que Python?

Python é uma linguagem de programação madura e de propósito geral, possui excelentes propriedades para programadores, o que a torna ideal para pessoas que nunca programaram. Algumas das mais notáveis ​​propriedades são: fácil leitura de código, digitação dinâmica e uso de memória. Python é uma linguagem interpretada, o código é executado imediatamente no console do Python sem precisar da etapa de compilação da linguagem de máquina. É uma linguagem de alto nível, isso significa que ela tem um nível de abstração elevado, seu código é facil de ler e ser entendido, ao contrário de linguagens de baixo nível que está relativamente próximo ao código da máquina.

Outras Vantagens:

* Gratuito
* Open Source
* Comunidate Grande e Ativa
* Diversas Bibliotecas

## Instalando Python

### Windows

1) Baixe a versão 3.8.0, [Download Python 3.8.0](https://www.python.org/downloads/release/python-380/).
   * Obs: Algumas versões do Python podem ser incompatíveis com certos pacotes, a versão 3.7.5 apresentou problemas para executar o Jupyter Lab. Já a versão 3.8.0 executou normalmente, assim como na versão 3.6.9.
2) Selecione a opção *Windows x86-64 executable installer* na seção *Files*.
3) [Tutorial para Instalação no Windows](https://python.org.br/instalacao-windows/)
4) Marque a opção **Add Python to PATH** durante a instalação.
5) Ao finalizar a instalação, procure por **cmd** ou **Prompt de Comando** no menur iniciar.
6) Ao abrir digite `python --version` e pressione **Enter**.
   ```bash
   C:\Users\UserName>python --version
   ```
7) Se aparecer uma mensagem monstrando a versão do python, então tudo ocorreu bem.
   ```bash
   C:\Users\UserName>Python 3.8.0
   ```

## Executando Online

[Python Online Compiler, IDE, Editor, Interpreter and REPL](https://repl.it/languages/python3)

## IDLE

IDLE é um Ambiente de Desenvolvimento e Aprendizagem Integrado, ele facilita a criação, modificação e execução de scripts. Há diversas IDLE para trabalhar, Python instala uma por padrão, __Python Shell__. É possível executar python no Terminal no modo interativo.

Para entrar no modo interativo acesse o **Prompt de Comando** no Windows:

1) Digite `python` e pressione **Enter**
  
   ```bash
   C:\Users\UserName>python
   ```

2) Agora você está no modo interativo.

   ```bash
   Python 3.8.0 (default, Apr 18 2020, 01:56:04) 
   [GCC 8.4.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 
   ```

3) Já é possível realizar algumas operações básicas, como somar dois números.

   ```bash
   Python 3.8.0 (default, Apr 18 2020, 01:56:04) 
   [GCC 8.4.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 2+2
   4
   >>>
	```

4) Para sair do modo interativo use o comando `exit()` ou `Ctrl+D`.

## Outras IDLE

* Jupyter Notebook
* PyCharm
* Atom
* Sublime Text
* Visual Studio Code

Atom, Sublime Text e Visual Studio Code são editores de código. Se seu PC tiver um processador fraco e/ou pouca memória RAM, recomendo usar o Sublime Text, ele é extremamente leve. Se não tiver fortes limitações use o Visual Studio Code.

## Executando um Arquivo Python

A extensão de um arquivo python é `.py`. Para rodar um arquivo digite `python` seguido pelo nome do arquivo.

```bash
C:\Users\UserName>python helloworld.py
```

Obs: É necessário que você esteja no mesmo diretório do arquivo. Se o arquivo estiver na Área de Trabalho do Windows é necessário alterar o diretório pelo Terminal. Caso contrário passe o caminho absoluto do arquivo.

No Windows, por padrão ao abrir o Prompt de Comando você estará na sua pasta de usuário.

```bash
C:\Users\UserName>
```

Para ir para a Área de Trabalho (Desktop) use o comando `cd` (*Change Directory*) seguido do nome da pasta.

```bash
C:\Users\UserName>cd Desktop
C:\Users\UserName\Desktop>
```

Agora você pode rodar o arquivo que está na área de trabalho. Outro método é digitar `cmd` na barra de endereço da pasta, [Leia Mais](https://www.thewindowsclub.com/how-to-open-command-prompt-from-right-click-menu/).