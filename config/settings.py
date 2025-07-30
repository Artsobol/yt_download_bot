import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Папка для временных файлов
TEMP_DIR = os.path.join(BASE_DIR, "tmp")
os.makedirs(TEMP_DIR, exist_ok=True)

FFMPEG_PATH = os.path.join(
    BASE_DIR,
    "bin",      # корневая папка bin вашего проекта
    "ffmpeg",   # подпапка с распакованным ffmpeg
    "bin",      # подпапка bin внутри сборки
    "ffmpeg.exe"  # сам исполняемый файл
)