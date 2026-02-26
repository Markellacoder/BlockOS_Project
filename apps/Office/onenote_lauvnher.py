import webbrowser

def start_onenote():
    url = "https://www.microsoft365.com/launch/onenote"
    print("BlockOS: OneNote (Cloud-Native) indítása...")
    webbrowser.open(url)

if __name__ == "__main__":
    start_onenote()