from __future__ import print_function
import datetime
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pytz
import pyttsx3
import subprocess


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
number_end=["st","nd","rd","th"]


def say(text, voice="en"):
    tts = gTTS(text=text, lang=voice)
    filename = "speech.mp3"
    tts.save(filename)
    playsound.playsound(filename)

'''def say(text, voice="Victoria"):
    try:
        subprocess.run(["osascript", "-e", f'say "{text}" using "{voice}"'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    eng=pyttsx3.init()
    eng.say(text)
    eng.runAndWait()
    tts=gTTS(text=text,lang="en")
    filename="speech.mp3"
    tts.save(filename)
    playsound.playsound(filename) '''

def user_audio_to_text():
    rz =sr.Recognizer()
    with sr.Microphone() as source:
        audio = rz.listen(source)
        user_input = ""

        try:
            user_input = rz.recognize_google(audio)
            print(user_input)
        except Exception as e:
            print("Exception: "+ str(e) )

    return user_input


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        return service
    except HttpError as error:
        print('An error occurred: %s' % error)

def get_events(day,service):
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc=pytz.UTC
    date=date.astimezone(utc)
    end_date=end_date.astimezone(utc)
    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(),timeMax=end_date.isoformat(),
                                            singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
      say('No upcoming events found.')
    else:
        say(f"you have {len(events)} events on this day")

    # Prints the start and name of the next 10 events
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        if start.find('T')>0:
            start_time=str(start.split("T")[1].split("+")[0])
            if int(start_time.split(":")[0]) <12:
                start_time=start_time+"a m"
            else:
                start_time=str(int(start_time.split(":")[0]) - 12)+ start_time.split(":")[1]
                start_time=start_time+"p m"
        else:
            start_time=start

        say(event["summary"]+"at"+start_time)

def get_date(text):
    text=text.lower()
    today=datetime.date.today()

    if "today" in text:
        return today

    day= -1
    theday = -1
    month=-1
    year=today.year

    for word in text.split():
        if word in months:
            month=months.index(word)+1
        elif word in days_of_week:
            day=days_of_week.index(word)
        elif word.isdigit():
            theday = int(word)
        else:
            for ext in number_end:
                try:
                    if word.endswith(ext):
                        theday = int(word[:-len(ext)])
                except:
                    pass


    if month < today.month and month != -1:
        year+=1

    if theday < today.day and month == -1 and day != -1:
        month +1
    if month == -1 and theday == -1 and day != -1:
        current_day= today.weekday()
        dif = day - current_day

        if dif<0:
            dif = dif+7
            if text.count("next")>=1:
                dif = dif +7

        return today+datetime.timedelta(dif)

    if month==-1 or theday ==-1:
            return None

    final = datetime.date(month=month, day=theday, year=year)

    return final

wake_word="hemesh" or "hey mesh" or "hey mish" or "himish" or "hi mish" or "hey tim"
serv=main()
print("start")
while True:
    print("listening")
    text=user_audio_to_text()

    if text.count(wake_word)>0:
        say("how can i help you")
        text= user_audio_to_text()

        date_events=["what do i have","do i have plans","am i busy","do i have anything"]
        for phrase in date_events:
            if phrase in text.lower():
                date=get_date(text)
                print(date)
                if date:
                    get_events(date,serv)
                else:
                    say("I am sorry can you please try again")







if __name__ == '__main__':
    main()




