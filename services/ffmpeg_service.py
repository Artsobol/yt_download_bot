import subprocess
from pathlib import Path
from config.settings import FFMPEG_PATH

def ffmpeg_merge_streams(video_file: Path | str, audio_file: Path | str, output_file: Path | str) -> str:
    cmd = [
        FFMPEG_PATH,
        "-y",
        "-i", str(video_file),
        "-i", str(audio_file),
        "-c", "copy",
        str(output_file),
    ]
    subprocess.run(cmd, check=True)
    return output_file
