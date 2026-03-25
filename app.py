import gradio as gr
import os

from core.engine import EnglishTutorBot
from core.voice_service import VoiceService
from core.helpers import parse_bot_reply, format_chat_message

# Khởi tạo bot và voice service
bot = EnglishTutorBot()
voice = VoiceService()

def process_voice_input(audio_path, chat_history):
    if chat_history is None:
        chat_history = []

    if audio_path is None:
        return chat_history, None
        
    user_text = voice.transcribe_audio(audio_path)

    if not user_text:
        chat_history.append({"role": "assistant", "content": "🎙️ Mình không nghe rõ. Bạn thử nói lại nhé!"})
        return chat_history, None

    raw_reply = bot.get_response(user_text)

    if not raw_reply:
        chat_history.append({"role": "user", "content": f"🎤 {user_text}"})
        chat_history.append({"role": "assistant", "content": "⚠️ Lỗi kết nối LLM. Thử lại nhé!"})
        return chat_history, None

    parsed = parse_bot_reply(raw_reply)
    formatted = format_chat_message(parsed)
    audio_reply = voice.text_to_speech(raw_reply)

    chat_history.append({"role": "user", "content": f"🎤 {user_text}"})
    chat_history.append({"role": "assistant", "content": formatted})

    return chat_history, audio_reply

def reset_conversation():
    bot.reset_history()
    return [], None

# GIAO DIỆN GRADIO 
with gr.Blocks(title="🎓 AI English Tutor") as demo:
    gr.Markdown(
        """
        # 🎓 AI English Tutor
        HI THERE , IT'S ME!!!
        **Hướng dẫn:** Nhấn giữ nút micro để nói tiếng Anh. Bot sẽ trò chuyện với bạn bằng tiếng anh.
        """
    )

    chatbot = gr.Chatbot(
        label="Hội thoại",
        height=500,
        
    )

    with gr.Row():
        input_audio = gr.Audio(
            sources=["microphone"],
            type="filepath",
            label="🎙️ Nhấn để nói"
        )
        output_audio = gr.Audio(
            autoplay=True,
            label="🔊 Phản hồi của Bot",
            interactive=False
        )

    reset_btn = gr.Button("🗑️ Xóa lịch sử hội thoại", variant="stop")

    input_audio.stop_recording(
        fn=process_voice_input,
        inputs=[input_audio, chatbot],
        outputs=[chatbot, output_audio],
    )

    reset_btn.click(
        fn=reset_conversation,
        inputs=[],
        outputs=[chatbot, output_audio],
    )

if __name__ == "__main__":
    demo.launch(theme="soft")