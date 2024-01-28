from tkinter import*
from tkinter import ttk #used for GUI and ttk has good GUI toolkits
from PIL import Image,ImageTk #  to work on images called pillow #image TK for image cropping


#Set up the main page the size of the window according to your interface
class student_details:
    def __init__(self,root): #root is the default name of the main screen
        self.root=root
        self.root.geometry("1275x650+0+0")  
        self.root.title("Face Recognition Attendence System")



 #import images from the folder
        img = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\uni.jpg")
        img=img.resize((425,110),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl =Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=425,height=110)

        #Second Image
        img2 = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\1.png")
        img2=img2.resize((425,110),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl =Label(self.root,image=self.photoimg2)
        f_lbl.place(x=425,y=0,width=425,height=110)
        
        #Third Image
        img3 = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\uni2.jpg")
        img3=img3.resize((425,110),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl =Label(self.root,image=self.photoimg3)
        f_lbl.place(x=850,y=0,width=425,height=110)

        #background Image
        bgimg = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\bg.jpg")
        bgimg=bgimg.resize((1275,650),Image.ANTIALIAS)
        self.photoimg_bg=ImageTk.PhotoImage(bgimg)
        
        bg_img =Label(self.root,image=self.photoimg_bg)
        bg_img.place(x=0,y=110,width=1275,height=650)
        
        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",26,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1275,height=45)
        
        #to make frame
        main_frame=Frame(bg_img,bd=4,bg="white")
        main_frame.place(x=10,y=50,width=1250,height=485)

        #left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=600,height=465)
        
        #course info frame
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=0,width=590,height=130)
        
        #labeling
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0)
        
        #combobox
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer Scince","IT","Maths")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        dep_label=Label(current_course_frame,text="Course:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=2)
        
        
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Course","IT","CS","BI","SE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #year
        dep_label=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=0)
        
        
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Year","2016-20","2017-21","2018-22","2019-23","2020-24")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester
        dep_label=Label(current_course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2)
        
        
        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #course info frame
        class_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_frame.place(x=5,y=130,width=590,height=310)
        
        #Student ID
        student_id_label=Label(class_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5)
        
        student_id_entry=ttk.Entry(class_frame,width=18,font=("times new roman",12))
        student_id_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        #Student name
        student_name_label=Label(class_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5)
        
        student_name_entry=ttk.Entry(class_frame,width=18,font=("times new roman",12))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        #Section
        section_label=Label(class_frame,text="Section:",font=("times new roman",12,"bold"),bg="white")
        section_label.grid(row=1,column=0,padx=5,pady=5)
        
        section_entry=ttk.Entry(class_frame,width=18,font=("times new roman",12))
        section_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        #Ag No.
        ag_label=Label(class_frame,text="Ag. No.:",font=("times new roman",12,"bold"),bg="white")
        ag_label.grid(row=1,column=2,padx=5,pady=5)
        
        ag_entry=ttk.Entry(class_frame,width=18,font=("times new roman",12))
        ag_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        #Gender
        gender_label=Label(class_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=5,pady=5)
        
        gender_entry=ttk.Entry(class_frame,width=18,font=("times new roman",12))
        gender_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        
        #date of birth
        dob_label=Label(class_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=5,pady=5)
        
        dob_entry=ttk.Entry(class_frame,width=18,font=("times new roman",12))
        dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)
        
        #email
        email_label=Label(class_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=5,pady=5)
        
        email_entry=ttk.Entry(class_frame,width=18,font=("times new roman",12))
        email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        
        #Phone Number
        phone_number_label=Label(class_frame,text="Phone Number:",font=("times new roman",12,"bold"),bg="white")
        phone_number_label.grid(row=3,column=2,padx=5,pady=5)
        
        phone_number_entry=ttk.Entry(class_frame,width=18,font=("times new roman",12))
        phone_number_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)
        
        #Address
        address_label=Label(class_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=5,pady=5)
        
        address_entry=ttk.Entry(class_frame,width=18,font=("times new roman",12))
        address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)
        
        #Teacher Name
        techer_label=Label(class_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        techer_label.grid(row=4,column=2,padx=5,pady=5)
        
        techer_entry=ttk.Entry(class_frame,width=18,font=("times new roman",12))
        techer_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)
        
        #radio buttons
        radiobtn1=ttk.Radiobutton(class_frame,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5)
        
        radiobtn2=ttk.Radiobutton(class_frame,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1,padx=5,pady=5)
        
        #btnframe
        btnframe=Frame(class_frame,bd=1,relief=RIDGE,bg="white")
        btnframe.place(x=5,y=200,width=573,height=35)
        
        save_btn=Button(btnframe,text="Save",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        update_btn=Button(btnframe,text="Update",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        delete_btn=Button(btnframe,text="Delete",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        reset_btn=Button(btnframe,text="Reset",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        #btnframe2
        btnframe2=Frame(class_frame,bd=1,relief=RIDGE,bg="white")
        btnframe2.place(x=5,y=235,width=573,height=35)
        take_photo_btn=Button(btnframe2,text="Take Photo",width=31,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        update_photo_btn=Button(btnframe2,text="Update Photo",width=30,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        #right frame
        right_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=630,y=10,width=610,height=465)
        
        #==========search system=============
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=0,width=590,height=70)
        #search
        search_label=Label(search_frame,text="Search",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        search_combo["values"]=("Select","roll_number","ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=18,font=("times new roman",12))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)
        show_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        show_btn.grid(row=0,column=4)
        
        #==========table frame=============
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=75,width=590,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Section")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        


#calling the main screen
if __name__ == "__main__":
    root=Tk()
    obj=student_details(root) #connecting it to root
    root.mainloop()