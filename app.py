import yt_dlp
import os

def download_audio(url):
    # TODO
    yt_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '0',
        }],
        'outtmpl': 'tmp/%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(yt_opts) as yt:
        yt.download([url])

def download_video(url):
    # TODO
    print(XD)

if __name__ == '__main__':
    opt = input("Que desea descargar [Audio] [Video]: ")

    if not os.path.exists("tmp"):
        os.mkdir("tmp")
        print("Creado el directorio tmp")

    if not os.path.exists("downloads"):
        os.mkdir("downloads")
        print("Creado el directorio downloads")

    if "Audio" in opt or "audio" in opt:
        link = input("Dame el link del audio a descargar: ")
        download_audio(link)
    else:
        link = input("Dame el link del video a descargar: ")
        download_video(link)

