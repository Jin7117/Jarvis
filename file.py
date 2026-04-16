import os
import shutil
from manager import search_path , add_path , delete_path


def open_path(name):
    path = search_path(name)

    if not path:
        print("[!] Path not found")
        return

    if os.path.exists(path):
        print(f"[+] Opening: {path}")
        os.startfile(path)  # Windows only
    else:
        print("[!] Path does not exist")


def create_file(new_file_name):
    name = input("Where do we need to create the file -> ").strip()
    base_path = search_path(name)

    if not base_path:
        print("[!] Base path not found")
        return

    full_path = os.path.join(base_path, new_file_name)

    try:
        with open(full_path, "w") as f:
            f.write("")

        print(f"[+] Created file: {full_path}")

        file_key = new_file_name.split(".")[0]  # use filename (without extension) as key
        add_path(file_key, full_path)

        print(f"[+] Stored '{file_key}' in path memory")

    except Exception as e:
        print(f"[!] Error creating file: {e}")


import os

def delete_file(file_key):
    full_path = search_path(file_key)
    if not full_path:
        print("Sir, I was unable to locate the file in memory.")
        
        manual_path = input("Kindly provide the full file path, Sir: ").strip()
        
        if not manual_path:
            print("Understood, Sir. Operation aborted.")
            return
        
        full_path = manual_path
    if os.path.exists(full_path):
        print(f"Sir, I have located the file:\n{full_path}")
        
        confirm = input("Shall I proceed with deletion? This action cannot be undone. (yes/no): ").strip().lower()

        if confirm in ["yes", "y", "proceed", "do it"]:
            os.remove(full_path)
            print("Consider it done, Sir. The file has been erased from existence.")
            delete_path(file_key)

        else:
            print("As you wish, Sir. The file remains untouched.")
    else:
        print("Sir, the file does not exist at the specified location.")


def empty_folder(name):
    base_path = search_path(name)

    if not base_path:
        print("Sir, I was unable to locate the specified directory.")
        return

    if not os.path.exists(base_path):
        print("Sir, the directory does not exist.")
        return

    print(f"Sir, I have accessed the directory:\n{base_path}")
    
    confirm = input("This will remove ALL contents inside this folder. Shall I proceed? (yes/no): ").strip().lower()

    if confirm not in ["yes", "y", "proceed", "do it"]:
        print("Understood, Sir. No changes have been made.")
        return

    try:
        for item in os.listdir(base_path):
            item_path = os.path.join(base_path, item)

            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

        print("It is done, Sir. The directory has been… cleansed.")
    
    except Exception as e:
        print(f"Apologies, Sir. I encountered an issue: {e}")


