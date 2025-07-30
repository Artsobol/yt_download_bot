import asyncio
from pathlib import Path

from pytubefix import Stream as PytubeStream

from config.settings import TEMP_DIR
from services.ffmpeg_service import ffmpeg_merge_streams


async def merge_streams(video_path: Path | str, audio_path: Path | str, output_file: Path | None = None) -> str:
    if output_file is None:
        output_file = Path(TEMP_DIR) / f"{video_path.stem}_merged.mp4"

    merged_video = ffmpeg_merge_streams(video_path, audio_path, output_file)
    return merged_video

async def download_video(youtube_stream: PytubeStream) -> str:
    filepath: str = await asyncio.to_thread(youtube_stream.download)
    return filepath

async def delete_all(*paths: str | Path) -> None:
    await asyncio.gather(*(delete_file(p) for p in paths))

async def delete_file(path: str | Path) -> None:
    path = Path(path)
    if path.exists():
        await asyncio.to_thread(path.unlink)