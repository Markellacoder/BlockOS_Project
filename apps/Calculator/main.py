import tkinter as tk
import json
import os

def get_theme():
    if os.path.exists("system/settings.json"):
        with open("system/settings.json", "r") as f:
            return json.load(f).get("theme", "light")
    return "light"

def on_click(btn_text):
    current = entry.get()
    if btn_text == "=":
        try:
            res = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(res))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Hiba")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)

theme = get_theme()
root = tk.Tk()
root.title("BlockCalc")
root.geometry("260x380")

# Színpaletta mód választás alapján
bg_main = "#1c1c1c" if theme == "dark" else "#f9f9f9"
fg_main = "white" if theme == "dark" else "black"
btn_num = "#333333" if theme == "dark" else "#e0e0e0"

root.configure(bg=bg_main)

entry = tk.Entry(root, font=("SF Pro", 30), bg=bg_main, fg=fg_main, borderwidth=0, justify="right")
entry.pack(fill="both", padx=15, pady=25)

btns = [
    'C', '/', '*', '-',
    '7', '8', '9', '+',
    '4', '5', '6', '=',
    '1', '2', '3', '0', '.'
]

frame = tk.Frame(root, bg=bg_main)
frame.pack()

for i, txt in enumerate(btns):
    color = "#ff9f0a" if txt in "/ * - + =" else btn_num
    b = tk.Button(frame, text=txt, width=5, height=2, bg=color, fg=fg_main if theme == "dark" or txt in "/ * - + =" else "black",
                  font=("SF Pro", 12, "bold"), borderwidth=0, command=lambda x=txt: on_click(x))
    b.grid(row=i//4, column=i%4, padx=3, pady=3)

root.mainloop()