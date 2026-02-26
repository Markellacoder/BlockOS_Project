import os
import subprocess

def open_photos():
    # A felhasználó Képek mappájának elérési útja
    path = os.path.expanduser("~/Pictures")
    
    # Ha nem létezik, létrehozza
    if not os.path.exists(path):
        os.makedirs(path)
        
    print(f"BlockOS Photos: Galéria megnyitása ({path})")
    
    if os.name == 'nt':
        os.startfile(path)
    else:
        subprocess.run(["xdg-open", path])

if __name__ == "__main__":
    open_photos()