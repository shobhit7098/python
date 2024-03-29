import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import sys
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Aviraj Sir")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!Aviraj Sir")
    else:
        speak("Good Evening! Aviraj Sir")
    speak("I am Miss Lopase Sir.Please tell me How may I help you")

def takeCommand():
      '''



      '''
      r =sr.Recognizer()
      with sr.Microphone() as source:
          print("listing...")
          r.pause_threshold = 1.0
          auido = r.listen(source,0,9)
      try:
           print("Recognizing/")
           query = r.recognize_google(auido, language= 'en-in')
           print(f"User said :{query}\n")
      except  Exception as e:
         print("Say that again please....")
         return " None"
      query =str(query)
      return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('avirajbharadwaj561@gmail.com', 'Aviraj@143')
    server.sendmail('avirajbharadwaj561@gmail.com',to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True: 
         
        query = takeCommand().lower()
        if 'Wikipedia' in query:
             speak('Searching Wikipedia...')
             query= query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences=1)
             speak("According to Wikipedia")
             speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
        elif 'open instagram.com' in query:
            webbrowser.open("instagram.com")
        elif 'open google' in query:
           webbrowser.open("google.com")
       # elif 'open whatsapp' in query:
            
        elif 'play music' in query:
            music_dir= 'E:\\song\\02 NEW  SONG'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open vscode ' in query:
            codepath = "a\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'email to avi ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to ="avirajbharadwaj561@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry , Sir I can't send the email")

            