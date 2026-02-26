import webbrowser
import os

def start_excel():
    # Az Office Online Excel elérési útja
    url = "https://www.microsoft365.com/launch/excel"
    print("BlockOS: Excel (Cloud-Native) indítása...")
    
    # Megnyitás a Brave motorral, ha telepítve van, egyébként alapértelmezett böngésző
    webbrowser.open(url)

if __name__ == "__main__":
    start_excel()