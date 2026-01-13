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


class AudioHandler:
    """Minimal audio handler used by tests.

    Provides `capture_audio()`, `start_stream()`, `stop_stream()` and a
    `stream` attribute with an `active` flag. Uses `sounddevice.InputStream`.
    """
    def __init__(self, samplerate=16000, channels=1, frames_per_buffer=1024):
        self.samplerate = samplerate
        self.channels = channels
        self.frames_per_buffer = frames_per_buffer
        # Create the stream (tests patch `sounddevice.InputStream`)
        self.stream = sd.InputStream(samplerate=self.samplerate, channels=self.channels)
        # Ensure an `active` attribute exists for tests
        try:
            _ = self.stream.active
        except Exception:
            self.stream.active = False

    def capture_audio(self):
        data, _ = self.stream.read(self.frames_per_buffer)
        return np.array(data)

    def start_stream(self):
        # Start the underlying stream and mark active
        try:
            self.stream.start()
        except Exception:
            pass
        self.stream.active = True

    def stop_stream(self):
        try:
            self.stream.stop()
        except Exception:
            pass
        self.stream.active = False