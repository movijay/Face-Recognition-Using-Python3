import tkinter.messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System_Using_Python:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Model Using Python")

        #first image
        img = Image.open(r"C:\Users\Mohit Vijayvargiya\Desktop\FACE-RECOGN\img\RGPV.jpg")
        img = img.resize((310, 132), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=310, height=132)

        # second image
        img2=Image.open(r"img\uit-logo-img.png")
        img2=img2.resize((1180,132),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        first_label=Label(self.root,image=self.photoimg2)
        first_label.place(x=310,y=0,width=1180,height=132)

        #back-ground img
        img3 = Image.open(r"img\bg1.jpg")
        img3= img3.resize((1366, 550), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=132, width=1366, height=550)



        title_label = Label(bg_img, text="\"FACE RECOGNITION MODEL USING PYTHON\"",
                            font=("times new roman", 28, "bold"), bg="white", fg="black")
        title_label.place(x=0, y=0, width=1366, height=70)

        title_label = Label(bg_img, text=" FACIAL RECOGNITION ATTENDANCE SYSTEM ",
                            font=("times new roman",20, "bold"), bg="black", fg="white")
        title_label.place(x=0, y=70, width=1366, height=55)

        #time
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl = Label(title_label, font = ("times new roman",16,"bold"),bg="white",fg="dark blue")
        lbl.place(x=0, y=0, width=130, height=50)
        time()

        #student button
        img4 = Image.open(r"img\smart-attendance.jpg")
        img4= img4.resize((180, 180), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4, command= self.student_details ,cursor="hand2")
        b1.place(x=190,y=128,width=180,height=180)

        b1_1=Button(bg_img,text="Student Details", command= self.student_details ,cursor="hand2",font=("arial", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=190,y=280,width=180,height=40)

        #detect_face button
        img5 = Image.open(r"img\face_detector1.jpg")
        img5 = img5.resize((180, 180), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=490,y=128,width=180,height=180)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("arial", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=490,y=280,width=180,height=40)


        #attendance button
        img6 = Image.open(r"img\attendance.jpg")
        img6 = img6.resize((180, 180), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2", command = self.attendance_data)
        b1.place(x=790,y=128,width=180,height=180)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2", command = self.attendance_data, font=("arial", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=790,y=280,width=180,height=40)

        #Help Desk
        img7 = Image.open(r"img\help.jpg")
        img7= img7.resize((180, 180), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1090,y=128,width=180,height=180)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("arial", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=1090,y=280,width=180,height=40)

        #train face button
        img8 = Image.open(r"img\di.jpg")
        img8= img8.resize((180, 180), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=190,y=348,width=180,height=180)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("arial", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=190,y=500,width=180,height=40)


        #Photos-face button
        img9 = Image.open(r"img\dev.jpg")
        img9= img9.resize((180, 180), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=490,y=348,width=180,height=180)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("arial", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=490,y=500,width=180,height=40)


        #Developer-face button
        img10 = Image.open(r"img\detect_face.png")
        img10= img10.resize((180, 180), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=790,y=348,width=180,height=180)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data, font=("arial", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=790,y=500,width=180,height=40)

        # Exit-face button
        img11 = Image.open(r"img\exit.jpg")
        img11 = img11.resize((180, 180), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command= self.exit)
        b1.place(x=1090, y=348, width=180, height=180)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command= self.exit ,font=("arial", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=1090, y=500, width=180, height=40)

    def open_img(self):
        os.startfile("data")

    def exit(self):
            self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project")
            if self.exit>0:
                self.root.destroy()
            else:
                return

    #================: Function buttons :=================

    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)

    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendance(self.new_window)

    def developer_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Developer(self.new_window)

    def help_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Help(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System_Using_Python(root)
    root.mainloop()