# Voice Assistant

## Overview

This is a simple voice assistant project built in Python. It can listen to voice commands, process them, and respond with audio feedback. The assistant is designed to interact with your Google Calendar, providing information about your upcoming events.

## Features

- **Speech Recognition**: Utilizes the `speech_recognition` library for converting spoken words into text.
- **Voice Commands**: Recognizes predefined voice commands to perform specific actions.
- **Google Calendar Integration**: Capable of checking and informing you about your upcoming events.

## Prerequisites

Before using the voice assistant, ensure you have the following dependencies installed:

- Python 3.x
- Required Python libraries (you can install them using `pip install -r requirements.txt`):
  - `speech_recognition`
  - `playsound`
  - `pyttsx3`
  - `gTTS` (Google Text-to-Speech)
  - `google-auth`
  - `google-auth-oauthlib`
  - `google-auth-httplib2`
  - `google-api-python-client`
  - `pytz`

## Getting Started

Follow these steps to set up and run the assistant:

1. **Set up Google Calendar API**:
   - Create a new project and enable the Google Calendar API by following the instructions in the [Google Calendar API Python Quickstart guide](https://developers.google.com/calendar/quickstart).
   - Download the JSON credentials file and save it as `credentials.json` in the same directory as your code.

2. **Run the Assistant**:
   - Execute the `main.py` file using Python 3.x.

3. **Wake Word**:
   - Use the specified wake word  to activate the assistant.

4. **Voice Commands**:
   - Issue voice commands like to interact with the assistant.

## Future Improvements


- Implement more advanced NLP to enhance natural language understanding.
- Add support for additional voice commands and features.
- Improve error handling and user feedback.



