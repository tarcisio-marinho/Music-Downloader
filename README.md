# Music Downloader
Baixe músicas de uma forma simples :D

Esqueceu o nome da música? escreva uma parte da letra, ou simplesmente baixe pelo link.

Baixe playlists inteiras do youtube.


# Usage: 

    usage: download [-h] [-p] [-m] [-d] [-l]

    Music-Downloader baixe músicas de um jeito simples Digitando o nome da
    música ou trexos/letra da música.

    optional arguments:
      -h, --help         show this help message and exit
      -p , --playlist    Download entire youtube playlist
      -m , --music       Nome da música ou letra/trexo da música.
      -d , --directory   Local onde serão salvo as suas músicas.
      -l , --link        Link da música para ser baixada

# Examples

    download -p snuff -d ~/Desktop/Musicas/ 
    download -p [LINK]
    download -l https://www.youtube.com/watch?v=5abamRO41fE

# Tutorial Download 

https://www.youtube.com/watch?v=sh8lpp3kYoo

# Download:

https://sourceforge.net/projects/music-download/files/download/download

# After download:

    sudo cp download /usr/bin/download
this will make the download as a intern program

# Compiling
    If you want to compile yourself, run:
    chmod +x requeriments.sh
    ./requeriments.sh
    pyinstaller -F --clean main.py -n download
