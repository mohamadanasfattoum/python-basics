import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Convert speech to text
        text = recognizer.recognize_google(audio, language="ar")
        print("Recognized Text:", text)
        process_command(text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error:", str(e))

def process_command(command):
    # Implement logic to handle different commands
    if "بحث" in command:
        # Extract the search query from the command
        query = extract_search_query(command)
        if query:
            search(query)
        else:
            response = "من فضلك قدم استعلام البحث."
            speak(response)
    else:
        # Perform a general search
        search(command)

def extract_search_query(command):
    # Extract the search query from the command
    query = command.partition(' ')[-1]
    return query

def search(query):
    # Perform a web search using a web browser
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def speak(response):
    print("Assistant:", response)
    engine.say(response)
    engine.runAndWait()

# Main loop
while True:
    listen()