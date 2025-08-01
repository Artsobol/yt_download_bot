import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Папка для временных файлов
TEMP_DIR = os.path.join(BASE_DIR, "tmp")
os.makedirs(TEMP_DIR, exist_ok=True)

# Путь до ffmpeg
FFMPEG_PATH = os.path.join(
    BASE_DIR,
    "bin",
    "ffmpeg",
    "bin",
    "ffmpeg.exe"
)