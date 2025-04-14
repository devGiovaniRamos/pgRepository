import pytubefix
from pytubefix.cli import on_progress

url = str(input('URL do vídeo: '))
destino = 'D:\Downloads videos python'

yt = pytubefix.YouTube(url, on_progress_callback= on_progress)
print( yt.title)

ys = yt.streams.get_highest_resolution(1080)

ys.download(output_path=destino)
