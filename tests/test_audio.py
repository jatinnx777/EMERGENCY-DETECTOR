import unittest
from unittest.mock import patch, MagicMock
import sounddevice as sd
import numpy as np
from src.audio import AudioHandler

class TestAudioHandler(unittest.TestCase):

    @patch('sounddevice.InputStream')
    def test_audio_capture(self, mock_input_stream):
        mock_input_stream.return_value.read.return_value = (np.zeros((1024, 1)), 0)
        audio_handler = AudioHandler()
        audio_data = audio_handler.capture_audio()
        self.assertEqual(audio_data.shape, (1024, 1))

    @patch('sounddevice.InputStream')
    def test_audio_stream_start(self, mock_input_stream):
        audio_handler = AudioHandler()
        audio_handler.start_stream()
        self.assertTrue(audio_handler.stream.active)

    @patch('sounddevice.InputStream')
    def test_audio_stream_stop(self, mock_input_stream):
        audio_handler = AudioHandler()
        audio_handler.start_stream()
        audio_handler.stop_stream()
        self.assertFalse(audio_handler.stream.active)

if __name__ == '__main__':
    unittest.main()