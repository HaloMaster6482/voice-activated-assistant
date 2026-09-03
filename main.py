try:
    import speech_recognition as sr
    import pyttsx3
    from datetime import datetime
except ImportError as e:
    print(f"Error importing modules: {e}. Please ensure all required libraries are installed.")

def speak(text: str):
    engine = pyttsx3.init()
    engine.setProperty('rate', 210)
    engine.say(text)
    engine.runAndWait()

def get_audio() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = str(r.recognize_google(audio))
            return text
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            speak("Could not request results; check your network connection.")
        return ""

def respond_to_command(command: str):
    if "time" in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        today = datetime.now().date()
        speak(f"Today's date is {today}")
    elif "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "bye" in command:
        speak("Goodbye! Have a great day!")
        return False
    elif "weather" in command:
        speak("I'm sorry, I cannot provide weather updates at the moment.")
    elif "your name" in command:
        speak("I am your voice assistant.")
    else:
        speak("I'm not sure how to respond to that.")
    return True

def main():
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        command = get_audio().lower()
        if command:
            if not respond_to_command(command):
                break

if __name__ == "__main__":
    main()