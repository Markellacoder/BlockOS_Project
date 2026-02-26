import os
import sys

def startup():
    # Ez a rész felel azért, hogy teljes képernyőn induljon a GUI
    print("BlockOS Kernel v1.0 - Booting Hardware...")
    
    # Ellenőrzi, hogy van-e grafikus felület, ha nincs, elindítja
    if sys.platform == "linux":
        # Ez kényszeríti ki a teljes képernyős módot Linuxon (a másik laptopon)
        os.system("xinit python3 system/dock_engine.py --kiosk")
    else:
        # Windows teszteléshez
        os.system("python system/dock_engine.py")

if __name__ == "__main__":
    startup()