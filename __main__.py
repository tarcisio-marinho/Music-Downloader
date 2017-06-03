import os

from config import diretorio

from constants import BLUE
from constants import GREEN
from constants import YELLOW
from constants import END

from download import get_html
from download import parse_html
from download import get_audio


def main():
    try:
        musica = input(BLUE + 'Nome ou letra da música: ' + END)
    except KeyboardInterrupt:
        exit()

    html = get_html(musica)
    lista = parse_html(html)

    for musica in lista:
        print('{}{} - {}{}\n'.format(GREEN, musica.index, END,  musica.nome))

    while True:
        try:
            escolha = int(input(BLUE + 'Escolha uma música: ' + END)) - 1
            break
        except KeyboardInterrupt:
            exit()
        except:
            print('Apenas números')

    print(YELLOW + 'baixando: ' + lista[escolha].nome + '\n\n')
    link = 'http://www.youtube.com' + lista[escolha].url
    os.chdir(diretorio)
    get_audio(link)
    os.system('clear')
    print('Download pronto!\nSalvo na pasta: ' + diretorio + '/')


if __name__ == '__main__':
    main()
