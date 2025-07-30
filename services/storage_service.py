import asyncio
import os
from pathlib import Path

from pytubefix import Stream as PytubeStream

async def download_video(youtube_stream: PytubeStream) -> str:
    filepath: str = await asyncio.to_thread(youtube_stream.download)
    return filepath

async def delete_video(path: str | Path) -> None:
    await asyncio.to_thread(os.remove, path)