import time
import os
import json

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class BlockOS_Installer:
    def __init__(self):
        self.config_path = "system/settings.json"
        if not os.path.exists("system"):
            os.makedirs("system")

    def run(self):
        clear()
        print("\n" + "="*40)
        print("       BLOCKOS INSTALLER v2026")
        print("="*40 + "\n")
        time.sleep(1)
        
        # 1. Alapbeállítások
        lang = input("Nyelv / Language (HU/EN): ")
        print("\nVerzió kiválasztása:")
        print("[1] BlockOS Home")
        print("[2] BlockOS Pro")
        ver_choice = input("Választás (1/2): ")
        version = "Pro" if ver_choice == "2" else "Home"
        
        # 2. Design választó (Ez állítja be az iPhone-stílusú ikonokat)
        clear()
        print("--- MEGJELENÉS BEÁLLÍTÁSA ---")
        print("[1] Világos mód (Light Mode)")
        print("[2] Sötét mód (Dark Mode - iPhone stílusú sötét ikonok)")
        mode_choice = input("Válassz stílust (1/2): ")
        theme = "dark" if mode_choice == "2" else "light"
        
        # 3. Felhasználói adatok (A lezárt képernyőhöz)
        clear()
        print("--- FELHASZNÁLÓI PROFIL ---")
        name = input("Add meg a neved: ")
        pin = input("Állíts be egy PIN kódot (a belépéshez): ")
        
        # 4. Telepítési folyamat szimulációja
        clear()
        print(f"BlockOS {version} telepítése folyamatban...")
        for i in range(0, 101, 5):
            time.sleep(0.1)
            print(f"Folyamat: {i}% ", end='\r')
            
        # Adatok mentése a rendszernek
        settings = {
            "user": name,
            "password": pin,
            "theme": theme,
            "lang": lang,
            "version": version,
            "wallpaper": "bootloader/splash.png", # Alapértelmezett háttér a logód
            "widgets": True
        }
        
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=4, ensure_ascii=False)

        clear()
        print("\n" + "!"*40)
        print("      TELEPÍTÉS SIKERES!")
        print(f"      Üdvözlünk, {name}!")
        print("!"*40)
        print("\nA rendszer most már készen áll. Indítsd el a Kernelt.")
        time.sleep(3)

if __name__ == "__main__":
    BlockOS_Installer().run()