# Vosk Emergency Detector

## Overview
The Vosk Emergency Detector is an AI voice keyword detection system that continuously listens to microphone audio and triggers alerts when specific emergency keywords are detected. This project utilizes the Vosk speech recognition toolkit to identify keywords such as "help", "bachao", "help me", and "save me".

## Features
- Continuous audio input monitoring
- Real-time keyword detection
- Alert system for emergency keywords
- Configurable settings for model path and alert sounds

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/vosk-emergency-detector.git
   cd vosk-emergency-detector
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your microphone is set up and working.
2. Run the main application:
   ```
   python src/main.py
   ```

3. The application will start listening for keywords. When a keyword is detected, an alert will be triggered.

## Keywords
The following emergency keywords are recognized by the system:
- help
- bachao
- help me
- save me

## Configuration
You can modify the configuration settings in `src/config.py` to change the Vosk model path and alert sound file location.

## Testing
To run the tests, use the following command:
```
pytest
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.