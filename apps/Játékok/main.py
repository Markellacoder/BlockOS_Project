import webbrowser

def open_games_hub():
    print("BlockOS Games: Játék központ indítása...")
    # Egy online játékportál, ami azonnal fut a BlockBrowserben
    url = "https://www.poki.com" 
    webbrowser.open(url)

if __name__ == "__main__":
    open_games_hub()