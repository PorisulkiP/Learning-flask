import tkinter as tk

counter = 0

styles = [dict(bg="azure", fg="#333333"), dict(fg="white", bg="black")]

def add_label(Event=None):

    global counter
    name = user_entry.get()
    if len(name) < 3:
        hint.configure(text="Введите хотябы три символа")
        return

    user_entry.delete(0, tk.END)
    new_label = tk.Label(window, text=name, pady="10")
    new_label.configure(styles[counter%2])
    if counter >= 5:
        counter = 0
        children = window.winfo_children()
        for element in filter(lambda x: isinstance(x, tk.Label) and x.winfo_name() not in ('!label1', '!label2') != '!label', children):
            element.destroy()

    new_label.pack(fill=tk.X)

    counter += 1



window = tk.Tk()

window.geometry("400x500")

window.resizable(False, False)

user_entry = tk.Entry(window, width="60")
user_entry.pack()
user_entry.focus_set()

tk.Button(window, text="Beech", command=add_label).pack()

hint = tk.Label(window, text="Введите хотябы три символа", fg="indian red", font=("Time New Roman", 10))
hint.pack()

# tk.Label(window, text="Тыч в кнопку", pady="30", bg="NavajoWhite2", fg="#885144").pack()

user_entry.bind('<Enter>',add_label)

window.mainloop()