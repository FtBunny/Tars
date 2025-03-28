import pyttsx3
import speech_recognition as sr
import eel



def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')   
    engine.setProperty('voice', voices[0].id)   
    engine.setProperty('rate', 174)
    print(voices)
    engine.say(text)
    engine.runAndWait()
    
@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise = r.listen(source)
        
        audio = r.listen(source, 10, 6)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        speak(query)
    except Exception as e:
        return ""
    return query.lower()

