import pytubefix
from pytubefix.cli import on_progress

url = str(input('URL do vídeo: '))
destino = 'D:\Downloads videos python'

audio_ou_video = int(input('ÁUDIO [1] OU VÍDEO [2]'))

if audio_ou_video == 1:
    yt = pytubefix.YouTube(url, on_progress_callback= on_progress)
    print( yt.title)

    ys = yt.streams.get_audio_only()

    ys.download(output_path=destino)

if audio_ou_video == 2:
    yt = pytubefix.YouTube(url, on_progress_callback= on_progress)
    print( yt.title)

    ys = yt.streams.get_highest_resolution()

    ys.download(output_path=destino)

else:
    print('ERRO')
