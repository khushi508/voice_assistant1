import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import random
import sys

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

# User Name
USER_NAME = "Khushi"

# Speak Function
def speak(text):
    print("Chatterly:", text)
    engine.say(text)
    engine.runAndWait()

# Greet the user
def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak(f"Good morning {USER_NAME}!")
    elif hour < 18:
        speak(f"Good afternoon {USER_NAME}!")
    else:
        speak(f"Good evening {USER_NAME}!")
    speak("I'm Chatterly, your chat buddy! How are you today?")

# Listen for command
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        try:
            # Timeout prevents hanging forever, phrase_time_limit limits long speech
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("I didn’t hear anything. Try again.")
            return "None"
        except Exception as e:
            speak("There was an error with the microphone.")
            print("Microphone error:", e)
            return "None"

    try:
        print("🧠 Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except sr.UnknownValueError:
        speak("Sorry, I didn’t understand.")
        return "None"
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return "None"

    return query.lower()


# Tell jokes
def tell_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "I told my computer I needed a break, and now it won’t stop sending vacation ads!",
        "Why did the developer go broke? Because he used up all his cache.",
        "You're awesome, Khushi! That’s the best joke I know!"
    ]
    speak(random.choice(jokes))

# Main
def main():
    wish_user()
    try:
        while True:
            query = take_command()

            if query == "none":
                continue

            elif 'how are you' in query:
                speak("I'm doing great! Especially since I'm chatting with you.")

            elif 'your name' in query:
                speak("I'm khushi's assistant!")

            elif 'my name' in query:
                speak(f"Of course! You’re {USER_NAME}, the queen of cool!")

            elif 'wikipedia' in query:
                speak("Let me look that up on Wikipedia...")
                query = query.replace("wikipedia", "")
                try:
                    result = wikipedia.summary(query, sentences=2)
                    speak(result)
                except:
                    speak("Couldn't find anything useful on that.")

            elif 'open youtube' in query:
                speak("Opening YouTube for you!")
                webbrowser.open("https://www.youtube.com")

            elif 'open google' in query:
                speak("Heading to Google!")
                webbrowser.open("https://www.google.com")

            elif 'time' in query:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"It’s {current_time}")

            elif 'joke' in query:
                tell_joke()

            elif 'exit' in query or 'bye' in query or 'stop' in query:
                speak("Goodbye Khushi! Chat with you soon 💖")
                break

            else:
                speak(random.choice([
                    "Hmm, not sure I understood that.",
                    "Let’s talk about something else!",
                    "You sound interesting! Tell me more.",
                    "Still learning… but I love chatting!"
                ]))

    except KeyboardInterrupt:
        speak("You pressed stop. Goodbye Khushi!")
        sys.exit(0)

# Run app
if __name__ == "__main__":
    main()
