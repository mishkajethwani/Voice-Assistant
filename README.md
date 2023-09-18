Voice Assistant
Overview
This is a simple voice assistant programmed in Python. It can listen to voice commands, process them, and respond with audio feedback. The assistant can interact with your Google Calendar to provide information about your upcoming events.

Features
Speech Recognition: The assistant uses the speech_recognition library to convert spoken words into text.
Voice Commands: Recognizes predefined voice commands to perform specific actions.
Google Calendar Integration: Can check and inform you about your upcoming events.
Prerequisites
Before using the voice assistant, make sure you have the following dependencies installed:

Python 3.x
Required Python libraries (pip install -r requirements.txt):
speech_recognition
playsound
pyttsx3
gTTS (Google Text-to-Speech)
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
pytz
Getting Started
Set up Google Calendar API:

Follow the instructions to create a project and enable the Google Calendar API in the Google Calendar API Python Quickstart guide.
Download the JSON credentials file and save it as credentials.json in the same directory as your code.
Run the Assistant:

Execute the main.py file using Python 3.x.
Wake Word:

Use the specified wake word (e.g., "hemesh," "hey mesh," etc.) to activate the assistant.
Voice Commands:

Issue voice commands like "What do I have on Wednesday?" to interact with the assistant.
Usage Examples
Wake Word: Say the wake word to activate the assistant.
Calendar Queries: Ask questions like "Do I have plans today?" or "Am I busy tomorrow?" to get information about your calendar events.
Limitations
This is a basic voice assistant and does not employ advanced Natural Language Processing (NLP) techniques for understanding complex queries.
It recognizes a predefined set of voice commands and may not handle all possible variations.
Future Improvements
Implement more advanced NLP to enhance natural language understanding.
Add support for additional voice commands and features.
Improve error handling and user feedback.
License
This project is licensed under the MIT License - see the LICENSE file for details.
