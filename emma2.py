import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard
from pygame import mixer

name = "emma"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voices", voices[0].id)
engine.setProperty('rate', 145)

def talk(some_text):
    engine.say(some_text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            listener.adjust_for_ambient_noise(source)
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
    except:
        pass
    return rec
def run_emma():
    while True:
        try:
             rec = listen()
        except UnboundLocalError:
                 talk("amo no te entendi, repita de nuevo")
                 continue
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("reproduciendo " + music)
            talk("reproduciendo " + music)
            pywhatkit.playonyt(music)
        elif 'busca' in rec:
            busqueda = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(busqueda, 1)
            print(busqueda  +": " + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            alar = rec.replace('alarma', ' ')
            alar = alar.strip()
            talk("activar alarma a las" + alar + 'horas')
            while True:
                if datetime.datetime.now().strftime('%H:%M') == alar:
                    print('¡Hora de despertar!') 
                    mixer.init()
                    mixer.music.load("El Dulce Sonido de los Pajaros Cantando.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break
        elif 'hola' in rec:
            hol = rec.replace('hola', ' ')
            talk('Hola, como estas?')
        elif 'que, eres' in rec:
            iden = rec.replace('que, eres', ' ')    
            print("soy emma, asistente emocional, creada por jahvid Rivera, estoy programada con la intencion de ser un asistente emocional, con mi ayuda tendras un compañera a quien contarle todos tu problemas.")
            talk("soy emma, asistente emocional, creada por jahvid Rivera, estoy programada con la intencion de ser un asistente emocional, con mi ayuda tendras un compañera a quien contarle todos tu problemas.")
        
if __name__=='__main__':
    run_emma()