import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("HomeWork")
root['bg'] = "gray22"
root.geometry("300x300")
root.resizable(False, False)

img_1 = Image.open('E:\\Projects\\Program\\python\\Tkinter\\img\\1.png')
resized_img1 = img_1.resize((80, 50), Image.ANTIALIAS)
ph_1 = ImageTk.PhotoImage(resized_img1)
panel1 = tk.Label(root, image = ph_1)

img_2 = Image.open('E:\\Projects\\Program\\python\\Tkinter\\img\\2.png')
resized_img2 = img_2.resize((80, 50), Image.ANTIALIAS)
ph_2 = ImageTk.PhotoImage(resized_img2)
panel2 = tk.Label(root, image = ph_2)

img_3 = Image.open('E:\\Projects\\Program\\python\\Tkinter\\img\\4.png')
resized_img3 = img_3.resize((80, 50), Image.ANTIALIAS)
ph_3 = ImageTk.PhotoImage(resized_img3)
panel3 = tk.Label(root, image = ph_3)

i = 0
def placeImage():
    global i
    i+=1
    if i==1:  
        panel1.place(x=110,y=20)
        panel2.place(x=210,y=150)
        panel3.place(x=20,y=140)
    if i==2:
        panel3.place(x=110,y=20)
        panel1.place(x=210,y=150)
        panel2.place(x=20,y=140)
    if i==3:
        i=0
        panel2.place(x=110,y=20)
        panel3.place(x=210,y=150)
        panel1.place(x=20,y=140)


btn = tk.Button(text="Change",
            background="#5a1e24",
            foreground="#FFF",
            padx="20",
            pady="8",
            )           
btn.bind("<Button-1>", lambda event: placeImage() )

btn.place(x=100, y=250)

root.mainloop()

