import json
import os

FILE = "chrome_functions.json"


# Ensure the JSON file exists
def initialize():
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump({"links": []}, f, indent=4)


# Load links from file
def load_links():
    with open(FILE, "r") as f:
        return json.load(f)


# Save links to file
def save_links(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# Add a new link
def add_link(name, url):
    data = load_links()

    if search_link(name):
        print("Link already exists.")
        return

    for link in data["links"]:
        if link["name"].lower() == name.lower():
            print("Link already exists.")
            return

    data["links"].append({
        "name": name,
        "url": url
    })

    save_links(data)
    print("Link added.")


# Delete a link
def delete_link(name):
    data = load_links()

    new_links = [link for link in data["links"] if link["name"].lower() != name.lower()]

    if len(new_links) == len(data["links"]):
        print("Link not found.")
        return

    data["links"] = new_links
    save_links(data)
    print("Link deleted.")


# Search for a link
def search_link(name):
    data = load_links()

    for link in data["links"]:
        if name.lower() in link["name"].lower():
            return link

    return None


# Traverse all links
def list_links():
    data = load_links()

    if not data["links"]:
        print("No links saved.")
        return

    for link in data["links"]:
        print(f"{link['name']} -> {link['url']}")

# Return a list of all saved link names
def get_all_link_names():
    data = load_links()
    return [link["name"] for link in data["links"]]

# Run initialization when file loads
initialize()