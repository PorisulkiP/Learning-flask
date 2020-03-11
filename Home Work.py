import tkinter as tk

root = tk.Tk()
root.title("За .grid() и двор стреляю в упор")
root.geometry("210x170")
root.resizable(False, False)

tk.Label(text="Label").grid(row=0, column=0)
tk.Label(text="Label 1").grid(row=1, column=0)

tk.Entry(width=15).grid(row=0, column=1, columnspan=10)
tk.Entry(width=15).grid(row=1, column=1, columnspan=10)

tk.Button(text="TextBotton", pady=10).grid(row=0, column=11, rowspan=1)
tk.Button(text="TextBotton", pady=30).grid(row=1, column=11, rowspan=4)

RB = tk.Radiobutton(root)
RB1 = tk.Radiobutton(root)
RB2 = tk.Radiobutton(root)

RB.grid(row=4, column=0)
RB1.grid(row=4, column=1)
RB2.grid(row=4, column=2)

scale = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale.grid(row=3, column=0, columnspan=5, rowspan=1)

tk.Checkbutton(root, text="Show title").place(x=0, y=140)

root.mainloop()