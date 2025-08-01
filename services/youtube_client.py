from pytubefix import YouTube


def get_youtube_object(url):
    return YouTube(url)

def get_thumbnail_url(yt: YouTube):
    return yt.thumbnail_url