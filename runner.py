#!/usr/bin/python
# encoding: utf-8
#
#  scriptLattes V8
#  Copyright 2005-2013: Jesús P. Mena-Chalco e Roberto M. Cesar-Jr.
#
#  http://scriptlattes.sourceforge.net/
#
#
#  GUI/Windows version
#  Copyright 2014: Roberto Faga Jr e Dorival Piedade Neto
#
#  http://github.com/rfaga/scriptlattesgui
#
#
#  Este programa é um software livre; você pode redistribui-lo e/ou 
#  modifica-lo dentro dos termos da Licença Pública Geral GNU como 
#  publicada pela Fundação do Software Livre (FSF); na versão 2 da 
#  Licença, ou (na sua opinião) qualquer versão.
#
#  Este programa é distribuído na esperança que possa ser util, 
#  mas SEM NENHUMA GARANTIA; sem uma garantia implicita de ADEQUAÇÂO a qualquer
#  MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#  Licença Pública Geral GNU para maiores detalhes.
#
#  Você deve ter recebido uma cópia da Licença Pública Geral GNU
#  junto com este programa, se não, escreva para a Fundação do Software
#  Livre(FSF) Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#

#force imports
import matplotlib
import numpy
from scipy import sparse
import matplotlib.pyplot as plt
import pygraphviz
from PIL import Image

import operator
import math
import re
import fileinput
import sets
import HTMLParser
import urllib, urllib2
import cookielib
import time
import tidylib
import htmlentitydefs
import xml.dom.minidom
import sys
import shutil
import Levenshtein
import os, errno

SEP = os.path.sep

import sys
import shutil
import Levenshtein
import os, errno

SEP = os.path.sep
BASE = 'lattes' + SEP + 'scriptLattes' + SEP
ABSBASE = os.path.abspath(BASE) + SEP
sys.path.append('lattes')
sys.path.append(BASE)
sys.path.append(BASE + 'producoesBibliograficas')
sys.path.append(BASE + 'producoesTecnicas')
sys.path.append(BASE + 'producoesArtisticas')
sys.path.append(BASE + 'producoesUnitarias')
sys.path.append(BASE + 'orientacoes')
sys.path.append(BASE + 'eventos')
sys.path.append(BASE + 'charts')
sys.path.append(BASE + 'internacionalizacao')
sys.path.append(BASE + 'qualis')

from grupo import *

def copy_files(dir):
	base = ABSBASE
	shutil.copy2(base + 'css'+SEP+'scriptLattes.css', dir)
	shutil.copy2(base + 'imagens'+SEP+'lattesPoint0.png', dir)
	shutil.copy2(base + 'imagens'+SEP+'lattesPoint1.png', dir)
	shutil.copy2(base + 'imagens'+SEP+'lattesPoint2.png', dir)
	shutil.copy2(base + 'imagens'+SEP+'lattesPoint3.png', dir)
	shutil.copy2(base + 'imagens'+SEP+'lattesPoint_shadow.png', dir)
	shutil.copy2(base + 'imagens'+SEP+'doi.png', dir)

if __name__ == "__main__":
	print sys.argv
	arquivoConfiguracao = sys.argv[1]
	os.chdir( os.path.abspath(os.path.join(arquivoConfiguracao, os.pardir)))
	novoGrupo = Grupo(arquivoConfiguracao)
	novoGrupo.imprimirListaDeParametros()
	novoGrupo.imprimirListaDeRotulos()

	if criarDiretorio(novoGrupo.obterParametro('global-diretorio_de_saida')):
		novoGrupo.carregarDadosCVLattes() #obrigatorio
		novoGrupo.compilarListasDeItems() # obrigatorio
		novoGrupo.identificarQualisEmPublicacoes() # obrigatorio
		novoGrupo.calcularInternacionalizacao() # obrigatorio
		novoGrupo.imprimirMatrizesDeFrequencia() 

		novoGrupo.gerarGrafosDeColaboracoes() # obrigatorio
		print "[ROTULOS]"
		print "- "+str(novoGrupo.listaDeRotulos)
		print "- "+str(novoGrupo.listaDeRotulosCores)

		novoGrupo.gerarGraficosDeBarras() # obrigatorio
		novoGrupo.gerarMapaDeGeolocalizacao() # obrigatorio
		novoGrupo.gerarPaginasWeb() # obrigatorio

		novoGrupo.gerarXMLdeGrupo()
		novoGrupo.gerarCSVdeQualisdeGrupo()
		novoGrupo.gerarRISdeGrupo()

		# copiar imagens e css
		copy_files(novoGrupo.obterParametro('global-diretorio_de_saida'))

		# finalizando o processo
		#print '[AVISO] Quem vê \'Lattes\', não vê coração! B-)'
		#print '[AVISO] Por favor, cadastre-se na página: http://scriptlattes.sourceforge.net\n'
		print '\n\n\n[COMO REFERENCIAR ESTE TRABALHO]'
		print '    Jesus P. Mena-Chalco e Roberto M. Cesar-Jr.'
		print '    scriptLattes: An open-source knowledge extraction system from the Lattes Platform.'
		print '    Journal of the Brazilian Computer Society, vol.15, n.4, páginas 31-39, 2009.'

		print '\n\nscriptLattes executado!'

# ---------------------------------------------------------------------------- #
def compararCadeias(str1, str2, qualis=False):
	str1 = str1.strip().lower()
	str2 = str2.strip().lower()

	if len(str1)==0 or len(str2)==0:
		return 0
	
	if len(str1)>=20 and len(str2)>=20 and (str1 in str2 or str2 in str1):
		return 1

	if qualis:
		dist = Levenshtein.ratio(str1, str2)
		if len(str1)>=10 and len(str2)>=10 and dist>=0.80:
			#return 1
			return dist

	else:
		if len(str1)>=10 and len(str2)>=10 and Levenshtein.distance(str1, str2)<=5:
			return 1
	return 0

def criarDiretorio(dir):
	if not os.path.exists(dir):
		try:
			os.makedirs(dir)
		### except OSError as exc:
		except:
			print "\n[ERRO] Não foi possível criar ou atualizar o diretório: "+dir.encode('utf8')
			print "[ERRO] Você conta com as permissões de escrita? \n"
			return 0
	return 1


