import pyttsx3

def speak_text(text: str):
    engine = pyttsx3.init()                  # Initializes the TTS engine
    engine.setProperty('rate', 150)          # Sets the speed of speech
    engine.setProperty('volume', 1.0)        # Sets the volume (1.0 is max)
    engine.say(text)                         # Queues the text to be spoken
    engine.runAndWait()                      # Blocks while speaking the text

