import speech_recognition as sr
import pyttsx3
import datetime as dt
import pywhatkit as pk
import wikipedia as wiki
#   *********************  My Virtual Assisstant == CHITTI  ***********************

listener = sr.Recognizer()

speaker = pyttsx3.init()

""" RATE"""
rate = speaker.getProperty('rate')   # getting details of current speaking rate
speaker.setProperty('rate', 150)     # setting up new voice rate

"""VOICE"""
voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

va_name='chitti'

speak('I am your,' + va_name + ',  Tell me boss?.')

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('Listening boss....!')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if va_name in command:
                command = command.replace(va_name + ' ', '')
               # print(command)
               # speak(command)



    except:
        print('Check your Mic')
        speak('I cant get you boss. ')
    return command
while True:
    user_command = take_command()
    if 'close' in user_command or 'shut' in user_command:
        speak('yes boss . see you again , bye. ')
        print('yes boss . see you again , bye . ')
        break
    elif 'time' in user_command:
        cur_time = dt.datetime.now().strftime("%I:%M %p")
        print(cur_time + ' boss')
        speak(cur_time +' boss')
    elif 'play' in user_command:
        user_command = user_command.replace('play ', '')
        print('yes boss,Playing ' + user_command + '. enjoy .')
        speak('yes boss,Playing ' + user_command + '. enjoy .')
        pk.playonyt((user_command))
        break
    elif 'search' in user_command or 'google' in user_command:
        user_command = user_command.replace('search', '')
        user_command = user_command.replace('google', '')
        speak('yes boss, searching for ' + user_command)
        pk.search(user_command)
    elif 'who is' in user_command:
        user_command = user_command.replace('who is', '')
        info = wiki.summary(user_command, 1)
        print(info)
        speak('boss  .  ' + info)
    elif 'who are you' in user_command:
        print('I am your virtual assisstant,' + va_name + ',  Tell me boss.')
        speak('I am your virtual assisstant,' + va_name + ',  Tell me boss.')
    elif 'hello' in user_command:
        print('hai lucky, welcome back , lets rock buddy')
        speak('hai lucky, welcome back !, lets rock buddy!!')
    elif 'whatsapp' in user_command:
        print('nothing much lucky. you have to say anything....')
        speak('nothing much lucky. you have to say anything....')
        print('so...hows your day? Is it good?')
        speak('so...hows your day? Is it good?')
    elif 'good' in user_command:
        print('Wow!!.. what have you done to make your day good??')
        speak('Wow!!.. what have you done to make your day good??')
        print('you can share with me bro')
        speak('you can share with me  broh!!!')

    else:
        speak('Please say it again boss.')


