# Voice Assistant using OpenAI

A personal voice assistant built with Python that can:
- Listen to voice commands using microphone
- Process commands using OpenAI GPT-4
- Respond with voice output
- Fallback to keyboard input if microphone fails

## Features
- Voice input via SpeechRecognition
- AI responses using OpenAI GPT-4
- Text-to-speech output using pyttsx3
- Keyboard fallback mode
- Wake word "Hey Assistant" support
- Voice exit with "Goodbye"

## Technologies Used
- Python 3.x
- OpenAI API (GPT-4)
- SpeechRecognition
- PyAudio
- pyttsx3
- python-dotenv

## Project Structure
voice_assistant/
├── main.py # Main application
├── assistant/
│ ├── init.py # Package initialization
│ ├── listener.py # Speech-to-text functionality
│ ├── brain.py # OpenAI GPT-4 integration
│ └── speaker.py # Text-to-speech functionality
├── requirements.txt # Dependencies
├── .gitignore # Ignored files
└── README.md # Documentation

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/voice_assistant.git

## Install dependencies
pip install -r requirements.txt

## Create .env file and add your OpenAI API key
OPENAI_API_KEY=your_api_key_here

## Run the assistant
python main.py

