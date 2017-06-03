import os


diretorio = os.path.join(os.path.expanduser('~'), 'Música')
limite = 8
site = 'https://www.youtube.com/results?search_query='

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
