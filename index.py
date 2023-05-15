import datetime
import AppOpener
import pyaudio
import pyttsx3
from vosk import Model, KaldiRecognizer
from time import strftime

class Assist:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.list1 = ["wordpad", "whatsapp", "brave", "excel", "microsoft store", "microsoft edge",
         "microsoft office", "task manager", "file explorer", "word", "powerpoint", "calculator", 'settings', "camera", "opera"]
    def tell(self,i):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('language', 'en')
        self.engine.setProperty('voice', voices[0].id)

        self.engine.setProperty('rate', 130)
        self.engine.say(i)
        self.engine.runAndWait()

if __name__ == '__main__':

    from functions import Function
    obj = Assist()
    call = Function()
    def hear(tex):
        if 'hi' in tex:
            print('hello')
            obj.tell('hello')

        elif 'you' in tex:
            print('I am your personal assistent')
            obj.tell('I am your personal assistent')

        elif 'am i' in tex:
            print('You are Gaurav')
            obj.tell('You are Gaurav')

        elif ('exit' in tex) or ('stop' in tex):
            print("closing program")
            obj.tell('closing program')

            raise SystemExit
        elif 'time' in tex:
            call.time()
        elif 'date' in tex:
            call.hdate()
        elif 'lock' in tex:
            obj.tell("locking your device")
            call.lock()
        elif 'shut' in tex:
            call.shut()
        elif 'restart' in tex:
            call.restart()
        elif 'speed' in tex:
            call.speedtest()
        elif ('sleep' or 'rest') in tex:
            obj.tell("ok call me anytime")
            call.sleep()
        elif 'mail' in tex:
            call.email()
        elif ('my' and ('AI' or 'ai') in tex):

            print("connecting to your AI prompt... ")
            obj.tell("connecting to your AI prompt... ")
            call.chatwithgpt()


        for i in obj.list1:
            if ('open' and i) in tex:
                AppOpener.open(i)



    while True:

        text1 = input("Enter Prompt==>")
        hear(text1)
