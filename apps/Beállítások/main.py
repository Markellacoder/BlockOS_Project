import json
import os

def load_settings():
    path = "system/settings.json"
    if not os.path.exists(path):
        return {"theme": "dark", "wallpaper": "default", "widgets": True}
    with open(path, "r") as f:
        return json.load(f)

def save_settings(data):
    with open("system/settings.json", "w") as f:
        json.dump(data, f, indent=4)

def main():
    config = load_settings()
    print("--- BlockOS Rendszerbeállítások ---")
    print(f"1. Téma mód: {config['theme']}")
    print(f"2. Widgetek: {'BE' if config['widgets'] else 'KI'}")
    
    val = input("\nMódosítandó szám (vagy 'q' a kilépéshez): ")
    if val == "1":
        config['theme'] = "light" if config['theme'] == "dark" else "dark"
    elif val == "2":
        config['widgets'] = not config['widgets']
    
    save_settings(config)
    print("Változások mentve!")

if __name__ == "__main__":
    main()