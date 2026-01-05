from assistant.listener import listen
from assistant.brain import ask_gpt
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def run_assistant():
    print("🤖 Assistant: Hello Momina, I am your personal voice assistant. Say 'Hey Assistant' to start.")
    while True:
        command = listen()
        if not command:
            continue
        answer = ask_gpt(command)
        print("🤖", answer)
        speak(answer)

if __name__ == "__main__":
    run_assistant()
