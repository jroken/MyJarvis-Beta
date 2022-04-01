from time import sleep
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init("sapi5")
engine.setProperty('rate', 130)
sleep(2)
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening:" + str(r.energy_threshold))
        ses = r.listen(source, timeout=10, phrase_time_limit=10)
        print(r.recognize_google(ses, language='tr-tr'))
        veri = r.recognize_google(ses, language='tr-tr')
    if (veri == 'Jarvis'):
        speak('Yes, I am listening you')
    if (veri=='Jarvis Işıkları Aç'):
        speak("Okey the lights are on")
