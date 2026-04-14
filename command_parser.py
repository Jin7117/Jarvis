def classify_sentence(sentence: str):
    # Define keyword groups
    actions = ["open", "close", "find", "search", "delete", "create"]
    targets = ["chrome", "youtube", "wikipedia", "github", "upes", "lms", "aniwatch", "incognito"]

    STOPWORDS = {
        "the", "a", "an", "please", "for", "me", "to", "and",
        "on", "in", "at", "of", "is", "are", "was", "were",
        "can", "you", "could", "would", "should", "my"
    }
    
    words = sentence.lower().split()

    action = None
    target = None

    # Find action
    for a in actions:
        if a in words:
            action = a
            words.remove(a)
            break

    # Find target
    for t in targets:
        if t in words:
            target = t
            words.remove(t)
            break

    # Remaining words become query
    query = None
    for i, word in enumerate(words):
        if word in ["search", "find", "about", "for"]:
            query_words = words[i+1:]
            query_words = [w for w in query_words if w not in STOPWORDS]
            query = " ".join(query_words)
            break

    # fallback: clean remaining words
    if not query:
        filtered_words = [w for w in words if w not in STOPWORDS]
        query = " ".join(filtered_words) if filtered_words else None

    return {
        "action": action,
        "target": target,
        "query": query
    }

