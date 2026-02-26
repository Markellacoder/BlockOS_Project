import webbrowser
import json
import os

def launch_browser():
    # Rendszerbeállítások beolvasása
    theme = "light"
    if os.path.exists("system/settings.json"):
        with open("system/settings.json", "r") as f:
            theme = json.load(f).get("theme", "light")

    print(f"BlockBrowser indítása {theme} módban...")
    # Safari-szerű kezdőlap
    url = "https://www.google.com" 
    webbrowser.open(url)

if __name__ == "__main__":
    launch_browser()