from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Details for Face Recognition Model Using Python")

        #============= Variables ============
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_sec = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_mob = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # first image
        img = Image.open(r"img\girl.jpeg")
        img = img.resize((343, 80), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=343, height=80)

        # second image
        img2 = Image.open(r"img\facialrecognition.png")
        img2 = img2.resize((690, 80), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=343, y=0, width=690, height=80)

        # third image
        img3 = Image.open(r"img\clg.jpg")
        img3 = img3.resize((343, 80), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        first_label = Label(self.root, image=self.photoimg3)
        first_label.place(x=1010, y=0, width=343, height=80)

        #back-ground img
        img4 = Image.open(r"img\bg1.jpg")
        img4 = img4.resize((1366, 685), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=80, width=1366, height=685)


        title_label = Label(bg_img, text=" \"STUDENT MANAGEMENT SYSTEM\"", font=("times new roman", 24, "bold"), bg="white", fg="Dark blue")
        title_label.place(x=0, y=0, width=1366, height=55)

        #main frame
        main_frame=Frame( bg_img, bd=2, bg="white" )
        main_frame.place(x=12,y=60,width=1330,height=550)


        #left label frame
         #Student details
        Left_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=5,width=645,height=535)

        #Student Details img
        img_left = Image.open(r"img\smart-attendance.jpg")
        img_left = img_left.resize((330, 200), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label = Label(Left_frame, image=self.photoimg_left)
        first_label.place(x=130, y=0, width=330, height=200)

        #current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current course information",
                                font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=100, width=630, height=110)

        #Department
        dept_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=0,column=0,padx=10,sticky=W)

        dept_combo_box=ttk.Combobox(current_course_frame, textvariable=self.var_dept,font=("times new roman",12,"bold"),state="read only",width=17)
        dept_combo_box["values"]=("Select Department","Computer","IT","Mechanical","Civil","Automobile")
        dept_combo_box.current(0)
        dept_combo_box.grid(row=0,column=1,padx=2,pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo_box = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="read only",
                                      width=17)
        course_combo_box["values"] = ("Select Course", "FE", "SE", "TE", "BE","B.TECH")
        course_combo_box.current(0)
        course_combo_box.grid(row=0, column=3, padx=2, pady=10 ,sticky=W)

        #Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo_box = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), state="read only",
                                        width=17)
        year_combo_box["values"] = ("Select Year", "2020-2021", "2021-22", "2022-23", "2023-24")
        year_combo_box.current(0)
        year_combo_box.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo_box = ttk.Combobox(current_course_frame,textvariable=self.var_sem, font=("times new roman", 12, "bold"), state="read only",
                                      width=17)
        semester_combo_box["values"] = ("Select Semester", "1", "2", "3", "4","5","6","7","8")
        semester_combo_box.current(0)
        semester_combo_box.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #Class Student information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student information",
                                font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=215, width=630, height=290)

        #student id
        studentID_label = Label(class_student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0, column=1 , padx=10, pady=5, sticky=W)

        # student name
        studentName_label = Label(class_student_frame, text="Student Name", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        # Class Section
        class_sec_label = Label(class_student_frame, text="Class Section", font=("times new roman", 12, "bold"), bg="white")
        class_sec_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)


        sec_combo_box = ttk.Combobox(class_student_frame, textvariable=self.var_sec,
                                        font=("times new roman", 12, "bold"), state="read only",
                                        width=17)
        sec_combo_box["values"] = (" A", "B", "C", "D", "E", "F")
        sec_combo_box.current(0)
        sec_combo_box.grid(row=1, column=1, padx=2, pady=5, sticky=W)

        # Roll No
        rollNo_label = Label(class_student_frame, text="Roll Number", font=("times new roman", 12, "bold"), bg="white")
        rollNo_label.grid(row=1, column=2, padx=10, pady=5,sticky=W)

        rollNo_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5,sticky=W)

        #Gender
        gender_label = Label(class_student_frame, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5,sticky=W)

        gender_combo_box = ttk.Combobox(class_student_frame, textvariable=self.var_gender,
                                        font=("times new roman", 12, "bold"), state="read only",
                                        width=17)
        gender_combo_box["values"] = ("Male", "Female", "Other")
        gender_combo_box.current(0)
        gender_combo_box.grid(row=2, column=1, padx=2, pady=5, sticky=W)

        # DOB
        DOB_label = Label(class_student_frame, text="Date of Birth", font=("times new roman", 12, "bold"), bg="white")
        DOB_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        DOB_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="E-mail", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Mobile Number
        mobile_number_label = Label(class_student_frame, text="Mobile Number", font=("times new roman", 12, "bold"), bg="white")
        mobile_number_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        mobile_number_entry = ttk.Entry(class_student_frame, textvariable=self.var_mob, width=20, font=("times new roman", 12, "bold"))
        mobile_number_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_name_label = Label(class_student_frame, text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
        teacher_name_label.grid(row=4, column=2, padx=10, pady=5,sticky=W)

        teacher_name_entry = ttk.Entry(class_student_frame ,textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Buttons
        self.var_radio1 = StringVar()
        radio_button1=ttk.Radiobutton(class_student_frame, variable= self.var_radio1, text="Take Photo Sample",value="Yes")
        radio_button1.grid(row=5, column=0)

        radio_button2 = ttk.Radiobutton(class_student_frame, variable= self.var_radio1, text="No Photo Sample", value="No")
        radio_button2.grid(row=5, column=1)

        # Buttons Frame
        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE, bg="white")
        button_frame.place(x=0,y=200,width=600,height=30)

        save_button=Button(button_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        save_button.grid(row=0,column=0)

        update_button = Button(button_frame, text="Update",command=self.update_data, width=15, font=("times new roman", 12, "bold"), bg="dark blue",
                             fg="white")
        update_button.grid(row=0, column=1)

        delete_button = Button(button_frame, text="Delete",command=self.delete_data, width=16, font=("times new roman", 12, "bold"), bg="dark blue",
                             fg="white")
        delete_button.grid(row=0, column=2)

        reset_button = Button(button_frame, text="Reset", command=self.reset_data, width=15, font=("times new roman", 12, "bold"), bg="dark blue",
                             fg="white")
        reset_button.grid(row=0, column=3)

        # button frame2
        button_frame2 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        button_frame2.place(x=0, y=230, width=600, height=30)

        take_photo_button = Button(button_frame2, text="Take Photo Sample",command=self.generate_dataset, width=33, font=("times new roman", 12, "bold"),
                              bg="black",
                              fg="white")
        take_photo_button.grid(row=1, column=0)

        update_photo_button = Button(button_frame2, text="Update Photo Sample", width=33,
                                   font=("times new roman", 12, "bold"),
                                   bg="black",
                                   fg="white")
        update_photo_button.grid(row=1, column=1)

        #right label frame
        Right_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=668,y=5,width=645,height=535)

        img_right = Image.open(r"img\student.jpg")
        img_right = img_right.resize((330, 100), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        first_label = Label(Right_frame, image=self.photoimg_right)
        first_label.place(x=130, y=0, width=330, height=100)

        #===========: Search System :================
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                         font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=100, width=630, height=90)

        #Search Label
        search_label= Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="white",fg="black")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo_box = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="read only",
                                      width=17)
        search_combo_box["values"] = ("Select", "Roll No", "Phone no")
        search_combo_box.current(0)
        search_combo_box.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0, column=2 , padx=10, pady=5, sticky=W)

        #Buttons:=
        search_button = Button(search_frame, text="Search", width=13, font=("times new roman", 10, "bold"),
                               bg="dark blue",
                               fg="white")
        search_button.grid(row=0, column=3,padx=4)

        show_all_button = Button(search_frame, text="Show All", width=13, font=("times new roman", 10, "bold"),
                              bg="dark blue",
                              fg="white")
        show_all_button.grid(row=0, column=4,padx=4)

        #========: Table Frame :=======
        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=195, width=630, height=310)

        scroll_x= ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","id","name","sec","roll","gender","dob","email","mob","address","teacher","photo"),xscrollcommand= scroll_x.set,yscrollcommand= scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("sec", text="Section")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("mob", text="Mobile No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")

        self.student_table["show"]="headings"

        self.student_table.column("dept", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("sec", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("mob", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #======== Function declaration ======
    def add_data(self):
        if self.var_dept.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Harsha989",
                                               database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                                    self.var_dept.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_sem.get(),
                                                                                                                    self.var_id.get(),
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_sec.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_mob.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get()
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}", parent=self.root)

    #=============: Fetch Data :==========
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Harsha989",
                                       database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()

    #===========: Get Cursor :===========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_sec.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_mob.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #=============: Update function :========
    def update_data(self):
        if self.var_dept.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                up_date=messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
                if up_date>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Harsha989",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dept=%s,course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Mobile_No=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",(

                                                                                                                                                                                                                        self.var_dept.get(),
                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                                        self.var_sec.get(),
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_mob.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_id.get()
                                                                                                                                                                                                                    ))
                else:
                    if not up_date:
                        return
                messagebox.showinfo("Success","Student's detail successfully updated ",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to Delete this Student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Harsha989",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted Student Details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    #reset
    def reset_data(self):
        self.var_dept.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_sec.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


    #============: Generate data set or Take photo Samples :=======
    def generate_dataset(self):
        if self.var_dept.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Harsha989",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dept=%s,course=%s,Year=%s,Semester=%s,Name=%s,Section=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Mobile_No=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s", (

                                                                                                                                                                                                                            self.var_dept.get(),
                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                            self.var_sem.get(),
                                                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                                                            self.var_sec.get(),
                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                            self.var_mob.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                            self.var_id.get()==id+1

                                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #======: Load predefined data on face frontals from openCv :==========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray, 1.5, 5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                capture=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                img_id=0
                while True:
                    ret,my_frame=capture.read()
                    if face_cropped(my_frame) is not None:
                        img_id +=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0, 255, 0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent =self.root)

        

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()