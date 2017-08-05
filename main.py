#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho
import youtube_dl
import requests
import bs4 as bs
import lxml
import os
import argparse
import subprocess
import sys

# argparse
parser = argparse.ArgumentParser(description='Music-Downloader baixe músicas de um jeito simples\nDigitando o nome da música ou trexos/letra da música')
parser.add_argument('-p', '--playlist', type = str, required = False, metavar = '',  help = 'Download entire youtube playlist')
parser.add_argument('-m', '--music', type = str, required = False, metavar = '',  help = 'Nome da música ou letra/trexo da música.')
parser.add_argument('-d', '--directory', type = str, required = False, metavar = '', help = 'Local onde serão salvo as suas músicas.')
parser.add_argument('-l', '--link', type = str, required = False, metavar = '', help = 'Link da música para ser baixada')
args = parser.parse_args()

# CORES NO TERMINAL
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def error(text):
    sys.exit(text)

def playlist(link, saida):
    os.chdir(saida)
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
            print('Download pronto!\nSalvo na pasta: '+saida)
    except:
        error('Error ao baixar a música.')

def link(l, saida):
    os.chdir(saida)
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
            ydl.download([l])
            os.system('clear')
            print('Download pronto!\nSalvo na pasta: '+saida)
    except:
        error('Error ao baixar a música.')


def busca_musica(musica, saida):
    site = 'https://www.youtube.com/results?search_query='
    if(not musica):
        try:
            musica=raw_input('\33[94mNome ou letra da música: \033[0m')
        except KeyboardInterrupt:
            exit()
    try:
        r=requests.get(site+musica)
    except requests.exceptions.ConnectionError:
        erorr('Erro de conexão. Verifique sua conexão com a internet.')
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
            error('Você escolheu sair.')
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
    if(not saida):
        if(os.path.isdir(os.environ['HOME']+'/Desktop/')):
            os.chdir(os.environ['HOME']+'/Desktop/')
        elif(os.path.isdir(os.environ['HOME']+'/Área\ de\ Trabalho/')):
            os.chdir(os.environ['HOME']+'/Área\ de\ Trabalho/')

    # faz o urro, digo, DOWNLOAD
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            os.system('clear')
            diretorio=os.getcwd()
            print('Download pronto!\nSalvo na pasta: '+diretorio+'/')
    except:
<<<<<<< HEAD
        error('Error ao baixar a música.')

if __name__ == '__main__':
    if not os.name == 'posix':
        error('Sistema não suportado')

    caminho = os.path.expanduser('~')+'/Desktop/'
    caminho2 = os.path.expanduser('~')+'/Área\ de\ Trabalho/'
    if(os.path.isdir(caminho)):
        saida = caminho
    elif(os.path.isdir(caminho2)):
        saida = caminho2

    if(args.directory):
        if(os.path.isdir(args.directory)):
            saida = args.directory
        else:
            try:
                os.mkdir(args.directory)
            except:
                print('Erro ao criar diretorio ' + args.directory + '. Música será salva no caminho: ' + saida)

    if ((not args.link) and (not args.playlist) and args.music): # music
        busca_musica(args.music, saida)
    elif(args.link and (not args.playlist) and (not args.music)): # link
        link(args.link, saida)
    elif(not (args.link or args.playlist or args.music)): # neither
        busca_musica(None, saida)
    elif(args.link and args.playlist and args.music): # both
        error('Apenas link -l ou playlist -p ou letra -p.\nUse -h para obter ajuda')
    elif((not args.link) and (not args.music) and args.playlist): # playlist
        playlist(args.playlist, saida)
    else:
        error('Sintaxe errada, apenas utilize -p ou -l ou -m\nUse -h para ajda')
=======
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
if(os.path.isdir(os.path.expanduser('~')+'/Desktop/')):
    os.chdir(os.path.expanduser('~')+'/Desktop/')
elif(os.path.isdir(os.path.expanduser('~')+'/Área\ de\ Trabalho/')):
    os.chdir(os.path.expanduser('~')+'/Área\ de\ Trabalho/')

# FAZ O DOWNLOAD 
try:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        os.system('clear')
        diretorio=os.getcwd()
        print('Download pronto!\nSalvo na pasta: '+diretorio+'/')
except:
    print('Algum erro ocorreu :0')
>>>>>>> 10688de0d6ba722925fd6a78f6c3bf469f8e35e7
