import speech_recognition
import pyttsx3

reconAudio = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            reconAudio.adjust_for_ambient_noise(mic, duration=0.5)
            audio = reconAudio.listen(mic)

            text = reconAudio.recognize_google(audio)
            text = text.lower()

            print(f"Recognized Audio: {text}")
    except speech_recognition.UnknownValueError():
        reconAudio = speech_recognition.Recognizer()
        continue
