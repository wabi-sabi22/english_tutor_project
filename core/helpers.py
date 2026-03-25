
import re
from dataclasses import dataclass


@dataclass
class ParsedReply:
    """Structured version của bot response sau khi parse."""
    correction: str = ""
    response: str = ""
    vietnamese: str = ""
    raw: str = ""


def parse_bot_reply(text: str) -> ParsedReply:
    """
    Parse bot reply theo format trong SYSTEM_PROMPT thành các phần riêng biệt.

    Expected format:
        ✅ Correction:
        ...

        💬 Response:
        ...

        ---

        🇻🇳 Dịch tiếng Việt:
        ...
    """
    result = ParsedReply(raw=text)

    correction_match = re.search(
        r"\s*Correction:\s*(.*?)(?=💬\s*Response:|---|\Z)",
        text, re.DOTALL
    )
    response_match = re.search(
        r"💬\s*Response:\s*(.*?)(?=---|🇻🇳|\Z)",
        text, re.DOTALL
    )
    vietnamese_match = re.search(
        r"🇻🇳\s*Dịch tiếng Việt:\s*(.*?)$",
        text, re.DOTALL
    )

    if correction_match:
        result.correction = correction_match.group(1).strip()
    if response_match:
        result.response = response_match.group(1).strip()
    if vietnamese_match:
        result.vietnamese = vietnamese_match.group(1).strip()

    return result


def format_chat_message(parsed: ParsedReply) -> str:
    """
    Tạo chuỗi hiển thị 
    """
    parts = []

    if parsed.correction:
        parts.append(f" **Correction:**\n{parsed.correction}")

    if parsed.response:
        parts.append(f" **Response:**\n{parsed.response}")

    if parsed.vietnamese:
        parts.append(f"---\n🇻🇳 **Dịch tiếng Việt:**\n{parsed.vietnamese}")

    return "\n\n".join(parts) if parts else parsed.raw