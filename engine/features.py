from playsound import playsound
import eel



# Play assistant sound

@eel.expose
def playAssistantSound():
    music_dir = r"www\\assets\audio\start_sound.mp3"
    playsound(music_dir)
    