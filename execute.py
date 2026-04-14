import chromeFunctions as browser_control

def execute(slot_result):

    action = slot_result.get("action")
    target = slot_result.get("target")
    query = slot_result.get("query")

    # ------------------------
    # MISSING PARAMETER CHECK (unchanged)
    # ------------------------
    if not action:
        print("Missing parameter: action")
        action = input("Action: ")
    elif not target:
        print("Missing parameter: target")
        target = input("Target: ")
    elif not query:
        print("Missing parameter: query")
        print("What should we use as a Query?")
        query = input("Query: ")
        if query == "none":
            query = ""

    print(f"[Executor] Action: {action} | Target: {target} | Query: {query}")

    # ------------------------
    # TARGET FIRST LOGIC
    # ------------------------

    # ===== CHROME =====
    if target == "chrome":

        if action == "open":
            if query:
                browser_control.smart_search(query)
            else:
                browser_control.open_chrome()
            return True

        elif action == "search":
            browser_control.search_google(query)
            return True
        
        elif action == "close":
            browser_control.close_all_chrome()
            return True

    # ===== INCOGNITO =====
    elif target == "incognito":

        if action == "open":
            if query:
                browser_control.smart_search(query)
            else:
                browser_control.open_incognito()
            return True

    # ===== YOUTUBE =====
    elif target == "youtube":

        if action == "open":
            if query:
                browser_control.searchYoutube(query)
            else:
                browser_control.smart_search("youtube")
            return True

        elif action == "search":
            
            browser_control.searchYoutube(query)
            return True

    # ===== Github =====
    elif target == "github":

        if action == "open":
            if query:
                browser_control.searchYoutube(query)
            else:
                browser_control.smart_search("youtube")
            return True

        elif action == "search":
            
            browser_control.searchYoutube(query)
            return True

