import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import pyjokes
import subprocess
import webbrowser
import os.path
from os import path




def main():
    close = True

    # create an instance of a speech recognizer
    listner = sr.Recognizer()

    # create an instance of text to speech
    engine = pyttsx3.init()

    # get all voices in the engine
    voices = engine.getProperty("voices")

    # make the speed of speech slower
    newVoiceRate = 145
    engine.setProperty('rate', newVoiceRate)

    # choose the female voice
    engine.setProperty('voice', voices[0].id)

    # create an instance of microphone
    mic = sr.Microphone(device_index=1)

    def talk(text):
        # let engine to say somthing when the program once runs
        engine.say(text)
        engine.runAndWait()

    def say_something():
        with mic as source:
            listner.adjust_for_ambient_noise(source)
            print("listning ...")
            voice = listner.listen(source, phrase_time_limit=5)
            try:
                if voice is not None:
                    command = listner.recognize_google(voice)
                    command = command.lower()
                    if command is not None:

                        if 'alexa' in command:
                            command = command.replace('alexa', '')

                            print(command)
                            return command
                else:
                    command = "hi"
                    return command

            except:
                pass
        return " "

    def run_assistant():

        command = say_something()
        global close
        if "exit" in command:
            close = False

        elif "play" in command:
            command = command.replace('play', '')
            print(command)
            pywhatkit.playonyt(command)

        elif "shark tank" in command:
            pywhatkit.playonyt("Shark Tank US ")

        elif "jok" in command:
            jok = pyjokes.get_joke(language="en", category="all")
            print(jok)
            talk(jok)

        elif "time" in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(time)

        elif "who is" in command and "google" not in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)

        elif "what is" in command and "google" not in command:
            thing = command.replace('what is', '')
            info = wikipedia.summary(thing, 1)
            talk(info)
        elif "when" in command and "google" not in command:
            result = command.replace('when', '')
            info = wikipedia.summary(result, 1)
            talk(info)

        elif "tell" in command and "google" not in command:
            result = command.replace('tell', '')
            info = wikipedia.summary(result, 1)
            talk(info)

        ############## folders on the machine ############################################
        # elif "desktop" in command:
        #     command = command.replace('desktop','')
        #     os.startfile(r'C:\Users\black\Desktop')
        # to open folders in desktop
        elif "desktop" in command and "find" in command:
            command = command.replace('find', '')
            command = command.replace('desktop', '')

            command = f'\{command}'

            pathDir = r"C:\Users\black\Desktop" + command
            pathDir = pathDir.replace(' ', '')
            print(pathDir)
            if path.exists(pathDir):
                os.startfile(pathDir)
            else:
                talk("the folder name is not on the desktop")
                talk("try again")

        #
        # elif "downloads" in command:
        #  #   command = command.replace('desktop', '')
        #     folder = os.startfile(r'C:\Users\black\Downloads')

        # open files on downloads

        elif "downloads" in command and "find" in command:
            command = command.replace('downloads', '')
            command = command.replace('find', '')
            command = f'\{command}'

            pathDirD = r"C:\Users\black\Downloads" + command
            pathDirD = pathDirD.replace(' ', '')
            print(pathDirD)
            if path.exists(pathDirD):
                os.startfile(pathDirD)
            else:
                talk("the folder name is not on the downloads")
                talk("try again")


        elif "documents" in command:
            #  command = command.replace('documents', '')
            folder = os.startfile(r'C:\Users\black\documents')

        # elif "dotnet" in command or "dot net" in command or ".net" in command:
        #   #  command = command.replace('documents', '')
        #     folder = os.startfile(r'C:\Users\black\Desktop\un\.Net')
        #################################################################################

        ####################### shutdown/restart/sleep ###################################

        elif "shutdown" in command:
            #  command = command.replace('documents', '')
            os.system("shutdown /s /t 1")

        elif "restart" in command:
            os.system("shutdown /r /t 1")

        elif "sleep" in command:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        #####################################################################################

        ################## application on the machine #############################################

        elif "whatsapp" in command:
            os.system('start Whatsapp:')

        elif "word" in command or 'ward' in command:
            os.startfile(r'C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE')

        elif "calc" in command:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')

        elif "notepad" in command:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

        elif "sittings" in command or "sitting" in command:
            subprocess.Popen([r"C:\Windows\System32\DpiScaling.exe"])

        elif "vs code" in command or "vscode" in command:
            os.startfile(r'C:\Users\black\AppData\Local\Programs\Microsoft VS Code\Code.exe')

        elif "visual studio" in command:
            os.startfile(r'C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\devenv.exe')

        elif "pycharm" in command or "py charm" in command:
            os.startfile(r'C:\Program Files\JetBrains\PyCharm 2019.3.1\bin\pycharm64.exe')

        elif "rider" in command:
            os.startfile(r'C:\Program Files\JetBrains\JetBrains Rider 2020.2\bin\rider64.exe')

        elif "android" in command:
            os.startfile(r'C:\Program Files\Android\Android Studio\bin\studio64.exe')

        elif "chrome" in command:
            os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

        elif "edge" in command:
            os.startfile(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')

        elif "git" in command or "get" in command:
            os.startfile(r'C:\Program Files\Git\git-bash.exe')
        ##################################################################################

        ################ websites ###############################################
        elif "translator" in command:
            webbrowser.open('https://translate.google.com/?sl=no&tl=en&op=translate')

        elif "google" in command:
            command = command.replace('google', '')
            command = f'search?q={command}'
            webbrowser.open(f'https://www.google.no/{command}')

        elif "chatgpt" in command or "chat gpt" in command:
            webbrowser.open('https://openai.com/blog/chatgpt')

        elif "github" in command:
            webbrowser.open('https://github.com/')

        elif "udi" in command:
            webbrowser.open('https://www.udi.no/')

        elif "dnb" in command:
            webbrowser.open('https://www.dnb.no/forside-pluss')



        ###############################################################################

        else:
            talk(command)

    while close is True:
        run_assistant()



if __name__ == "__main__":
    main()