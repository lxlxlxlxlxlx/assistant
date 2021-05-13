import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calender
import random
import wikipedia

warnings.filterwarnings('ignore')

def recordAudio():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)

    # use google speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('you said: '+data)
    except sr.UnknownValueError:
        print('Google could not recognize the audio.')
    except sr.RequestError as e:
        print('Request results from google error: '+e)
    return data

recordAudio()