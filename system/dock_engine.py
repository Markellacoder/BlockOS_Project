import subprocess
import os
import json

class DockEngine:
    def __init__(self):
        self.apps_dir = "apps"
        self.settings_path = "system/settings.json"

    def launch(self, app_name):
        app_name = app_name.lower()
        
        # Útvonalak meghatározása az appokhoz
        app_map = {
            "safari": "BlockBrowser/main.py",
            "finder": "Fájlkezelő/main.py",
            "brave": "Brave/launcher.py",
            "word": "Office/word_launcher.py",
            "calc": "Calculator/main.py",
            "photos": "Photos/main.py",
            "camera": "Camera/main.py",
            "media": "Media/main.py",
            "games": "Games/main.py",
            "settings": "Settings/main.py"
        }

        if app_name in app_map:
            script_path = os.path.join(self.apps_dir, app_map[app_name])
            if os.path.exists(script_path):
                print(f"BlockOS: {app_name} indítása...")
                subprocess.Popen(["python3", script_path])
            else:
                print(f"Hiba: A(z) {script_path} nem található!")
        elif app_name == "shutdown":
            print("BlockOS leállítása...")
            os.system("shutdown /s /t 0" if os.name == 'nt' else "sudo shutdown now")

if __name__ == "__main__":
    # Ez a rész várja a hívást a Dock felületről
    import sys
    if len(sys.argv) > 1:
        engine = DockEngine()
        engine.launch(sys.argv[1])