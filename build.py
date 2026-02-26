import os
import shutil

def build():
    print("--- BlockOS Build Folyamat Indítása ---")
    target = "BlockOS_Final"
    
    if os.path.exists(target):
        shutil.rmtree(target)
    os.makedirs(target)

    # Szükséges mappák átmásolása
    folders = ['apps', 'bootloader', 'desktop', 'installer', 'system']
    for f in folders:
        if os.path.exists(f):
            shutil.copytree(f, os.path.join(target, f))
            print(f"[OK] {f} mappa hozzáadva.")
        else:
            print(f"[!] HIÁNYZIK: {f}")

    print("\nKÉSZ! A BlockOS fájljai a 'BlockOS_Final' mappában vannak.")
    print("Ezt a mappát töltheted fel internetre vagy használhatod virtuális gépben.")

if __name__ == "__main__":
    build()