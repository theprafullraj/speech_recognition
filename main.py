import speech_recognition as sr
import os

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("Transcription:", text)

        with open("output/transcribed.txt", "w") as file:
            file.write(text)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

if __name__ == "__main__":
    if not os.path.exists("output"):
        os.makedirs("output")
    speech_to_text()
