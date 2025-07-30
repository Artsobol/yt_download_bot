from pytubefix import YouTube
from pytubefix import Stream as PytubeStream

from .file_size import FileSize

def get_highest_stream(yt: YouTube) -> PytubeStream:
    return yt.streams.get_highest_resolution()

def check_valid_video_size(youtube_stream: PytubeStream, max_size: int = FileSize.MAX_SIZE) -> bool:
    return youtube_stream.filesize <= max_size