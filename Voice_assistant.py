import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your command.")
        return ""
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
        return ""

def speak(response):
    text_to_speech.say(response)
    text_to_speech.runAndWait()

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "what's the time" in command:
        # You can use the datetime module to get the current time
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    else:
        speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I assist you today?")
    while True:
        command = listen_for_command()
        process_command(command)
git 