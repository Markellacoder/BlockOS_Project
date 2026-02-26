import subprocess
import os

def launch_app(app_path):
    # Ellenőrizzük, hogy Windows-os .exe fájlról van-e szó
    if app_path.endswith(".exe"):
        print(f"BlockOS: Windows környezet emulálása a(z) {app_path} fájlhoz...")
        # A Wine réteg hívása (ez van a system mappádban)
        subprocess.run(["wine", app_path])
    else:
        # Ha natív BlockOS/Linux app
        os.startfile(app_path)

# Példa: launch_app("apps/Brave/Brave.exe")