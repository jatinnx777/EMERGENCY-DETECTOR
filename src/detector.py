import json
import time
from vosk import Model, KaldiRecognizer

class KeywordDetector:
    def __init__(self, model_path, keywords=None, debounce_s=1.5):
        if keywords is None:
            keywords = ["help", "bachao", "save me", "help me"]
        self.model = Model(model_path)
        self.rec = KaldiRecognizer(self.model, 16000)
        self.rec.SetWords(False)
        self.keywords = [kw.lower() for kw in keywords]
        self.last_detect = 0.0
        self.debounce_s = debounce_s

    def process_audio(self, data):
        if self.rec.AcceptWaveform(data):
            r = json.loads(self.rec.Result())
            text = r.get("text", "").lower()
            return self.check_keywords(text)
        else:
            partial = json.loads(self.rec.PartialResult()).get("partial", "").lower()
            return self.check_keywords(partial)

    def check_keywords(self, text):
        if not text:
            return None
        for kw in self.keywords:
            if kw in text:
                now = time.time()
                if now - self.last_detect > self.debounce_s:
                    self.last_detect = now
                    return kw
        return None