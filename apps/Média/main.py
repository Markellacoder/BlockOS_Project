import webbrowser

def open_media_center():
    print("BlockMedia: Zene és Videó központ...")
    # A YouTube Music a legjobb beépített megoldás
    url = "https://music.youtube.com"
    webbrowser.open(url)

if __name__ == "__main__":
    open_media_center()