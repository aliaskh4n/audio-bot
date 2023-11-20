from pytube import YouTube, Playlist

link = "https://youtu.be/gaJtUpgJDcM?si=ntLiXaV_qJkDKtNd"

def download_audio(link):
    yt = YouTube(link)
    streams = yt.streams.get_by_itag(251)
    return streams.download(output_path="audio", filename='audo.webm')