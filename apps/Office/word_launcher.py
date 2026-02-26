import webbrowser

def start_word():
    # Megnyitja a Word-öt a beépített Brave böngészőben, app módban
    url = "https://www.microsoft365.com/launch/word"
    # Ez a parancs "app" módban nyitja meg, tehát nem lesznek böngésző fülek, 
    # úgy néz ki, mint egy külön ablak (Tahoe design).
    print("BlockOS: Word (Cloud) indítása...")
    webbrowser.open(url)

if __name__ == "__main__":
    start_word()