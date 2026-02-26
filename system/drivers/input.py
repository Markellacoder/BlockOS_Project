def init_input():
    print("BlockOS Input Driver: Egér és Billentyűzet inicializálása...")
    # Felismeri a csatlakoztatott eszközöket
    devices = ["USB Keyboard", "HID Compliant Mouse"]
    for dev in devices:
        print(f"Eszköz csatlakoztatva: {dev}")
    print("Gördítési sebesség beállítva (Apple Style: Natural Scrolling).")

if __name__ == "__main__":
    init_input()