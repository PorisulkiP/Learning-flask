import tkinter as tk
import tkinter.messagebox as message

def open_results():
    veg_choice = state_of_ratio.get()
    user_choice = [cb_1.get(), cb_2.get(), cb_3.get()]
    message.showinfo("Title", "You choice " f'{user_choice}' " was choice")


root = tk.Tk()
root.geometry("400x500")

state_of_ratio = tk.IntVar()

tk.Label(root, text="Выбери свой овощь!", pady="30", font=('Time New Roman', 13)).pack(fill=tk.X)

ratio_frame = tk.Frame(root)
ratio_frame.pack()
rb_1 = tk.Radiobutton(ratio_frame, text="Tomato", value=1, variable = state_of_ratio)
rb_2 = tk.Radiobutton(ratio_frame, text="Cucumder", value=2, variable = state_of_ratio)
rb_3 = tk.Radiobutton(ratio_frame, text="Potato", value=3, variable = state_of_ratio)

check_frame = tk.Frame(root)
check_frame.pack()
cb_l = tk.Checkbutton(check_frame, text="У меня аллергия)")
cb_2 = tk.Checkbutton(check_frame, text="У меня судимость))")
cb_3 = tk.Checkbutton(check_frame, text="У меня поправки в конституцию))))))")



cb_l.pack()
cb_2.pack()
cb_3.pack()

button = tk.Button(root, text="I made a choice", command=open_results)
button.pack(side = tk.BOTTOM)

rb_1.pack(side = tk.LEFT)
rb_2.pack(side = tk.LEFT)
rb_3.pack(side = tk.LEFT)

root.mainloop()

