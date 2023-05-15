import subprocess
import datetime
import os
import AppOpener
from time import strftime
from index import Assist
import openai
import smtplib
obj = Assist()
import speedtest

class Function:
    def time(self):
        string = strftime('%H:%M')
        now = datetime.datetime.now().time()
        if 12 > now.hour >= 6:

            print(string)
            obj.tell("its" + string)
        elif 17 > now.hour >= 12:
            obj.tell("Good afternoon")
            print(string)
            obj.tell("its" + string)
        elif 21 > now.hour >= 17:
            obj.tell("Good Evening")
            print("Good Evening")
            print(string)
            obj.tell("its" + string)
        elif 23 >= now.hour > 21:
            obj.tell("Good night")
            print(string)
            obj.tell("its" + string)
        else:
            obj.tell(string)

    def hdate(self):
        tdate = datetime.datetime.now()
        print(f'{tdate:%b %d %Y}')
        obj.tell(f'{tdate:%b %d %Y}')

    def shut(self):
        os.system("shutdown /s 0")


    def sleep(self):
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


    def lock(self):
        subprocess.run(["rundll32", 'user32.dll', 'LockWorkStation'])


    def restart(self):
        AppOpener.close("PyCharm Community Edition 2022.2.3")
        os.system("shutdown /r /t 0")

    def speedtest(self):
        st = speedtest.Speedtest()
        try:
            obj.tell(
                "internet speed test is in progrees, have some patience....")
            d = st.download()
            u = st.upload()
            kb = d / 1024
            kbu = u / 1024
            mb = kb / 1024
            mbu = kbu / 1024
            string_mb = str(mb)
            string_mbu = str(mbu)
            x = string_mb[0:4]
            y = string_mbu[0:4]
            print(
                f"your internet download speed is {x} mb/s and upload speed is {y} mb/s")
            obj.tell(
                f"your internet download speed is{x} m b per second and upload speed is {y} m b per second")

        except Exception as e:
            obj.tell(
                f"sorry sir, device is not connected to internet or there is an error{e}")

    def chatwithgpt(self):
        try:
            print('successfully connected to your AI prompt....')
            obj.tell('successfully connected to your AI prompt....')
            print('\nHey I am Rayan your AI prompt, tell me how can i help you?')
            obj.tell('Hey I am Rayan your AI prompt, tell me how can i help you?')

            openai.api_key = "API key"

            while True:
                model_engine = "text-davinci-003"

                prompt = input('Ask me anything: ')

                if 'exit' in prompt or 'quit' in prompt:
                    print('disconnecting from your AI prompt')
                    obj.tell('disconnecting from your AI prompt')
                    break

                completion = openai.Completion.create(
                    engine=model_engine,
                    prompt=prompt,
                    max_tokens=1024,
                    n=1,
                    stop=None,
                    temperature=0.5,
                )

                response = completion.choices[0].text

                print(response)
                if len(response) < 100:
                    obj.tell(response)


        except Exception as e:
            print(f'Can not connect to your AI right now due to {e}')
            obj.tell(f'Can not connect to your AI right now due to {e}')
    def email(self):
        obj.tell("Ok sir, I am ready to send email, just give me receivers email id")

        myemail = "g******5@gmail.com"
        password = '#### #### #### ####'
        receiver = input("Enter receivers email-id here=")
        s = smtplib.SMTP('smtp.gmail.com',587)
        try:
            s.starttls()
            s.login(myemail,password)
        except Exception as e:
            print(e)
            obj.tell(f"sorry sir, I can't send email, there is an {e} error")

        obj.tell('please type subject and message for the email=')
        sub = input("Write down subject here:")
        msg = input("write down msg here:")
        msg = "Subject:{}\n\n{}".format(sub, msg)
        s.sendmail(myemail, receiver, msg)
        chk = s.ehlo()
        if chk[0] == 250:
            obj.tell(f'email sent to {receiver} successfully')
        else:
            obj.tell(f'sorry sir, email not sent, please check receivers email id')



    def close(self):
        raise SystemExit
