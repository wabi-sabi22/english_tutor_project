"""
core/voice_service.py — STT (speech-to-text) và TTS (text-to-speech).
"""
import os
import logging

import speech_recognition as sr
from gtts import gTTS

from settings import VOICE_CFG

logger = logging.getLogger(__name__)


class VoiceService:
    """
    Extending:
    """

    def __init__(self, cfg=VOICE_CFG):
        self.cfg = cfg
        self.recognizer = sr.Recognizer()

    # STT

    def transcribe_audio(self, audio_path: str | None) -> str:
        """
        Chuyển file âm thanh → text tiếng Anh.
        Trả về chuỗi rỗng nếu không nhận ra hoặc có lỗi.
        """
        if not audio_path:
            return ""

        try:
            with sr.AudioFile(audio_path) as source:
                self.recognizer.adjust_for_ambient_noise(
                    source, duration=self.cfg.stt_ambient_duration
                )
                audio_data = self.recognizer.record(source)

            return self.recognizer.recognize_google(
                audio_data, language=self.cfg.stt_language
            )

        except sr.UnknownValueError:
            logger.warning("STT: Không nghe rõ giọng nói.")
            return ""
        except sr.RequestError as e:
            logger.error("STT: Lỗi kết nối Google API — %s", e)
            return ""
        except Exception as e:
            logger.error("STT: Lỗi không xác định — %s", e)
            return ""
    # TTS

    def text_to_speech(self, text: str) -> str | None:
        """
        Chuyển text → file MP3.
        Trả về đường dẫn file MP3 nếu thành công, hoặc None nếu có lỗi.
        """
        if not text or not text.strip():
            return None

        english_only = self._extract_english(text)
        if not english_only:
            return None

        try:
            os.makedirs(self.cfg.tts_output_dir, exist_ok=True)
            tts = gTTS(text=english_only, lang=self.cfg.tts_language, tld=self.cfg.tts_tld)
            tts.save(self.cfg.tts_output_file)
            return self.cfg.tts_output_file

        except Exception as e:
            logger.error("TTS: Lỗi tạo audio — %s", e)
            return None

    # Private helpers

    @staticmethod
    def _extract_english(bot_reply: str) -> str:
        """
        Lấy phần tiếng Anh để đọc to — bỏ phần dịch tiếng Việt.
        Phần dịch bắt đầu sau dấu '---' hoặc '🇻🇳 Dịch tiếng Việt:'.
        """
        for separator in ("---", "🇻🇳 Dịch tiếng Việt:"):
            if separator in bot_reply:
                return bot_reply.split(separator)[0].strip()
        return bot_reply.strip()