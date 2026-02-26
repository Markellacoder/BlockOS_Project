import webbrowser

def start_powerpoint():
    url = "https://www.microsoft365.com/launch/powerpoint"
    print("BlockOS: PowerPoint (Cloud-Native) indítása...")
    webbrowser.open(url)

if __name__ == "__main__":
    start_powerpoint()