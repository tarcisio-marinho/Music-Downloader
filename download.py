#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
#


from constants import *

import youtube_dl
import requests
import bs4 as bs
import os

site = 'https://www.youtube.com/results?search_query='

try:
    musica = input('\33[94mNome ou letra da música: \033[0m')
except KeyboardInterrupt:
    exit()
try:
    r = requests.get(site + musica)
except requests.exceptions.ConnectionError:
    print('Erro conexão')
    exit()

bs_obj = bs.BeautifulSoup(r.text, 'lxml')
lista = []
url = []
i = 0
limite = 8
k = 0

for li in bs_obj.find_all('h3'):
    if(i > 2):
        print('\033[1;32m' + str(i-2) + '\033[0m - ' + li.text+'\n')
        lista.append(li.text)
        for pa in li.find_all('a'):
            url.append(pa.get('href'))
        k += 1
        if(k == limite):
            break
    i += 1

while True:
    try:
        escolha = int(input('\33[94mEscolha uma música: \033[0m')) - 1
        break
    except KeyboardInterrupt:
        exit()
    except:
        print('Apenas números')

print('\33[93mbaixando: ' + lista[escolha] + '\n\n')
link = 'http://www.youtube.com' + url[escolha]
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        os.system('clear')
        diretorio = os.getcwd()
        print('Download pronto!\nSalvo na pasta: ' + diretorio + '/')
except:
    print('Algum erro ocorreu :0')
