import tkinter as tk

counter = 0

styles = [dict()]

def add_label():
    global counter
    name = user_entry.get()
    user_entry.delete(0, tk.END)
    new_label = tk.Label(window, text=name, pady="20")

    new_label.configure(styles[counter%2])

    new_label.pack(fill=tk.X)
    counter += 1



window = tk.Tk()

window.geometry("400x500")
window.resizable(False, False)

tk.Label(window, text="Тыч в кнопку", pady="30", bg="NavajoWhite2", fg="#885144").pack()
user_entry = tk.Entry(window, width="60")
user_entry.pack()
tk.Button(window, text="Beech", command=add_label).pack()

window.mainloop()