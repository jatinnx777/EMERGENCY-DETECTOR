import sounddevice as sd
import vosk
import json
import time
from datetime import datetime
from config import MODEL_PATH, ALERT_SOUND
from detector import KeywordDetector
from audio import AudioInput

def main():
    model = vosk.Model(MODEL_PATH)
    keyword_detector = KeywordDetector(model)
    audio_input = AudioInput(keyword_detector)

    print("Listening for emergency keywords...")
    audio_input.start_listening()

if __name__ == "__main__":
    main()