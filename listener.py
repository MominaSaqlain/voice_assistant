import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Sun raha hoon...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("👤 You:", text)
        return text
    except:
        return "Sorry, main samajh nahi paya"
