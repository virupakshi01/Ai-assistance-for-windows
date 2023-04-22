import os
import time
import subprocess
import json
import wolframalpha
import requests
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3

name="viru"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",'voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()
    

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("hello, good morning "+ name)
        print("hello, good morning "+ name)
    elif hour >=12 and hour <=18:
        speak("hello, good afternoon "+ name)
        print("hello, good afternoon "+ name)
    else:
        speak("Its already the night time better go to sleep"+ name)
        print("Its already the night time better go to sleep"+ name)
        
  


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("i am LISTENING")
        audio = r.listen(source)
        
        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
            
        except Exception as e:
            speak("pardon me, please say that again")
            return "None"
        return statement  

speak("LOADING YOUR PERSONAL A.I ASSISTANT JARVIS")
wishMe()    



if __name__=='__main__':
    while True:
        speak("how can i help you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("Your personal AI assistant JARVIS in shutting down, Good bye ")
            print("Your personal AI assistant JARVIS in shutting down, Good bye ")
            break
            
        if 'wikipedia' in statement:
            speak("searching wikipedia....")
            statement = statement.replace("wikipedia"," ")
            results = wikipedia.summary(statement , sentences = 3)
            speak("According to wikipedia....")
            print(results)
            speak(results)
            
        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open for you")
            time.sleep(5)
            
        elif "open google" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google search is open for you")
            time.sleep(5)
            
        elif "open gmail" in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("your gmail is open for you")
            time.sleep(5)
            
        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url ="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid = "+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" the temperature in kelvin units is " + str(current_temperature) +"\n humidity in percentage is" + str(current_humidity) + "\n weather description" + str(weather_description))
                print(" the temperature in kelvin units is " + str(current_temperature) +"\n humidity in percentage is" + str(current_humidity) + "\n weather description" + str(weather_description))
            else:
                speak("city not found")
                print("city not found")
                    
        elif "time" in statement:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"the time is {strTime}")
                          
        elif "who are you" in statement or "what can you do" in statement:
                    speak('I am JARVIS version 1 point O your personal assistant.I am programmed to minor tasks like'
                          'opening youtube,google chrome, gmail and stack overflow,predict time,take a photo,search wikipedia,predict weather'
                          'in different cities,get top headline news from times of India and you can ask me computational or geographical questions too!')
                          
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                    speak("I WAS BUILT BY "+name)
                    print("I WAS BUILT BY "+name)
                          
        elif "open stackoverflow" in statement:
                    webbrowser.open_new_tab("https://stackoverflow.com/login")
                    time.sleep(5)
                          
        elif "news" in statement:
                    news = webbrowser.open_new_tab("https://timesofindia.Indiatimes.com/home/headlines")
                    speak("here are some headlines for you from times of India - happy reading")
                    time.sleep(7)
                          
        elif "search" in statement:
                    statement = statement.replace("search"," ")
                    webbrowser.open_new_tab("statement")
                    time.sleep(5)
                          
                          
        elif "ask" in statement:
                    speak("I can answer to computational and geographical questions too just try me !! what do you want to ask ")
                    question = takeCommand()
                    app_id = "R2K75H-7ELALHR35X"
                    client = wolframalpha.Client('R2K75H-7ELALHR35X')
                    res = client.query(question)
                    answer = next(res.results).text
                    speak(answer)
                    print(answer)
                          
        elif "log off" in statement or "sign out" in statement or "shut down" in statement:
                    speak("ok, Your PC will shut down in 10 seconds - make sure you have saved and exit from all applications")
                    subprocess.call(['shutdown',"/1"])
                          
                          
    time.sleep(3)
