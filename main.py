from commandCleaner import clean_command
from command_parser import classify_sentence 
from execute import execute
from datetime import datetime 

def greet():
    current_hour = datetime.now().hour
    
    if 5 <= current_hour < 12:
        return "Good morning, boss. Systems are fresh and ready."
    elif 12 <= current_hour < 17:
        return "Good afternoon sir. What shall we work on today?"
    elif 17 <= current_hour < 21:
        return "Good evening boss. Let’s get things done."
    else:
        return "Burning the midnight oil, I see. I'm with you sir."

print(greet())
while True:

    command = input("Command: ")
    cleaned = clean_command(command)
    text = classify_sentence(cleaned)
    print(text)
    execute(text)


    # Optional exit
    if command.lower() in ["exit", "quit"]:
        print("Jarvis shutting down.")
        break




   
    