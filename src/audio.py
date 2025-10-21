import sounddevice as sd
import numpy as np
import queue

class AudioInput:
    def __init__(self, samplerate=16000, channels=1):
        self.samplerate = samplerate
        self.channels = channels
        self.q = queue.Queue()

    def callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.q.put(indata.copy())

    def start(self):
        with sd.InputStream(samplerate=self.samplerate, channels=self.channels, callback=self.callback):
            while True:
                yield self.q.get()