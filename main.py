from tkinter import*
from tkinter import ttk #used for GUI and ttk has good GUI toolkits
from PIL import Image,ImageTk #  to work on images called pillow #image TK for image cropping


#Set up the main page the size of the window according to your interface
class Face_recognition_system:
    def __init__(self,root): #root is the default name of the main screen
        self.root=root
        self.root.geometry("1275x650+0+0")  
        self.root.title("Face Recognition Attendence System")
        
        #import images from the folder
        img = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\Stanford.jpg")
        img=img.resize((425,110),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl =Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=425,height=110)

        #Second Image
        img2 = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\facialrecognition.png")
        img2=img2.resize((425,110),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl =Label(self.root,image=self.photoimg2)
        f_lbl.place(x=425,y=0,width=425,height=110)
        
        #Third Image
        img3 = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\u.jpg")
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

        title_lbl=Label(bg_img,text="Face Recognition Attendence System Software",font=("times new roman",26,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1275,height=45)
        
        #getting all the buttons of the first page
        #student button
        stdimg = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\std.jpg")
        stdimg=stdimg.resize((140,140),Image.ANTIALIAS)
        self.stdimage=ImageTk.PhotoImage(stdimg)
        
        std_btn=Button(bg_img,image=self.stdimage,cursor="hand2")
        std_btn.place(x=140,y=100,width=140,height=140)
        std_btn_text=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        std_btn_text.place(x=140,y=240,width=140,height=40)
        
        #detect face button
        face_detector_img = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\face_detector1.jpg")
        face_detector_img=face_detector_img.resize((140,140),Image.ANTIALIAS)
        self.face_detector_image=ImageTk.PhotoImage(face_detector_img)
        
        face_detector__btn=Button(bg_img,image=self.face_detector_image,cursor="hand2")
        face_detector__btn.place(x=420,y=100,width=140,height=140)
        face_detector__btn_text=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        face_detector__btn_text.place(x=420,y=240,width=140,height=40)
        
        #Attendance button
        atd_img = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\report.jpg")
        atd_img=atd_img.resize((140,140),Image.ANTIALIAS)
        self.atd_image=ImageTk.PhotoImage(atd_img)
        
        atd__btn=Button(bg_img,image=self.atd_image,cursor="hand2")
        atd__btn.place(x=700,y=100,width=140,height=140)
        atd__btn_text=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        atd__btn_text.place(x=700,y=240,width=140,height=40)
        
        #help button
        help_img = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\help.jpg")
        help_img=help_img.resize((140,140),Image.ANTIALIAS)
        self.help_image=ImageTk.PhotoImage(help_img)
        
        help__btn=Button(bg_img,image=self.help_image,cursor="hand2")
        help__btn.place(x=980,y=100,width=140,height=140)
        help__btn_text=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        help__btn_text.place(x=980,y=240,width=140,height=40)

        #train button
        train_img = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\train.png")
        train_img=train_img.resize((140,140),Image.ANTIALIAS)
        self.train_image=ImageTk.PhotoImage(train_img)
        
        train__btn=Button(bg_img,image=self.train_image,cursor="hand2")
        train__btn.place(x=140,y=300,width=140,height=140)
        train__btn_text=Button(bg_img,text=" Train Data",cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        train__btn_text.place(x=140,y=440,width=140,height=40)
        
        #photo button
        photo_img = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\photo.jpg")
        photo_img=photo_img.resize((140,140),Image.ANTIALIAS)
        self.photo_image=ImageTk.PhotoImage(photo_img)
        
        photo__btn=Button(bg_img,image=self.photo_image,cursor="hand2")
        photo__btn.place(x=420,y=300,width=140,height=140)
        photo__btn_text=Button(bg_img,text="Photographs",cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        photo__btn_text.place(x=420,y=440,width=140,height=40)
        
        #developer button
        developer_img = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\developer.jpg")
        developer_img=developer_img.resize((140,140),Image.ANTIALIAS)
        self.developer_image=ImageTk.PhotoImage(developer_img)
        
        developer__btn=Button(bg_img,image=self.developer_image,cursor="hand2")
        developer__btn.place(x=700,y=300,width=140,height=140)
        developer__btn_text=Button(bg_img,text="developer",cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        developer__btn_text.place(x=700,y=440,width=140,height=40)
        
        #exit button
        exit_img = Image.open(r"C:\Users\MIN\Documents\Face Recognition Attendence System\Main Page Images\exit.jpg")
        exit_img=exit_img.resize((140,140),Image.ANTIALIAS)
        self.exit_image=ImageTk.PhotoImage(exit_img)
        
        exit__btn=Button(bg_img,image=self.exit_image,cursor="hand2")
        exit__btn.place(x=980,y=300,width=140,height=140)
        exit__btn_text=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",14,"bold"),bg="blue",fg="white")
        exit__btn_text.place(x=980,y=440,width=140,height=40)
        

#calling the main screen
if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_system(root) #connecting it to root
    root.mainloop()