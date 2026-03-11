# main.py
import speech_recognition as sr
import chromeFunctions  # your Chrome module
import linksEdit
import spacy
import time
import datetime
import asyncio
from edge_tts import Communicate
import playsound
import os

# -----------------------------
# Voice / TTS Setup
# -----------------------------
TEMP_AUDIO = "speech.mp3"

async def _speak_async(text, voice="en-US-AriaNeural"):
    communicate = Communicate(text, voice=voice)
    await communicate.save(TEMP_AUDIO)
    playsound.playsound(TEMP_AUDIO)
    os.remove(TEMP_AUDIO)

def speak(text):
    """Speak text using edge-tts"""
    asyncio.run(_speak_async(text))

# -----------------------------
# NLP Setup
# -----------------------------
nlp = spacy.load("en_core_web_sm")

# -----------------------------
# Speech Recognition Setup
# -----------------------------
recognizer = sr.Recognizer()
mic = sr.Microphone(device_index=1)

# -----------------------------
# Helper Functions
# -----------------------------
def get_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning sir."
    elif 12 <= hour < 17:
        return "Good afternoon sir."
    elif 17 <= hour < 21:
        return "Good evening sir."
    else:
        return "Good night sir."

# -----------------------------
# NLP Parsing for Commands
# -----------------------------
def parse_command(command):
    command_lower = command.lower().replace("jarvis", "").strip()
    doc = nlp(command_lower)

    intent = None
    query = None
    normal_window = False  # Default for smart search

    # Intent keywords
    search_keywords = ["search", "look up", "find"]
    open_keywords = ["open", "go to", "launch"]

    # Detect intent from verbs
    for token in doc:
        if token.lemma_ in search_keywords:
            intent = "search"
            break
        if token.lemma_ in open_keywords:
            intent = "open"
            break

    # Check if any saved link matches
    saved_links = [link.lower() for link in linksEdit.get_all_link_names()]
    for link_name in saved_links:
        if link_name in command_lower:
            intent = "open"
            query = link_name
            return intent, query, normal_window

    # Extract search query
    if intent == "search":
        for k in search_keywords:
            if k in command_lower:
                query = command_lower.split(k,1)[1].replace("on chrome","").strip()
                break

    # Default fallback
    if query is None and intent is None:
        intent = "search"
        query = command_lower

    return intent, query, normal_window

# -----------------------------
# Jarvis Listener
# -----------------------------
def listen_for_jarvis():
    with mic as source:
        print("Calibrating mic...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        greeting = get_greeting()
        print(greeting)
        speak(greeting)
        print("Ready... Say 'Jarvis' to wake me up!")

        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=5)
                text = recognizer.recognize_google(audio).lower()
                print(f"Heard: {text}")

                # Check if Jarvis name is mentioned
                if "jarvis" in text:
                    print("Jarvis activated!")
                    speak("Yes, sir?")

                    # Parse command in same line
                    intent, query, normal_window = parse_command(text)
                    if query:
                        execute_command(intent, query, normal_window)
                        continue

                    # Wait 5 seconds for additional command if not in same line
                    print("Waiting 5 seconds for command...")
                    try:
                        audio_followup = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        followup_text = recognizer.recognize_google(audio_followup).lower()
                        intent, query, normal_window = parse_command(followup_text)
                        if query:
                            execute_command(intent, query, normal_window)
                        else:
                            speak("No valid command detected, sir. Going back to sleep.")
                            print("No valid command detected. Going back to sleep.")
                    except sr.WaitTimeoutError:
                        speak("No command detected within 5 seconds, sir. Going back to sleep.")
                        print("No command detected within 5 seconds. Going back to sleep.")

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError:
                print("API unavailable")
            except KeyboardInterrupt:
                speak("Shutting down, sir.")
                print("Stopping...")
                break

# -----------------------------
# Execute Commands
# -----------------------------
def execute_command(intent, query, normal_window=False):
    if intent == "search":
        speak(f"Searching for {query}")
        print(f"Searching for: {query}")
        chromeFunctions.smart_search(query, normal=normal_window)
    elif intent == "open":
        speak(f"Opening {query}")
        print(f"Opening: {query}")
        chromeFunctions.open_saved_link(query)
    elif intent == "new tab":
        speak("Opening a new tab")
        print("Opening a new tab")
        chromeFunctions.new_tab()
    elif intent == "close tab":
        speak("Closing the current tab")
        print("Closing the current tab")
        chromeFunctions.close_tab()
    elif intent == "next tab":
        speak("Switching to the next tab")
        print("Switching to next tab")
        chromeFunctions.next_tab()
    elif intent == "previous tab":
        speak("Switching to the previous tab")
        print("Switching to previous tab")
        chromeFunctions.previous_tab()
    elif intent == "reopen tab":
        speak("Reopening the last closed tab")
        print("Reopening closed tab")
        chromeFunctions.reopen_closed_tab()
    elif intent == "scroll down":
        speak("Scrolling down")
        print("Scrolling down")
        chromeFunctions.scroll_down()
    elif intent == "scroll up":
        speak("Scrolling up")
        print("Scrolling up")
        chromeFunctions.scroll_up()
    elif intent == "go back":
        speak("Going back")
        print("Going back")
        chromeFunctions.go_back()
    elif intent == "go forward":
        speak("Going forward")
        print("Going forward")
        chromeFunctions.go_forward()
    elif intent == "refresh":
        speak("Refreshing the page")
        print("Refreshing the page")
        chromeFunctions.refresh_page()
    elif intent == "hard refresh":
        speak("Performing a hard refresh")
        print("Performing hard refresh")
        chromeFunctions.hard_refresh()
    elif intent == "zoom in":
        speak("Zooming in")
        print("Zooming in")
        chromeFunctions.zoom_in()
    elif intent == "zoom out":
        speak("Zooming out")
        print("Zooming out")
        chromeFunctions.zoom_out()
    elif intent == "reset zoom":
        speak("Resetting zoom")
        print("Resetting zoom")
        chromeFunctions.reset_zoom()
    elif intent == "bookmark":
        speak("Bookmarking this page")
        print("Bookmarking page")
        chromeFunctions.bookmark_page()
    elif intent == "downloads":
        speak("Opening downloads")
        print("Opening downloads")
        chromeFunctions.open_downloads()
    elif intent == "history":
        speak("Opening browser history")
        print("Opening history")
        chromeFunctions.open_history()
    else:
        speak("Command not recognized, sir.")
        print("Command not recognized")

# -----------------------------
# Main Entry
# -----------------------------
if __name__ == "__main__":
    listen_for_jarvis()