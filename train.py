from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root, text=" TRAIN DATA SET", font=("verdana", 24, "bold"), bg="white", fg="Dark red")
        title_label.place(x=0, y=0, width=1366, height=55)

        img_top = Image.open(r"img\facialrecognition.png")
        img_top = img_top.resize((1366, 250), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=1366, height=250)

        # button
        b1_1 = Button(self.root, text="TRAIN DATA",command=self.train_classifier, cursor="hand2", font=("verdana", 26, "bold"), bg="black", fg="white")
        b1_1.place(x=0, y=280, width=1366, height=80)

        img_bottom = Image.open(r"img\FACE.jpg")
        img_bottom = img_bottom.resize((1366, 350), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        first_label = Label(self.root, image=self.photoimg_bottom)
        first_label.place(x=0, y=355, width=1366, height=350)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img =Image.open(image).convert('L') #Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #========: Train the classifier and SAVE :===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Sets Completed!!")



if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()