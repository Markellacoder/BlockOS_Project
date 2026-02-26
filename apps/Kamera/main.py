import os
import subprocess

def start_camera():
    print("BlockOS Tahoe: Kamera inicializálása...")
    # Windows alatt a gyári kamerát hívja, Linuxon a Cheese-t
    if os.name == 'nt':
        os.system("start microsoft.windows.camera:")
    else:
        try:
            subprocess.run(["cheese"])
        except:
            print("Hiba: Nincs telepítve kamera szoftver (cheese).")

if __name__ == "__main__":
    start_camera()