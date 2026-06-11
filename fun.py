import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# ---------------- WINDOW ---------------- #
root = tk.Tk()
root.title("Neon Nexus - Cyberpunk Realm")
root.geometry("800x500")
root.resizable(False, False)

# ---------------- BACKGROUND ---------------- #
bg_image = Image.open("cyber_bg.jpg")
bg_image = bg_image.resize((800, 500))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=800, height=500, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# ---------------- COLORS ---------------- #
NEON = "#00F5FF"
DARK = "#0B0F1A"

# ---------------- GLITCH TITLE ---------------- #
title_text = "NEON NEXUS"

title = tk.Label(
    root,
    text=title_text,
    font=("Consolas", 30, "bold"),
    fg=NEON,
    bg=DARK
)
title_window = canvas.create_window(400, 70, window=title)

def glitch_text():
    if random.randint(0, 10) > 7:
        corrupted = list(title_text)

        for _ in range(random.randint(1, 4)):
            i = random.randint(0, len(corrupted) - 1)
            corrupted[i] = random.choice(["#", "@", "%", "&", "█", "▓"])

        title.config(text="".join(corrupted))

        # jitter movement (NOW FIXED)
        canvas.coords(
            title_window,
            400 + random.randint(-5, 5),
            70 + random.randint(-2, 2)
        )

    else:
        title.config(text=title_text)
        canvas.coords(title_window, 400, 70)

    root.after(120, glitch_text)

# ---------------- GLASS FRAME (FAKE GLASSMORPHISM) ---------------- #
glass_frame = tk.Frame(
    root,
    bg="#0F172A",   # dark tinted glass
    padx=25,
    pady=25,
    highlightbackground="#00F5FF",
    highlightthickness=2
)

canvas.create_window(400, 260, window=glass_frame)

# inner soft border layer (glass depth effect)
inner_frame = tk.Frame(
    glass_frame,
    bg="#111827",
    padx=15,
    pady=15
)
inner_frame.pack()

# ---------------- INPUTS ---------------- #
tk.Label(
    inner_frame,
    text="USERNAME",
    font=("Consolas", 10),
    fg=NEON,
    bg="#111827"
).pack(anchor="w")

username_border = tk.Frame(
    inner_frame,
    bg="#00F5FF",   # neon border color
    padx=2,
    pady=2
)
username_border.pack(pady=(5, 12), anchor="w")

username_entry = tk.Entry(
    username_border,
    width=30,
    font=("Consolas", 11),
    bg="#0B0F1A",
    fg="white",
    insertbackground="white",
    relief="flat",
    borderwidth=0
)
username_entry.pack()

tk.Label(
    inner_frame,
    text="PASSWORD",
    font=("Consolas", 10),
    fg=NEON,
    bg="#111827"
).pack(anchor="w")

password_border = tk.Frame(
    inner_frame,
    bg="#00F5FF",
    padx=2,
    pady=2
)
password_border.pack(pady=(5, 15), anchor="w")

password_entry = tk.Entry(
    password_border,
    width=30,
    font=("Consolas", 11),
    show="*",
    bg="#0B0F1A",
    fg="white",
    insertbackground="white",
    relief="flat",
    borderwidth=0
)
password_entry.pack()

# ---------------- STATUS ---------------- #
status_label = tk.Label(
    root,
    text="SYSTEM: ONLINE",
    font=("Consolas", 10),
    fg="#00FF9F",
    bg=DARK
)
canvas.create_window(400, 440, window=status_label)

# ---------------- LOGIN LOGIC ---------------- #
VALID_USERS = {"admin": "1234", "neo": "matrix"}

def login():
    u = username_entry.get()
    p = password_entry.get()

    if not u or not p:
        status_label.config(text="SYSTEM: INPUT REQUIRED", fg="#FFB000")
        return

    if VALID_USERS.get(u) == p:
        status_label.config(text="ACCESS GRANTED", fg="#00FF9F")
        messagebox.showinfo("ACCESS", "Welcome to Neon Nexus")
    else:
        status_label.config(text="ACCESS DENIED", fg="#FF0055")

# ---------------- BUTTONS ---------------- #
btn_frame = tk.Frame(inner_frame, bg="#111827")
btn_frame.pack(pady=5)

login_btn = tk.Button(
    btn_frame,
    text="LOGIN",
    width=12,
    bg="#00F5FF",
    fg="black",
    font=("Consolas", 10, "bold"),
    command=login,
    relief="flat",
    activebackground="#00FF9F"
)
login_btn.pack(side="left", padx=5)

register_btn = tk.Button(
    btn_frame,
    text="REGISTER",
    width=12,
    bg="#1F2937",
    fg="#00F5FF",
    font=("Consolas", 10, "bold"),
    relief="flat",
    command=lambda: messagebox.showinfo("SYSTEM", "Locked module"),
    activebackground="#FF00FF"
)
register_btn.pack(side="left", padx=5)

# ---------------- HOVER EFFECT ---------------- #
def hover_on(e):
    login_btn.config(bg="#00FF9F")

def hover_off(e):
    login_btn.config(bg="#00F5FF")

login_btn.bind("<Enter>", hover_on)
login_btn.bind("<Leave>", hover_off)

# ---------------- START EFFECTS ---------------- #
glitch_text()
root.bind("<Return>", lambda e: login())

root.mainloop()