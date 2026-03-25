
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from settings import LLM_CFG
from core.prompts import SYSTEM_PROMPT

load_dotenv()


class EnglishTutorBot:
    """
    Wraps the LLM and maintains conversation history.

    """

    def __init__(self, cfg=LLM_CFG):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise EnvironmentError(
                "GROQ_API_KEY không tìm thấy. Kiểm tra file .env"
            )

        self.llm = ChatGroq(
            groq_api_key=api_key,
            model_name=cfg.model_name,
            temperature=cfg.temperature,
            max_tokens=cfg.max_tokens,
        )
        # System prompt là message đầu tiên cố định trong history
        self._history: list = [SystemMessage(content=SYSTEM_PROMPT)]

    # Public API

    def get_response(self, user_text: str) -> str:
        """
        Nhận text từ user, trả về response string theo format trong SYSTEM_PROMPT.
        Chat history được giữ tự động.
        """
        if not user_text or not user_text.strip():
            return ""

        self._history.append(HumanMessage(content=user_text.strip()))
        response = self.llm.invoke(self._history)
        self._history.append(AIMessage(content=response.content))

        return response.content

    def reset_history(self) -> None:
        """Xoá lịch sử hội thoại, giữ lại system prompt."""
        self._history = [SystemMessage(content=SYSTEM_PROMPT)]

    # Private helpers 

    def _maybe_summarize_history(self, max_turns: int = 20) -> None:
        """
        Placeholder: khi history > max_turns, có thể gọi LLM để tóm tắt
        rồi replace history cũ bằng bản tóm tắt → tiết kiệm token.
        """
        pass