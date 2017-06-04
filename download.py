#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import youtube_dl
import requests
import bs4 as bs
import lxml
import os

# CORES NO TERMINAL
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
site = 'https://www.youtube.com/results?search_query='

# BUSCA NO SITE O NOME DIGITADO
try:
    musica=raw_input('\33[94mNome ou letra da música: \033[0m')
except KeyboardInterrupt:
    exit()
try:
    r=requests.get(site+musica)
except requests.exceptions.ConnectionError:
    print('Erro conexão')
    exit()
bs_obj = bs.BeautifulSoup(r.text, 'lxml')
lista=[]
url=[]
i=0
limite=8
k=0

# PROCURA TODOS OS LI'S NO CODIGO HTML DO RETORNO DA PAGINA
for li in bs_obj.find_all('h3'):
    if(i>2):
        print('\033[1;32m'+str(i-2)+'\033[0m - '+li.text+'\n')
        lista.append(li.text)
        for pa in li.find_all('a'):
            url.append(pa.get('href'))
        k+=1
        if(k==limite):
            break
    i+=1

# ESCOLHA DE MUSICA
while True:
    try:
        escolha=int(input('\33[94mEscolha uma música: \033[0m'))-1
        break
    except KeyboardInterrupt:
        exit()
    except:
        print('Apenas números')

# CONFIGURAÇÕES DE DOWNLOAD E LINK DE ESCOLHA DA MUSICA
print('\33[93mbaixando: '+lista[escolha]+'\n\n')
link='http://www.youtube.com'+url[escolha]
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# TENTA SALVAR A MUSICA NA ÁREA DE TRABALHO
if(os.path.isdir(os.environ['HOME']+'/Desktop/')):
    os.chdir(os.environ['HOME']+'/Desktop/')
elif(os.path.isdir(os.environ['HOME']+'/Área\ de\ Trabalho/')):
    os.chdir(os.environ['HOME']+'/Área\ de\ Trabalho/')

# FAZ O DOWNLOAD 
try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        os.system('clear')
        diretorio=os.getcwd()
        print('Download pronto!\nSalvo na pasta: '+diretorio+'/')
except:
    print('Algum erro ocorreu :0')
