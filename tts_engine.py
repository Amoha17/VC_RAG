
from gtts import gTTS
from langdetect import detect
import os
import tempfile
import pygame
import time

def speak_gtts(text: str, lang: str = None):
    if lang is None:
        lang = detect(text)

    tts = gTTS(text=text, lang=lang)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_path = fp.name
        tts.save(temp_path)

    # Initialize mixer and play the audio
    pygame.mixer.init()
    pygame.mixer.music.load(temp_path)
    pygame.mixer.music.play()

    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()
    os.remove(temp_path)
