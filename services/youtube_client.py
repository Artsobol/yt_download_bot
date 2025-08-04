from pytubefix import YouTube


def get_youtube_object(url) -> YouTube:
    return YouTube(url)


def get_thumbnail_url(yt: YouTube) -> str:
    return yt.thumbnail_url
