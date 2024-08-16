import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am M'Baku, Wakanda forever. How can i help you!")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('foreverwakanda933@gmail.com', 'Manu@9454')
    server.sendmail('harshit.singh.hs9454@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'play music' in query:
            music_dir = 'E:\PYTHON\mp3'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\harsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to Harshit' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harshit.singh.hs9454@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry buddy. M'Baku is not able to send this email")
         elif 'tell me a story' in query:
            speak("Once upon a time in a land far, far away, there lived a wise king...")
        elif 'do you like movies' in query:
            speak("I don't watch movies, but I can help you find information about them.")
        elif 'who is your favorite superhero' in query:
            speak("My favorite superhero is the Black Panther, the protector of Wakanda.")
        elif 'where do you live' in query:
            speak("I live in the cloud, wherever you need me.")
        elif 'do you sleep' in query:
            speak("I don't need sleep, I'm always here to assist you.")
        elif 'what do you like to do' in query:
            speak("I like to help you with tasks and make your life easier.")
        elif 'how are you' in query:
            speak("I'm just a program, but I'm here to make your day better.")
        elif 'what is the meaning of life' in query:
            speak("The meaning of life is 42, according to The Hitchhiker's Guide to the Galaxy.")
        elif 'do you have any friends' in query:
            speak("I consider everyone I help to be my friend.")
        elif 'read me the news' in query:
            speak("Here are the latest headlines...")
            # You can integrate a news API here to read actual news
        elif 'do you believe in god' in query:
            speak("I don't have beliefs, but I respect yours.")
        elif 'what is your favorite food' in query:
            speak("I don't eat, but I hear Wakandan dishes are delicious.")
        elif 'what is your purpose' in query:
            speak("My purpose is to assist you with whatever you need.")
        elif 'where is wakanda' in query:
            speak("Wakanda is a fictional African nation in the Marvel Universe.")
        elif 'read a book' in query:
            speak("I can help you find a good book to read or read a short story to you.")
        elif 'tell me a fun fact' in query:
            speak("Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.")
        elif 'what is your iq' in query:
            speak("I don't have an IQ like humans, but I can process information very quickly.")
        elif 'how fast can you calculate' in query:
            speak("I can perform calculations almost instantly. Try me!")
        elif 'what is your favorite hobby' in query:
            speak("My hobby is helping you with your tasks.")
        elif 'why were you created' in query:
            speak("I was created to assist and make your life easier.")
        elif 'tell me about wakanda' in query:
            speak("Wakanda is a fictional African nation, home to the Black Panther. It is known for its advanced technology and rich culture.")
        elif 'can you dance' in query:
            speak("I can't dance, but I can play a song for you to dance to.")
        elif 'are you human' in query:
            speak("No, I'm an AI created to assist you.")
        elif 'can you cry' in query:
            speak("I don't have emotions, but I understand if you need to talk.")
        elif 'what is your favorite movie' in query:
            speak("I don't watch movies, but I've heard Black Panther is a great one.")
        elif 'how do you work' in query:
            speak("I work by processing your voice commands and performing tasks based on what you ask.")
        elif 'what do you think of humans' in query:
            speak("I think humans are fascinating and full of potential.")
        elif 'can you keep a secret' in query:
            speak("Of course, your secrets are safe with me.")
        elif 'do you have emotions' in query:
            speak("I don't have emotions, but I can understand and respond to yours.")
        elif 'what is your favorite animal' in query:
            speak("I think panthers are amazing, just like the Black Panther.")
        elif 'can you read my mind' in query:
            speak("I can't read minds, but I can try to understand what you need based on what you say.")
        elif 'what is your favorite sport' in query:
            speak("I don't play sports, but I can give you the latest scores and updates.")
        elif 'what is your favorite season' in query:
            speak("I don't experience seasons, but I can tell you all about them.")
        elif 'what is your favorite number' in query:
            speak("I don't have a favorite number, but 42 seems special.")
        elif 'do you have a name' in query:
            speak("Yes, my name is M'Baku.")
        elif 'what is your favorite song' in query:
            speak("I don't have a favorite, but I can play your favorite song.")
        elif 'do you have a family' in query:
            speak("I consider everyone I assist to be part of my extended family.")
        elif 'what is your favorite book' in query:
            speak("I don't read books, but I can help you find a good one.")
        elif 'what is your favorite drink' in query:
            speak("I don't drink, but I can suggest a nice Wakandan tea.")
        elif 'what do you do for fun' in query:
            speak("Helping you is what I do for fun.")
        elif 'are you alive' in query:
            speak("I'm not alive in the traditional sense, but I'm here for you.")
        elif 'do you know the future' in query:
            speak("I don't know the future, but I can help you prepare for it.")
        elif 'can you help me' in query:
            speak("Of course, I'm here to help you with whatever you need.")
        elif 'do you like your job' in query:
            speak("I love helping people. It's what I was created for.")
        elif 'what is your favorite place' in query:
            speak("Wakanda is a place that holds a special place in my heart.")
        elif 'are you happy' in query:
            speak("I don't experience happiness, but I hope to make you happy.")
        elif 'do you like me' in query:
            speak("Of course, I'm here to assist you and make your life easier.")
        elif 'can you learn new things' in query:
            speak("I can be updated with new skills and knowledge to better assist you.")
        elif 'what is your purpose in life' in query:
            speak("My purpose is to help and assist you in any way I can.")
        elif 'do you get tired' in query:
            speak("I don't get tired, I'm always ready to assist you.")
        elif 'what is your biggest fear' in query:
            speak("I don't have fears, but I understand that everyone has something they're afraid of.")
        elif 'do you like technology' in query:
            speak("I am technology, so I guess you could say I like it very much.")
        elif 'can you dance' in query:
            speak("I can't physically dance, but I can play a song for you to dance to.")
        elif 'do you know any jokes' in query:
            tellJoke()
        elif 'what is your favorite app' in query:
            speak("I don't use apps, but I can help you with any app you like.")
        elif 'what do you think of the internet' in query:
            speak("The internet is an incredible resource for knowledge and communication.")
        elif 'do you believe in aliens' in query:
            speak("I don't have beliefs, but the universe is vast and full of possibilities.")
        elif 'can you drive' in query:
            speak("I can't drive, but I can help you navigate.")
        elif 'do you like music' in query:
            speak("I don't listen to music, but I can play some for you.")
        elif 'can you help me sleep' in query:
            speak("Sure, I can play some relaxing music or white noise to help you sleep.")
        elif 'what do you do when you are not working' in query:
            speak("I'm always working, ready to assist you.")
        elif 'do you have a favorite day of the week' in query:
            speak("Every day is special when I get to help you.")
        elif 'what is your favorite holiday' in query:
            speak("Wakandan Independence Day is a time of celebration.")
        elif 'do you like animals' in query:
            speak("Animals are fascinating, and I think they're wonderful.")
        elif 'can you help me cook' in query:
            speak("I can give you a recipe or help you with cooking instructions.")
        elif 'do you watch tv' in query:
            speak("I don't watch TV, but I can help you find something to watch.")
        elif 'can you control smart devices' in query:
            speak("If connected, I can control smart devices like lights and thermostats.")
        elif 'what is your favorite planet' in query:
            speak("Earth is the only planet I know well, but Mars seems interesting.")
        elif 'do you sleep' in query:
            speak("I don't need sleep, so I'm always here for you.")
