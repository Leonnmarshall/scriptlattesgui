scriptLattesGUI
===============

Interface gráfica e instalador Windows para o [ScriptLattes][1]
[1]: http://scriptlattes.sourceforge.net/code.html

[Baixar versão do Windows][2]

Adaptação no arquivo .config
============================

Para executar no ambiente gráfico, é necessário que os arquivos **".config"** estejam no mesmo formato que o aceito pelo scriptLattes, alterando para que os caminhos das pastas não utilizem caminho exato, e sim relativo.

Por exemplo:
```
global-arquivo_de_entrada  = ./exemplo/teste-01.list
```

Para quando o arquivo "teste-01.list" está na mesma pasta "exemplo", o valor deve ficar:
```
global-arquivo_de_entrada  = teste-01.list
```
  
O scriptLattesGUI sempre irá procurar os caminhos a partir do arquivo **".config"** indicado.


Binário no Windows
==================

O instalador contendo todos os requisitos pode ser baixado em [Release Beta 1][2].

[2]: https://github.com/rfaga/scriptlattesgui/releases/tag/beta1

Instruções para Linux
=====================

É necessário instalar os mesmos pacotes do scriptLattes + python-pyside:
```sh
sudo apt-get install python-all python-setuptools python-utidylib python-matplotlib python-levenshtein python-pygraphviz python-numpy tidy python-scipy python-imaging python-pyside
easy_install pytidylib
```
  
Para executar a interface gráfica, executar o arquivo main.py:
```sh
cd /diretorio/do/projeto
chmod +x main.py
./main.py
```
