from typing import List, Union

from pytubefix import Stream as PytubeStream
from pytubefix import YouTube

from config.Itag import Itag
from services import FileSize


def get_video_and_audio_stream(
    yt: YouTube, video_itag: int, audio_itag: int = 140
) -> tuple[PytubeStream, PytubeStream]:
    video_stream = get_stream_by_itag(yt, video_itag)
    audio_stream = get_stream_by_itag(yt, audio_itag)
    return video_stream, audio_stream



def get_available_itags(yt: YouTube) -> List[Itag]:
    available_itags = {stream.itag for stream in yt.streams.filter(adaptive=True)}
    return [itag for itag in Itag if itag.value in available_itags]


def get_highest_stream(yt: YouTube) -> PytubeStream:
    return yt.streams.get_highest_resolution()


def get_stream_by_itag(yt: YouTube, itag: Union[int, str]) -> PytubeStream:
    return yt.streams.get_by_itag(itag)


def check_valid_video_and_audio_size(
    video_stream: PytubeStream,
    audio_stream: PytubeStream,
    max_size: int = FileSize.MAX_SIZE,
) -> bool:
    return (video_stream.filesize + audio_stream.filesize) <= max_size


def check_valid_video_size(
    youtube_stream: PytubeStream, max_size: int = FileSize.MAX_SIZE
) -> bool:
    return youtube_stream.filesize <= max_size
