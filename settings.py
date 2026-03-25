"""
config.py — Tập trung toàn bộ cấu hình của dự án.
Khi dự án lớn lên, chỉ cần sửa file này.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class LLMConfig:
    # Groq models: llama-3.3-70b-versatile | mixtral-8x7b-32768 | gemma2-9b-it
    model_name: str = "llama-3.3-70b-versatile"
    temperature: float = 0.5
    max_tokens: int = 1024


@dataclass(frozen=True)
class VoiceConfig:
    # Speech recognition language
    stt_language: str = "en-US"
    stt_ambient_duration: float = 0.5

    # gTTS: tld='com' → giọng Mỹ | tld='co.uk' → giọng Anh
    tts_language: str = "en"
    tts_tld: str = "com"
    tts_output_dir: str = "temp"
    tts_output_file: str = "temp/response.mp3"


@dataclass(frozen=True)
class AppConfig:
    title: str = "🎓 AI English Tutor"
    theme: str = "soft"

# Singleton instances  
LLM_CFG = LLMConfig()
VOICE_CFG = VoiceConfig()
APP_CFG = AppConfig()