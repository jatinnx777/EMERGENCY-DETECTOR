import unittest
from unittest.mock import patch, MagicMock
from src.detector import KeywordDetector

class TestKeywordDetector(unittest.TestCase):

    @patch('src.detector.Model')
    @patch('src.detector.Recognizer')
    def setUp(self, mock_recognizer, mock_model):
        self.detector = KeywordDetector()
        self.detector.recognizer = mock_recognizer
        self.detector.model = mock_model

    def test_keyword_detection(self):
        # Simulate audio input that contains a keyword
        mock_audio_data = b'some audio data containing help'
        self.detector.recognizer.AcceptWaveform.return_value = True
        self.detector.recognizer.Result.return_value = '{"text": "help"}'

        detected_keyword = self.detector.process_audio(mock_audio_data)
        self.assertEqual(detected_keyword, "help")

    def test_no_keyword_detection(self):
        # Simulate audio input that does not contain a keyword
        mock_audio_data = b'some audio data without keywords'
        self.detector.recognizer.AcceptWaveform.return_value = True
        self.detector.recognizer.Result.return_value = '{"text": ""}'

        detected_keyword = self.detector.process_audio(mock_audio_data)
        self.assertIsNone(detected_keyword)

    def test_debounce_functionality(self):
        self.detector.last_detected_time = 0
        self.detector.debounce_time = 1

        # Simulate detecting a keyword
        self.detector.detect_keyword("help", 0)
        self.assertTrue(self.detector.alert_triggered)

        # Simulate detecting the same keyword within debounce time
        self.detector.detect_keyword("help", 0.5)
        self.assertFalse(self.detector.alert_triggered)

        # Simulate detecting the same keyword after debounce time
        self.detector.detect_keyword("help", 1.5)
        self.assertTrue(self.detector.alert_triggered)

if __name__ == '__main__':
    unittest.main()