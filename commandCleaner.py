# command_cleaner.py

FILLER_PHRASES = [
    "could you",
    "would you",
    "can you",
    "please",
    "for me",
    "do me a favor",
    "kindly",
    "would you mind",
    "jarvis",
    "hey jarvis",
    "ok jarvis",
    "okay jarvis",
    "can you please",
    "could you please",
    "would you please",
    "a favor",
    "favor",
    "mind",
    "if you don’t mind",
    "would it be possible",
    "may I ask you to",
    "I’d appreciate it if",
    "be so kind",
    "could I trouble you",
    "would you be able to",
    "do me this one thing",
    "help me out",
    "assist me",
    "lend me a hand",
    "do me this favor",
    "if you could",
    "would you kindly",
    "can I ask you",
    "I need you to",
    "I want you to",
    "I’d like you to",
    "please do",
    "please help",
    "please assist",
    "please make sure",
    "please go ahead",
    "please try",
    "please check",
    "please ensure",
]



def clean_command(command: str) -> str:

    command = command.lower()
    command = replace_synonyms(command)

    for phrase in FILLER_PHRASES:
        command = command.replace(phrase, "")

    # remove extra spaces
    command = " ".join(command.split())
    print("cleaned -> " + command)

  

    return command

REPLACEMENTS = {
    "launch": "open",
    "start": "open",
    "bring up": "open",
    "call": "open",
    "check": "show",
    "view": "show",
    "display": "show",
    "see": "show",
    "look at": "show",
    "show me": "show",
    "find": "search",
    "search for": "search",
    "look up": "search",
    "explore": "search",
    "run": "execute",
    "execute": "run",
    "initiate": "start",
    "begin": "start",
    "activate": "start",
    "play": "start",
    "remove": "delete",
    "erase": "delete",
    "clear": "delete",
    "discard": "delete",
    "destroy": "delete",
    "add": "create",
    "make": "create",
    "compose": "create",
    "write": "create",
    "generate": "create",
    "update": "edit",
    "modify": "edit",
    "change": "edit",
    "adjust": "edit",
    "revise": "edit",
    "correct": "edit",
    "wikipedia":"wiki",
    "quit":"close",
    "information":"usage",
    "computer details":"usage",
    "pc details":"usage",
    "get":"usage"
}


def replace_synonyms(command: str) -> str:
    for key, value in REPLACEMENTS.items():
        command = command.replace(key, value)
    return command