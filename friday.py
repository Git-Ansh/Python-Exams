import os
try:
    import pyttsx3
    import datetime
    import speech_recognition as sr
    import wikipedia
    import webbrowser
    import sys
    import smtplib
    import random
    import pyjokes
    import requests,json
    import spotipy as sp
    from spotipy import Spotify
    from spotipy.oauth2 import SpotifyOAuth
    import mysql.connector as m
    from time import strftime
    from playsound import playsound
    #import win32gui, win32con
except:
    os.system('cmd /k "pip install pyttsx3"')
    os.system('cmd /k "pip install speech_recognition"')
    os.system('cmd /k "pip install wikipedia"')
    os.system('cmd /k "pip install smtplib"')
    os.system('cmd /k "pip install webbrowser"')
    os.system('cmd /k "pip install requests"')
    os.system('cmd /k "pip install json"')
    os.system('cmd /k "pip install spotipy"')
    os.system('cmd /k "pip install mysql-connector-python"')
    os.system('cmd /k "pip install playsound"')
finally:
    api_key = "328594b42f178c9e880f40f9c21c1ad2"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + "Ahmedabad"
    db=m.connect(host="localhost", user="root",passwd="Anshshah2003")
    c=db.cursor(buffered=True)
    c.execute("create database if not exists jarvis")
    c.execute("use jarvis")
    c.execute("create table if not exists reminder(rem_id int not null auto_increment primary key, rem_name varchar(1000), rem_date date)")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    #print(voices[1].id)
    engine.setProperty('voice', voices[1].id)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning Boss!")
        elif hour>=12 and hour<12:
            speak("Good Afternoon Boss!")
        else:
            speak("Good Evening Boss!")
        speak("I am Friday , tell me how may I help you")

    wake='hello friday'
    wishMe()
    if __name__=="__main__":
        def takeCommand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 0.5
                audio = r.listen(source)
            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")
            except Exception as e:
                print("Say that again please...")
                return "None"
            return query

        def speak(audio):
            engine.say(audio)
            engine.runAndWait()
        while True:
            query = takeCommand().lower()
            if query.count(wake) > 0:
                speak('yes boss')
                query = takeCommand()
                try:
        #=========== WIKIPEDIA =========================================
                    if "wikipedia" in query:
                        speak('Searching Wikipedia...')
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=1)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)
                    elif "by Friday" in query:
                        speak('my pleasure sir. bye. have a great day')
                        exit()
                        break
                    elif 'tell me about' in query:
                         speak('Searching Wikipedia...')
                         query = query.replace("tell me about", "")
                         results = wikipedia.summary(query, sentences=2)
                         speak("According to Wikipedia")
                         print(results)
                         speak(results)
                    elif 'what is a' in query:
                         speak('Searching Wikipedia...')
                         query = query.replace("what is a", "")
                         results = wikipedia.summary(query, sentences=2)
                         speak("According to Wikipedia")
                         print(results)
                         speak(results)
                    elif 'what is an' in query:
                         speak('Searching Wikipedia...')
                         query = query.replace("what is an", "")
                         results = wikipedia.summary(query, sentences=2)
                         speak("According to Wikipedia")
                         print(results)
                         speak(results)
        #=========== HELLO how are you =================================
                    elif 'hello how are you' in query:
                        speak('i am fine sir, how are you? what can i help')
        #=========== Amazon music ==================================
                    elif 'open amazon music'in query:
                        os.startfile("C:\\Users\\dh1011tu\\OneDrive\\Desktop\\Amazon Music")
                    elif "close amazon music" in query:
                        os.system('taskkill /IM "AmazonMusic.exe" /F')
        #============= WHATSAPP ===============================
                    elif 'open WhatsApp'in query:
                        os.startfile("C:\\Users\\dh1011tu\\OneDrive\\Desktop\\Whatsapp Desktop")
                    elif "close WhatsApp" in query:
                        os.system('START /wait taskkill /f /im WhatsApp.exe')
        #=========== CHROME =================================
                    elif 'open Chrome'in query:
                        os.startfile('chrome.exe')
                    elif "close Chrome" in query:
                        try:
                            os.system('START /wait taskkill /f /im chrome.exe')
                        except EnvironmentError as e:
                            speak("Chrome is not currently open, sir")
                            print("Chrome is not currently open, sir")
                            pass
                    '''elif "minimise Chrome" in query:
                        hide = win32gui.GetForegroundWindow()
                        win32gui.ShowWindow(hide, win32con.SW_HIDE)'''
            #=========== YOUTUBE =================================
                    if 'open YouTube' in query:
                        webbrowser.open("https://www.youtube.com/")
                    elif "close YouTube" in query:
                        os.system('START /wait taskkill /f /im chrome.exe')
        #=========== GOOGLE =================================
                    elif 'open Google' in query:
                        webbrowser.open("https://www.google.com/")

                    elif "close Google" in query:
                        os.system('START /wait taskkill /f /im chrome.exe')

        #=========== INSTAGRAM =================================
                    elif 'open Instagram' in query:
                        webbrowser.open("instagram.com")

                    elif "close Instagram" in query:
                        os.system('START /wait taskkill /f /im chrome.exe')
        #=========== TIME =================================
                    elif 'what is the time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak("Sir, the time is "+strTime)
                    elif "search Google for" in query:
                        #speak("what should I search?")
                        tbs = query.replace("search Google for ","")
                        webbrowser.open("https://www.google.com/search?q="+tbs)

                    elif "close Google" in query:
                        os.system('START /wait taskkill /f /im chrome.exe')

                    elif "search the web for" in query:
                        bs=query.replace("search the web for","")
                        webbrowser.open("https://www.google.com/search?q=" + bs)

                    elif "search the internet for" in query:
                        bs=query.replace("search the internet for","")
                        webbrowser.open("https://www.google.com/search?q=" + bs)
                    elif "look up" in query:
                        bs=query.replace("look up ","")
                        webbrowser.open("https://www.google.com/search?q=" + bs)
                    # =========== reminder =====================================
                    elif "set a reminder" in query:
                        speak("what is the reminder?")
                        remind = takeCommand()
                        print(remind)
                        '''c.execute("select rem_id from reminder")
                        l = []
                        for i in c:
                            l.append(i)
                        o = (l[-1])
                        re = int(''.join(map(str, o)))
                        res = re + 1
                        rel = str(res)'''
                        c.execute("insert into reminder(rem_name,rem_date) values('" + remind + "',now())")
                        db.commit()

                    elif "show my reminders" in query:
                        li = []
                        lis = []
                        c.execute("select rem_date from reminder")
                        for i in c:
                            lis.append(i)
                        c.execute("select rem_name from reminder")
                        for j in c:
                            li.append(j)
                        for x, y in zip(li, lis):
                            print(*x)
                            speak(str(x))
                            speak(" For date")
                            tm = y[0]
                            p = tm.strftime('%d-%b-%Y')
                            print(p)
                            speak(p)

                    # =========== SHUT DOWN =================================
                    elif 'shutdown computer' in query:
                        speak("are you sure, you want to shutdown?")
                        cmd = takeCommand()
                        if cmd == 'yes':
                            os.system("shutdown /s /t 12")
                            speak("okay, your system will shut down in 10 seconds")
                        else:
                            speak("okay, shutdown cancelled")
                            pass
                    # =========== RESTART =================================
                    elif 'restart computer' in query:
                        speak("are you sure, you want to restart?")
                        cmd = takeCommand()
                        if cmd == 'yes':
                            os.system("shutdown /r /t 12")
                            speak("okay, your system will restart in 10 seconds")
                        else:
                            speak("okay, restart cancelled")
                            pass
        #=========== EMAIL =================================

        #=========== GMAIL =================================
                    if 'open Gmail' in query:
                        webbrowser.open("gmail.com")
                    elif "close Gmail" in query:
                        os.system('START /wait taskkill /f /im chrome.exe')
                        os.system('START /wait taskkill /f /im msedge.exe')

        #=========== JOKE =================================
                    elif 'tell me a joke' in query:
                        speak('sure, here is one')
                        result=pyjokes.get_joke()
                        print(result)
                        speak(result)
                    elif 'open music' in query:
                        os.startfile('Spotify.exe')
                    elif 'close spotify' in query:
                        try:
                            os.system('taskkill /IM "Spotify.exe" /F')
                        except :
                            print("Spotify is not open, sir")
        #=========== WEATHER =================================
                    elif 'what is the weather' in query:
                        response = requests.get(complete_url)
                        x = response.json()
                        if x["cod"] != "404":
                            y = x["main"]
                            current_temperature = round(y["temp"]-273.00, 2)
                            current_pressure = y["pressure"]
                            current_humidiy =y["humidity"]
                            z = x["weather"]
                            weather_description = z[0]["description"]
                            print("The Temperature is " +
                                            str(current_temperature) + "Degree Celsius" +
                                  "\n atmospheric pressure is " +
                                            str(current_pressure) + "bar"
                                  "\n humidity is " +
                                            str(current_humidiy) + "Percentage" +
                                  "\n description " +
                                            str(weather_description))
                            speak("The Temperature is " +
                                            str(current_temperature) + "Degree Celsius" +
                                  "\n atmospheric pressure is " +
                                            str(current_pressure) + "bar"
                                  "\n humidity is " +
                                            str(current_humidiy) + "Percentage" +
                                  "\n description " +
                                            str(weather_description))
        #=======================Spotify========================================================================================================
                    elif 'open spotify' in query or 'play a song' in query:
                        os.startfile("Spotify.exe")
                        def spotify():
                            class InvalidSearchError(Exception):
                                pass
                            def get_album_uri(spotify: Spotify, name: str) -> str:
                                original = name
                                name = name.replace(' ', '+')
                                results = spotify.search(q=name, limit=1, type='album')
                                if not results['albums']['items']:
                                    raise InvalidSearchError(f'No album named "{original}"')
                                album_uri = results['albums']['items'][0]['uri']
                                return album_uri
                            def get_artist_uri(spotify: Spotify, name: str) -> str:
                                original = name
                                name = name.replace(' ', '+')
                                results = spotify.search(q=name, limit=1, type='artist')
                                if not results['artists']['items']:
                                    raise InvalidSearchError(f'No artist named "{original}"')
                                artist_uri = results['artists']['items'][0]['uri']
                                print(results['artists']['items'][0]['name'])
                                return artist_uri
                            def get_track_uri(spotify: Spotify, name: str) -> str:
                                original = name
                                name = name.replace(' ', '+')
                                results = spotify.search(q=name, limit=1, type='track')
                                if not results['tracks']['items']:
                                    raise InvalidSearchError(f'No track named "{original}"')
                                track_uri = results['tracks']['items'][0]['uri']
                                return track_uri
                            def play_album(spotify=None, device_id=None, uri=None):
                                spotify.start_playback(device_id=device_id, context_uri=uri)
                            def play_artist(spotify=None, device_id=None, uri=None):
                                spotify.start_playback(device_id=device_id, context_uri=uri)
                            def play_track(spotify=None, device_id=None, uri=None):
                                spotify.start_playback(device_id=device_id, uris=[uri])
                            def pause_track(spotify=None, device_id=None, uri=None):
                                spotify.pause_playback(device_id=device_id, uris=[uri])
                            # -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
                            client_id = 'b7559059c68a4ef69171e0b6c76c43fb'
                            client_secret = '85a7350fb96b4c4481c31b86cfa9e2d8'
                            device_name = "HP"
                            redirect_uri = 'https://example.com/callback'
                            username = 'fd4hycy4x9sahsya5cr52xnuk'
                            scope = 'user-read-private user-read-playback-state user-modify-playback-state'
                            auth_manager = SpotifyOAuth(
                                client_id=client_id,
                                client_secret=client_secret,
                                redirect_uri=redirect_uri,
                                scope=scope,
                                username=username)
                            spotify = sp.Spotify(auth_manager=auth_manager)
                            devices = spotify.devices()
                            deviceID = 'c3f044814f2eba6c083670556ea58d33f4f3d204'
                            d1={'is_active':True}
                            for d in devices['devices']:
                                devices.update(d1)
                                d['name'] = d['name'].replace('’', '\'')
                                if d['name'] == device_name:
                                    deviceID = d['id']
                                    break
                            # -x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x
                            engine.setProperty('rate', 150)
                            def takeCommand():
                                r = sr.Recognizer()
                                with sr.Microphone() as source:
                                    print("Listening...")
                                    r.pause_threshold = 1.5
                                    audio = r.listen(source)
                                try:
                                    print("Recognizing...")
                                    query = r.recognize_google(audio, language='en-in')
                                    print(f"User said: {query}\n")
                                except Exception as e:
                                    print("Say that again please...")
                                    return "None"
                                return query
                            def speak(audio):
                                engine.say(audio)
                                engine.runAndWait()
                            speak("i have opened spotify for you, what song would you like me to play")
                            print("i have opened spotify for you, what song would you like me to play")
                            while True:
                                query = takeCommand()
                                print(query)
                                words = query.split()
                                if len(words) <= 1:
                                    print('Could not understand. Try again')
                                    continue
                                name = ' '.join(words[0:])
                                try:
                                    if 'kill' in words:
                                        os.system('taskkill /IM "Spotify.exe" /F')
                                        speak("ok sir, i have closed spotify")
                                        print("ok sir, i have closed spotify")
                                        break
                                    uri = get_track_uri(spotify=spotify, name=name)
                                    play_track(spotify=spotify, device_id=deviceID, uri=uri)
                                except InvalidSearchError:
                                    print('InvalidSearchError. Try Again')
                                    continue
                        spotify()
                    elif 'send email' in query:
                            def takeCommand2():
                                r = sr.Recognizer()
                                with sr.Microphone() as source:
                                    print("Listening...")
                                    r.pause_threshold = 1
                                    audio = r.listen(source)
                                print("Recognizing...")
                                query = r.recognize_google(audio, language='en-in')
                                print(f"User said: {query}\n")
                                return query
                            emails = {'dad': 'mitts72@gmail', 'Jayam': 'jjp1735@gmail.com', 'jasnoor': 'salujajasnoor1603@gmail.com'}
                            speak('send to whom?')
                            email = takeCommand2()
                            while email == '':
                                email = takeCommand2()
                            email_id = ''
                            for i in emails:
                                if i == email:
                                    email_id = emails[i]
                            speak("What should I write?")
                            content = ''
                            while content == '':
                                content = takeCommand2()
                            print(content)
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.ehlo()
                            server.starttls()
                            server.login("anshjarvis2003@gmail.com", "orrcvnvzfgxpybkh")
                            server.sendmail('&&&&&&&&&&&', email_id, content)
                            server.close()
                            speak('Email has been sent succesfully!')
                except:
                        print("couldn't complete that request try again")
            elif "bye" in query:
                speak("bye sir, have a nice day")
                sys.exit()
    '''elif "search" or "web search" or "internet search" in query:
                    speak("what should I search the web for?")
                    bs = takeCommand()
                    if "stop the search" in bs:
                        speak("Okay sir, i have terminated the search")
                        print("Okay sir, i have terminated the search")
                        pass
                    else:
                        webbrowser.open("https://www.google.com/search?q=" + bs)'''