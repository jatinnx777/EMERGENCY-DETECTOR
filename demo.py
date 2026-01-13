"""Simple demo script for presentations.

Runs in two modes:
- live: attempts to use real `KeywordDetector` with a VOSK model (needs MODEL_PATH in config)
- mock: simulates detections without microphone or model (default)

Usage:
    python demo.py --mode mock
    python demo.py --mode live
"""
import time
import argparse
import json

from src.detector import KeywordDetector


def run_mock_demo():
    detector = KeywordDetector(model_path=None)

    # Replace recognizer with a simple mock object
    class MockRec:
        def __init__(self):
            self.calls = 0

        def AcceptWaveform(self, data):
            self.calls += 1
            return True

        def Result(self):
            # Cycle through a few simulated texts
            texts = [
                '{"text": "hello"}',
                '{"text": "help"}',
                '{"text": ""}',
                '{"text": "save me"}',
                '{"text": "help me"}',
            ]
            return texts[(self.calls - 1) % len(texts)]

        def PartialResult(self):
            return '{"partial": ""}'

    detector.recognizer = MockRec()

    print("Starting mock demo — simulated phrases will be checked for keywords.")
    for i in range(8):
        # Simulate audio bytes (detector only inspects recognizer output in mock)
        detected = detector.process_audio(b"fake")
        if detected:
            print(f"DETECTED: {detected}")
        else:
            print("No keyword")
        time.sleep(1)


def run_live_demo():
    try:
        from config import MODEL_PATH
    except Exception:
        print("Please set MODEL_PATH in config.py for live demo.")
        return

    detector = KeywordDetector(model_path=MODEL_PATH)
    print("Live demo not fully implemented: this will require microphone and model.")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["mock", "live"], default="mock")
    args = p.parse_args()

    if args.mode == "mock":
        run_mock_demo()
    else:
        run_live_demo()
