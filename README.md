# 🎙️ Voice Assistant (J.A.R.V.I.S)

## 🤖 Overview

This is a Python-based Voice Assistant project inspired by **J.A.R.V.I.S** from Iron Man. It listens to voice commands and responds with speech, performing a variety of tasks like playing music, telling the weather, opening applications, searching the web, and more.

## ✨ Features

- 🎧 Speech Recognition and Text-to-Speech
- 🌤️ Get Weather Updates
- 📅 Tell Date and Time
- 📂 Open Applications and Files
- 🔊 Control System Volume and Brightness
- 📺 Play YouTube Videos and Songs
- 💬 Tell Jokes, Facts, and Quotes

## 🛠️ Technologies Used

- **Python 3**
- `speech_recognition` - for listening
- `pyttsx3` - for speaking
- `pywhatkit` - for YouTube, WhatsApp, etc.
- `datetime`, `os`, `webbrowser` - for system tasks
- `pyjokes`, `requests`, `wikipedia` - for fun and information
- `pyaudio` - for mic input (install via pip or wheel)

## 📦 Installation

git clone https://github.com/your-username/voice-assistant.git

cd voice-assistant

pip install -r requirements.txt

If pyaudio doesn't install, use:

pip install pipwin

pipwin install pyaudio


▶️ How to Run

python assistant.py

"play Alan Walker faded"

"what's the weather in Mumbai"

"tell me a joke"

"open YouTube"

"what time is it"

"increase volume"

💡 Future Plans

-Add GPT-based conversation mode

-Add GUI interface using Tkinter/PyQt

-Integrate home automation

-Add face authentication

-Add command history and context memory

🧑‍💻 Author
Prateek
Computer Science & Engineering Student
LinkedIn | GitHub

⚠️ Note: Ensure your microphone is working and your environment is relatively quiet for better recognition.
