---
🎓 AI English Tutor
---
Your Personal AI Speaking Coach for Real-Time Fluency
AI English Tutor is an interactive voice-to-voice application designed to help English learners break the "speaking barrier." By providing a judgment-free environment, it helps you build reflexes, correct grammar in real-time, and practice natural conversations.
<img width="1564" height="914" alt="image" src="https://github.com/user-attachments/assets/ee0b22ff-de10-4a4d-a720-b9e91c96a111" />

<img width="1749" height="916" alt="image" src="https://github.com/user-attachments/assets/0720ca31-4e0c-4357-9f6d-57500f47ff68" />


View Demo ()

Deloy: (https://huggingface.co/spaces/nhu445/ai-english-tutor)

🌟 The Problem It Solves
Many students possess strong "passive English" (reading and writing) but struggle with "active English" (speaking). This project creates a low-pressure environment to:
Build instant speaking reflexes.
Get immediate corrections on sentence structure.
Practice listening to various native accents.
Bridge the gap between thinking in a native language and speaking in English.

✨ Key Features

🎙️ Voice-First Interaction: Uses Google STT for high-accuracy voice recognition with a simple hold-to-talk interface.

🧠 Intelligent Feedback: Powered by Llama-3.3-70B via Groq to provide native-level corrections and contextual follow-up questions.
🇻🇳 Bilingual Support: Provides both the English response and its Vietnamese translation to ensure full comprehension.

🔊 Natural Text-to-Speech: Integrated with gTTS to read responses aloud in customizable US or UK accents

📱 Clean Interface: A modern Gradio UI featuring full chat history and session management.

🏗️ Project Architecture

The system operates on a modular pipeline to ensure low latency:
User Layer: Gradio captures audio input from the user.
Voice Layer: Google STT converts audio to text; gTTS converts AI text back to audio.
Intelligence Layer: Groq Cloud processes the text through Llama-3.3 to analyze grammar and generate natural dialogue.
Formatting Layer: Custom parsers split the AI response into English, Corrections, and Translations for the UI

📁 File Structure
---
<img width="810" height="392" alt="image" src="https://github.com/user-attachments/assets/8aedd887-48e1-4a07-9083-01fcaf092ac7" />

---

*1.Clone the Repository:*

git clone https://github.com/your-username/ai-english-tutor.git

cd ai-english-tutor

*2.Environment Setup

pip install -r requirements.txt

*3. API Configuration

Create a .env file in the root directory and add your Groq API key:*

GROQ_API_KEY=your_groq_api_key_here

*4. Run the Application

Launch the local server:*

python app.py

--->>> Access the interface at http://127.0.0.1:7860
---
