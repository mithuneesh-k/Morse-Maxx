import morseplay
from tkinter import *

# ---------- Functions ---------- #
def show_frame(frame):
    frame.tkraise()
    morze.update_idletasks()
    morze.geometry('')  # Dynamic resizing

# Button styling helper
def styled_button(parent, text, command, bg="#4CAF50", fg="white", width=20):
    btn = Button(parent, text=text, command=command, bg=bg, fg=fg, font=("Consolas", 18),
                 activebackground="#45a049", activeforeground="white", relief="flat", bd=0)
    btn.pack(pady=10, ipadx=10, ipady=5)
    return btn

# Copy button helper
def add_copy_button(parent, get_text):
    def copyclip():
        morze.clipboard_clear()
        morze.clipboard_append(get_text())
    return styled_button(parent, "Copy", copyclip, bg="#2196F3")

# ---------- Main Window ---------- #
morze = Tk()
morze.title("Morse MAXX")
morze.configure(bg="#f5f5f5")  # soft background

# Container for pages
container = Frame(morze, bg="#f5f5f5")
container.pack(fill="both", expand=True)

# ---------- Homepage ---------- #
home_frame = Frame(container, bg="#f5f5f5")
home_frame.grid(row=0, column=0, sticky="nsew")

Label(home_frame, text="MORSE MAXX", font=('Spectral', 60), fg="#ff3d00", bg="#f5f5f5").pack(pady=40)

styled_button(home_frame, "Morse To Text", lambda: show_frame(m2t_frame), bg="#29b6f6")
styled_button(home_frame, "Text to Morse", lambda: show_frame(t2m_frame), bg="#ef5350")

# ---------- Morse to Text Page ---------- #
m2t_frame = Frame(container, bg="#f5f5f5")
m2t_frame.grid(row=0, column=0, sticky="nsew")

Label(m2t_frame, text="Enter Morse Code:", font=("Consolas", 20), bg="#f5f5f5").pack(pady=15)
morset = Text(m2t_frame, font=("Consolas", 18), height=3, width=35, bd=2, relief="groove")
morset.pack(pady=5)

conv_txt = Label(m2t_frame, text="", font=("Consolas", 28), bg="#f5f5f5", wraplength=800)
conv_txt.pack(pady=15)

def returnMtoT():
    morse = morset.get("1.0", END).rstrip()
    conv_mors = morseplay.mor2txt(morse)
    conv_txt.configure(text=conv_mors)

styled_button(m2t_frame, "CONVERT", returnMtoT, bg="#ff7043")
add_copy_button(m2t_frame, lambda: morseplay.mor2txt(morset.get("1.0", END).rstrip()))
styled_button(m2t_frame, "Back", lambda: show_frame(home_frame), bg="#9e9e9e")

# ---------- Text to Morse Page ---------- #
t2m_frame = Frame(container, bg="#f5f5f5")
t2m_frame.grid(row=0, column=0, sticky="nsew")

Label(t2m_frame, text="Enter Text:", font=("Consolas", 20), bg="#f5f5f5").pack(pady=15)
textt = Text(t2m_frame, font=("Consolas", 18), height=3, width=35, bd=2, relief="groove")
textt.pack(pady=5)

conv_morse = Label(t2m_frame, text="", font=("Consolas", 28), bg="#f5f5f5", wraplength=800)
conv_morse.pack(pady=15)

def returnTtoM():
    text = textt.get("1.0", END).rstrip()
    conv_txt_val = morseplay.txt2mor(text)
    conv_morse.configure(text=conv_txt_val)

styled_button(t2m_frame, "CONVERT", returnTtoM, bg="#ff7043")
add_copy_button(t2m_frame, lambda: morseplay.txt2mor(textt.get("1.0", END).rstrip()))
styled_button(t2m_frame, "Back", lambda: show_frame(home_frame), bg="#9e9e9e")

# Start on homepage
show_frame(home_frame)

morze.mainloop()
