import tkinter as tk
from PIL import ImageTk, Image
import random

class Parametrs:
    def __init__(self):   
        self.xpos = random.randint(0, 254)
        self.ypos = random.randint(0, 310)
        self.xspeed = random.randint(1, 5)
        self.yspeed = random.randint(1, 5)

class Image(tk.Canvas):
    def image(self):
        self.img_1 = Image.open('E:\\Projects\\Program\\python\\Tkinter\\img\\1.png')
        self.resized_img1 = img_1.resize((90, 70), Image.ANTIALIAS)
        self.ph_1 = ImageTk.PhotoImage(resized_img1)
        self.panel1 = tk.Label(root, image = ph_1)

        self.img_2 = Image.open('E:\\Projects\\Program\\python\\Tkinter\\img\\2.png')
        self.resized_img2 = img_2.resize((90, 70), Image.ANTIALIAS)
        self.ph_2 = ImageTk.PhotoImage(resized_img2)
        self.panel2 = tk.Label(root, image = ph_2)

        self.img_3 = Image.open('E:\\Projects\\Program\\python\\Tkinter\\img\\4.png')
        self.resized_img3 = img_3.resize((90, 70), Image.ANTIALIAS)
        self.ph_3 = ImageTk.PhotoImage(resized_img3)
        self.panel3 = tk.Label(root, image = ph_3)

    def __init__(self, master):
        self.images = []
        self.im = [] 
        for _ in range(25):
            img = Parametrs()
            self.images.append(img)
            self.im.append(self.image)
        self.run()

    def run(self):
        for i, picture  in zip(self.im, self.images):
            self.move(i, picture.xspeed, picture.yspeed)
            pos = self.coords(i)
            if pos[3] >= 310 or pos[1] <= 0:
                picture.yspeed = - picture.yspeed
            if pos[2] >= 254 or pos[0] <= 0:
                picture.xspeed = - picture.xspeed
        self.after(10, self.run)

    def placeImage():
        global c
        c+=1
        if c==1:
            
            panel1.place(x=110,y=20)

            panel2.place(x=210,y=150)

            panel3.place(x=20,y=140)

        if c==2:

            panel3.place(x=110,y=20)

            panel1.place(x=210,y=150)

            panel2.place(x=20,y=140)

        if c==3:
            c=0

            panel2.place(x=110,y=20)

            panel3.place(x=210,y=150)

            panel1.place(x=20,y=140)


    btn = tk.Button(text="Change",
                background="#5a1e24",
                foreground="#FFF",
                padx="20",
                pady="8",
                font="16"
                )           
    btn.bind("<Button-1>", lambda event: placeImage() )

    btn.place(x=100, y=250)

if __name__ == '__main__':

    root = tk.Tk()

    root.title("HomeWork")
    root.geometry("300x300")
    root['bg'] = "gray22"
    root.resizable(False, False)
    c = Image(root)

    root.mainloop()
