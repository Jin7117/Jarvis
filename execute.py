import chromeFunctions as browser_control
import spotify 
import systemFunctions
import file
import chatgpt


# ------------------------
# HELPER
# ------------------------
def require_internet():
    if not systemFunctions.is_online():
        print("No internet connection.")
        return False
    return True


# ------------------------
# CHROME FUNCTIONS
# ------------------------
def chrome_open(query):
    if not require_internet(): return
    browser_control.smart_search(query) if query else browser_control.open_chrome()

def chrome_search(query):
    if not require_internet(): return
    browser_control.search_google(query)

def chrome_close(query):
    if not require_internet(): return
    browser_control.close_all_chrome()


# ------------------------
# INCOGNITO
# ------------------------
def incognito_open(query):
    if not require_internet(): return
    browser_control.smart_search(query) if query else browser_control.open_incognito()


# ------------------------
# YOUTUBE
# ------------------------
def youtube_search(query):
    browser_control.searchYoutube(query) if query else browser_control.smart_search("youtube")


# ------------------------
# GITHUB
# ------------------------
def github_search(query):
    browser_control.searchGithub(query) if query else browser_control.smart_search("github")


# ------------------------
# WIKI
# ------------------------
def wiki_search(query):
    browser_control.searchWiki(query) if query else browser_control.smart_search("wikipedia")


# ------------------------
# SPOTIFY
# ------------------------
def spotify_open(query):
    spotify.spotify_search(query) if query else spotify.open_spotify()

def spotify_search_func(query):
    spotify.spotify_search(query)

def spotify_play(query):
    if query:
        spotify.spotify_search(query)
    else:
        spotify.open_spotify()
        spotify.playpause()


# ------------------------
# SYSTEM
# ------------------------
def system_show(query):
    if query == "time":
        print(systemFunctions.get_current_time())

    elif query == "memory":
        print(systemFunctions.get_memory_info())

    elif query == "cpu":
        print(systemFunctions.get_cpu_usage())

    else:
        print(systemFunctions.get_system_info())


# ------------------------
# FILE
# ------------------------
def file_open(query):
    if query:
        file.open_path(query)

def file_create(query):
    name = query if query else input("Enter file name: ")
    file.create_file(name)

def file_delete(query):
    name = query if query else input("Enter file name: ")
    file.delete_file(name)


# ------------------------
# FOLDER
# ------------------------
def folder_open(query):
    if query:
        file.open_path(query)


# ------------------------
# CHATGPT
# ------------------------
def chatgpt_open(query):
    chatgpt.search_chatgpt(query) if query else chatgpt.open_chatgpt()


# ------------------------
# VICTORIA
# ------------------------
def victoria_open(query):
    chatgpt.victoria()


# ========================
# 🧠 ROUTING DICTIONARY
# ========================
routes = {
    "chrome": {
        "open": chrome_open,
        "search": chrome_search,
        "close": chrome_close
    },
    "incognito": {
        "open": incognito_open
    },
    "youtube": {
        "open": youtube_search,
        "search": youtube_search
    },
    "github": {
        "open": github_search,
        "search": github_search
    },
    "wiki": {
        "open": wiki_search,
        "search": wiki_search
    },
    "spotify": {
        "open": spotify_open,
        "search": spotify_search_func,
        "play": spotify_play
    },
    "system": {
        "show": system_show,
        "usage": system_show
    },
    "file": {
        "open": file_open,
        "create": file_create,
        "delete": file_delete
    },
    "folder": {
        "open": folder_open
    },
    "chatgpt": {
        "open": chatgpt_open
    },
    "victoria": {
        "open": victoria_open
    }
}


# ========================
# 🚀 EXECUTOR
# ========================
def execute(slot_result):

    action = slot_result.get("action")
    target = slot_result.get("target")
    query = slot_result.get("query")

    # ------------------------
    # PARAMETER CHECK
    # ------------------------
    if not action:
        print("Missing parameter: action")
        action = input("Action: ")

    if not target:
        print("Missing parameter: target")
        target = input("Target: ")

    if query is None:
        print("Missing parameter: query")
        query = input("Query: ")
        if query.lower() == "none":
            query = ""

    print(f"[Executor] Action: {action} | Target: {target} | Query: {query}")

    # ------------------------
    # ROUTING
    # ------------------------
    target_routes = routes.get(target)

    if not target_routes:
        print("Unknown target")
        return False

    action_func = target_routes.get(action)

    if not action_func:
        print("Unknown action for this target")
        return False

    action_func(query)
    return True