from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_label = Label(self.root, text="FACE RECOGNITION", font=("sans-serif", 30, "bold"), bg="white", fg="Dark blue")
        title_label.place(x=0, y=0, width=1366, height=55)

        #1st image
        img_top = Image.open(r"img\face_detector1.jpg")
        img_top = img_top.resize((683, 650), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label = Label(self.root, image=self.photoimg_top)
        first_label.place(x=0, y=55, width=683, height=650)

        #2nd image
        img_bottom = Image.open(r"img\2.jpg")
        img_bottom = img_bottom.resize((683, 650), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        first_label = Label(self.root, image=self.photoimg_bottom)
        first_label.place(x=683, y=55, width=683, height=650)

        # button
        b1_1 = Button(self.root, text="Face Recognition", cursor="hand2",command=self.face_recogn, font=("verdana", 14, "italic"), bg="black", fg="light blue")
        b1_1.place(x=900, y=600, width=250, height=80)

    #=======:  Attendance  :=======
    def mark_attendance(self,i,r,n,d):
        with open("face_model_attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_List=[]
            for line in myDataList:
                entry = line.split((","))
                name_List.append(entry[0])
            if((i not in name_List) and (r not in name_List) and (n not in name_List) and (d not in name_List)):
                now=datetime.now()
                d1=now.strftime("%d-%m-%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    #=====: Face Recognition :====
    def face_recogn(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            co_ordinate=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
                id,predict=clf.predict(gray_image[y:y+h, x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Harsha989",database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_ID=" +str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_ID=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dept from student where Student_ID=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_ID from student where Student_ID=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                
            #color co-ordinate---dark red=(0,0,128);dark blue=(128,0,0);black=(0,0,0)

                if confidence>77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 128), 2)
                    cv2.putText(img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 128), 2)
                    cv2.putText(img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 128), 2)
                    cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)

                co_ordinate=[x,y,w,h]

            return co_ordinate

        def recognize(img, clf, faceCascade):
            co_ordinate = draw_boundary(img,faceCascade,1.3, 5,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture=cv2.VideoCapture(0)

        while True:
            ret,img=video_capture.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            c =cv2.waitKey(2000)
            if c == 13: #press esc to go out of window
               break
            video_capture.release()
            cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
