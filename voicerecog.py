import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import time
import os
import requests
import datetime
import pywhatkit
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


engine = pyttsx3.init()
engine.setProperty('rate', 150)





def set_volume(level):  # level: 0 to 100
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume_range = volume.GetVolumeRange()

    min_vol = volume_range[0]  # usually -65.25
    max_vol = volume_range[1]  # usually 0.0

    # Normalize level to range
    level = max(0, min(level, 100))
    new_volume = min_vol + (level / 100) * (max_vol - min_vol)
    volume.SetMasterVolumeLevel(new_volume, None)


def get_weather(city, api_key="b4c9f192fabc1e581596ab4ba3c755fe"):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    full_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(full_url)
    data = response.json()

    if data["cod"] != "404":
        weather_main = data["main"]
        temperature = weather_main["temp"]
        humidity = weather_main["humidity"]
        weather_desc = data["weather"][0]["description"]

        report = f"The weather in {city} is {weather_desc} with a temperature of {temperature}°C and humidity of {humidity}%."
        return report
    else:
        return "City not found. Please try again."


def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Didn't catch that. Please try again.")
        return ""  # Continue loop even if nothing was heard
    except sr.RequestError:
        print("Error connecting to the service.")
        return ""

def run_jarvis():
    speak("Hi , how can I help you today?")
    while True:
        command = take_command()

        if command == "":
            continue  # Skip empty commands

        if "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
        elif "hello" in command:
            speak("Hello! I'm your voice assistant.")
        elif "how are you" in command:
            speak("I'm doing great, thanks for asking!")
        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "play on youtube" in command:
            topic = command.replace("play on youtube", "").strip()
            speak(f"Playing {topic} on YouTube")
            pywhatkit.playonyt(topic)

        elif "open github" in command:
            speak("Opening GitHub")
            webbrowser.open("https://www.github.com")
        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}")
        elif "search" in command:
            search_term = command.replace("search", "").strip()
            speak(f"Searching for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad.exe")
        elif "open chrome" in command:
            speak("Opening Google Chrome")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif "play music" in command or "play song" in command:
            speak("Opening Spotify and playing music")

            os.system("start spotify:")

            time.sleep(5)

            pyautogui.press("space")

        elif "volume" in command:
            if "increase" in command:
                speak("Increasing volume")
                set_volume(90)
            elif "decrease" in command:
                speak("Decreasing volume")
                set_volume(30)
            elif "mute" in command:
                speak("Muting volume")
                set_volume(0)
            elif "full" in command:
                speak("Setting volume to maximum")
                set_volume(100)
        elif "weather" in command:
            speak("Which city's weather do you want to check?")
            city = take_command()
            speak("Checking weather for " + city)
            weather_report = get_weather(city)
            speak(weather_report)




        else:
            speak("Sorry, I didn't understand that. Try again.")




run_jarvis()
