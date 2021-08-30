from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Model Using Python")

        title_label = Label(self.root, text="HELP DESK", font=("verdana", 32, "bold"), bg="white", fg="brown")
        title_label.place(x=0, y=0, width=1366, height=55)

        img_top = Image.open(r"img\uit-rgpv-campus.jpg")
        img_top = img_top.resize((1366, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=1366, height=720)

        # Developer info
        help_label = Label(first_label, text="Email: mohit.vijayvargiya27@gmail.com , harshakaithal@gmail.com", font=("sans-serif", 28, "bold"), bg="white", fg="dark red")
        help_label.place(x=343, y=0)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()