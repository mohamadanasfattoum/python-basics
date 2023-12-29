import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from bs4 import BeautifulSoup

recognizer = sr.Recognizer()

engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("Recognized Text:", text)
        process_command(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error:", str(e))

def process_command(command):
    if "search" in command:
        query = command.replace("search", "")
        query = query.strip()
        if query:
            search(query)
        else:
            response = "Please provide a search query."
            speak(response)
    elif "weather" in command:
        response = "The weather today is sunny."
        speak(response)
    elif "reminder" in command:
        response = "Reminder set successfully."
        speak(response)
    else:
        response = "Sorry, I didn't understand that command."
        speak(response)

def search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    answer_element = soup.find("div", class_="Z0LcW")
    if answer_element:
        answer = answer_element.get_text()
        speak(answer)
    else:
        response = "I'm sorry, I couldn't find a specific answer to your query."
        speak(response)

def speak(response):
    print("Assistant:", response)
    engine.say(response)
    engine.runAndWait()

# Main loop
while True:
    listen()