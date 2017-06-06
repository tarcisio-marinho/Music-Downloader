#!/bin/bash/env python
# coding=UTF-8
# by Tarcisio marinho
# github.com/tarcisio-marinho


from bs4 import BeautifulSoup
from collections import namedtuple
import youtube_dl
import requests

from .config import limite
from .config import ydl_opts
from .config import site


def get_html(musica):
    try:
        resp = requests.get(site + musica)
    except requests.exceptions.ConnectionError:
        print('Erro conexão')
        exit()
    return resp.text


def parse_html(resp):
    lista = []
    bs_obj = BeautifulSoup(resp, 'lxml')

    i = 0
    for li in bs_obj.find_all('h3')[3:]:
        musica = namedtuple('Musica', ['index', 'nome', 'url'])
        musica.nome = li.text
        musica.index = i
        for pa in li.find_all('a'):
            musica.url = pa.get('href')
        lista.append(musica)
        i += 1
        if(i == limite):
            break
    return lista


def get_audio(link):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except:
        print('erro indesperado em download.get_audio()')
