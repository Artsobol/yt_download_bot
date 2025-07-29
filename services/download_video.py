from pytubefix import YouTube

def get_video(url):
    yt = YouTube(url)

    ys = yt.streams.get_highest_resolution()
    return ys.download()