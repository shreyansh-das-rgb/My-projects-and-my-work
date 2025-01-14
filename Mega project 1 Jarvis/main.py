import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibray
import requests
import google.generativeai as genai
from gtts import gTTS
import pygame
import os


engine = pyttsx3.init()
newsapi = "ab2f38fe4b5a4585b17a7a290f9e6913"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

# Initialize pygame mixer
    pygame.mixer.init()

    # Load the music file
    pygame.mixer.music.load("temp.mp3")  

    # Play the music
    pygame.mixer.music.play() 

    # Game loop (optional)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
       genai.configure(api_key="AIzaSyCKG6YFc23MhplPbSdcVuxrCrxPVjhT1zQ")
       model = genai.GenerativeModel("gemini-1.5-flash")
       # Create a generation configuration to limit output tokens
       generation_config = genai.GenerationConfig(
        max_output_tokens=50  # Limit output to 50 tokens
    )

       response = model.generate_content(f"{command} (answer in 50 words)")
       print(response.text)
       speak(response.text)


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibray.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}.")
    elif "news" in c.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            r.raise_for_status()
            data = r.json()
            articles = data.get("articles", [])
            if articles:
                speak("Here are the top headlines.")
                for index, article in enumerate(articles[:5], start=1):
                    print(f"{index}. {article.get('title')}")
                    speak(article.get('title'))
            else:
                speak("No news articles found.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")
            speak("Sorry, I couldn't fetch the news.")
    elif "who created you" or "who is your creator" in c.lower():
        speak("One and only Shreyansh Das, my creator, has created me.")
        print("One and only Shreyansh Das, my creator, has created me.")
    else:
        # Delegate to AI for unrecognized commands
        aiProcess(c)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
    # Listen for the wake word "Jarvis"
    # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using Sphinx
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listentin...")
                audio = r.listen(source,timeout=5,phrase_time_limit=2)
                word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))