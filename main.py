from commandCleaner import clean_command
from command_parser import classify_sentence 
from execute import execute



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




   
    