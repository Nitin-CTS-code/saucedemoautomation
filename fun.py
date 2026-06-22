import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.configure(bg="#0f0f1a")
root.title("Legend of Pythonia")

title = tk.Label(
    root,
    text="LEGEND OF PYTHONIA",
    fg="gold",
    bg="#0f0f1a"
)
title.pack(pady=50)


userInput = tk.Entry(
    root,
    bg="#e1e1e2",
    fg="black",
)

userInput.pack()


def open_game():
    name = userInput.get()

    root.withdraw()

    game = tk.Toplevel(root)
    game.title("Game Screen")
    game.geometry("500x400")
    game.configure(bg="#101020")

    tk.Label(
        game,
        text=f"Welcome to the World, {name}!",
        font=("Helvetica", 18, "bold"),
        fg="gold",
        bg="#101020"
    ).pack(pady=50)

    tk.Button(
        game,
        text="Exit",
        command=root.destroy
    ).pack()


btn = tk.Button(
    root,
    text="ENTER WORLD",
    bg="gold",
    fg="black",
    activebackground="orange"
)
btn.pack(pady=50)


root.mainloop()