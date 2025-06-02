import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

DEFAULT_LANGUAGE = "auto"
DEFAULT_SUMMARY_STYLE = "default"

SUPPORTED_LANGUAGES = {
    "auto": "🌍 Автоматически",
    "ru": "🇷🇺 Русский",
    "en": "🇺🇸 English",
    "de": "🇩🇪 Deutsch",

}

SUMMARY_STYLES = {
    "default": {"name": "📝 Стандартное"},
    "short": {"name": "🤏 Очень коротко (1-2 предложения)"},
    "bullet_points": {"name": "🔑 Ключевые пункты"},
    "detailed": {"name": "🧐 Подробное"}
}

WHISPER_MODEL_SIZE = "small"
MAX_MESSAGE_LENGTH = 4096
TRANSCRIPTION_DISPLAY_CHUNK_SIZE = 3800
SUMMARY_DISPLAY_CHUNK_SIZE = 3800