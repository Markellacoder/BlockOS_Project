import time
import subprocess

class BlockOS_PhoneLink:
    def __init__(self):
        self.app_name = "BlockOS PhoneLink"
        self.connected_device = None

    def scan_bluetooth(self):
        print(f"[{self.app_name}] Bluetooth modul aktiválása...")
        time.sleep(1.5)
        print("Keresés: Közeli iOS és Android eszközök...")
        
        # Szimulált eszközlista (Valódi környezetben a bluetooth könyvtár listázná)
        devices = ["iPhone 15 Pro", "Samsung Galaxy S24", "Xiaomi 14 Ultra"]
        for i, device in enumerate(devices):
            print(f"[{i+1}] {device}")
        
        choice = input("\nVálassz eszközt a csatlakozáshoz (szám): ")
        try:
            self.connected_device = devices[int(choice)-1]
            self.establish_connection()
        except:
            print("Hiba: Érvénytelen választás.")

    def establish_connection(self):
        print(f"\nKapcsolódás: {self.connected_device}...")
        time.sleep(2)
        print("✓ Biztonságos kapcsolat létrejött.")
        print("✓ Képernyőtükrözés protokoll aktív.")
        self.show_remote_screen()

    def show_remote_screen(self):
        clear_cmd = 'cls' if subprocess.os.name == 'nt' else 'clear'
        subprocess.os.system(clear_cmd)
        
        print(f"--- {self.app_name} : {self.connected_device} ---")
        print("------------------------------------------")
        print("|                                        |")
        print("|       [ TELEFON KIJELZŐJE ITT ]        |")
        print("|                                        |")
        print("|      Használd az egeret és a           |")
        print("|      billentyűzetet a vezérléshez!     |")
        print("|                                        |")
        print("------------------------------------------")
        print("Kilépéshez nyomj 'Q'-t.")

if __name__ == "__main__":
    app = BlockOS_PhoneLink()
    app.scan_bluetooth()