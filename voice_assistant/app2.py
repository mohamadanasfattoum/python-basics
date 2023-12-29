import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
from bs4 import BeautifulSoup

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Zuhören...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio, language="de-DE")
        print("Erkannter Text:", text)
        process_command(text)
    except sr.UnknownValueError:
        print("Kann Audio nicht verstehen")
    except sr.RequestError as e:
        print("Fehler:", str(e))

def process_command(command):
    # Implement logic to handle different commands
    if "suche" in command:
        # Extract the search query from the command
        query = command.replace("suche", "")
        query = query.strip()
        if query:
            search(query)
        else:
            response = "Bitte geben Sie eine Suchanfrage ein."
            speak(response)
    elif "wetter" in command:
        # Call weather API and provide weather information
        response = "Das Wetter heute ist sonnig."
        speak(response)
    elif "erinnerung" in command:
        # Set a reminder using a database or scheduling library
        response = "Erinnerung erfolgreich festgelegt."
        speak(response)
    else:
        # If the command is not specific, perform a general search
        search(command)

def search(query):
    # Perform a voice-based search using a web browser
    url = f"https://www.google.com/search?q={query}&hl=de"
    webbrowser.open(url)

    # Send a GET request to the search results page
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant information from the search results page
    answer_element = soup.find("div", class_="Z0LcW")
    if answer_element:
        answer = answer_element.get_text()
        speak(answer)
    else:
        response = "Entschuldigung, ich konnte keine spezifische Antwort auf Ihre Anfrage finden."
        speak(response)

def speak(response):
    print("Assistent:", response)
    engine.say(response)
    engine.runAndWait()

# Main loop
while True:
    listen()