from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Model Using Python")

        title_label = Label(self.root, text="DEVELOPER", font=("verdana", 28, "bold"), bg="white", fg="Dark blue")
        title_label.place(x=0, y=0, width=1366, height=55)

        img_top = Image.open(r"img\dev.jpg")
        img_top = img_top.resize((1366, 720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=1366, height=720)

        # main frame
        main_frame = Frame(first_label, bd=2, bg="white")
        main_frame.place(x=930, y=0, width=421, height=520)

        img_top1 = Image.open(r"img\RGPV.jpg")
        img_top1 = img_top1.resize((370, 260), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        first_label = Label(main_frame, image=self.photoimg_top1)
        first_label.place(x=28, y=250, width=370, height=260)

        #Developer info
        dept_label=Label(main_frame,text="Hey there, Thanks for showing \n your interest and building \n your trust upon us \n Developer credit goes to:\n \"HARSHA KAITHAL\" \n and \n \"MOHIT VIJAYVARGIYA\"",font=("arial",20,"bold"),bg="light blue",fg="black")
        dept_label.place(x=0,y=0)


if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()