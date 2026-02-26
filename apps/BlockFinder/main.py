import os
import json

def run_finder():
    theme = "light"
    if os.path.exists("system/settings.json"):
        with open("system/settings.json", "r") as f:
            theme = json.load(f).get("theme", "light")

    print(f"--- BlockFinder ({theme.upper()} MODE) ---")
    current_dir = os.getcwd()
    print(f"Helyszín: {current_dir}")
    
    print("\nFájlok:")
    for item in os.listdir(current_dir):
        icon = "📁" if os.path.isdir(item) else "📄"
        print(f"  {icon} {item}")

if __name__ == "__main__":
    run_finder()