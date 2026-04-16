import json
import os

FILE = "paths.json"


def load_paths():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)


def save_paths(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_path(name, path):
    data = load_paths()
    data[name.lower()] = path
    save_paths(data)
    print(f"[+] Added: {name} -> {path}")


def delete_path(name):
    data = load_paths()
    if name.lower() in data:
        del data[name.lower()]
        save_paths(data)
        print(f"[-] Deleted: {name}")
    else:
        print("[!] Not found")


def search_path(name):
    data = load_paths()
    return data.get(name.lower(), None)


def list_paths():
    data = load_paths()
    if not data:
        print("[!] No paths stored")
        return
    for key, value in data.items():
        print(f"{key} -> {value}")


# Simple CLI (optional)
if __name__ == "__main__":
    while True:
        cmd = input("\nCommand (add/delete/search/list/exit): ").lower()

        if cmd == "add":
            name = input("Name: ")
            path = input("Path: ")
            add_path(name, path)

        elif cmd == "delete":
            name = input("Name: ")
            delete_path(name)

        elif cmd == "search":
            name = input("Name: ")
            result = search_path(name)
            print(result if result else "[!] Not found")

        elif cmd == "list":
            list_paths()

        elif cmd == "exit":
            break