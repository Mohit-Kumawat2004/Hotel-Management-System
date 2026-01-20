from tkinter import*
import re
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #===================Variables======================--======#
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_SecurityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()




        #====================Bg Image============================#
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\regiborder.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        
        #================Bg Image============================#
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\thought-good-morning-messages-LoveSove.jpg")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=100,y=100,width=470,height=570)


        #============================Main Frame==================================#
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=570)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        #================================Label and Entry===============================#
        #Row1==============
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #Row2====================
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #Row3====================
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_SecurityQ,font=("times new roman",15,"bold"))
        self.combo_security_Q["values"]=("Select","Your Favourite Movie","Your Pet Name","Your Favourite Game","Your Favourite Rifle Name","Your Dream Company Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answers",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)


        #Row4====================
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)


        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        #Check Button===========================#
        self.var_check=IntVar()                                                                                 #because of offvalue and onvalue
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)


        #===================Image Buttons=============================#
        img=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\register-now-button1.jpg")
        img=img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=60,y=448,width=200)


        img1=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\loginpng.png")
        img1=img1.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"))
        b1.place(x=390,y=448,width=200)




#=====================================Functions__Declarations======================================#

    def  register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_SecurityQ.get()=="Select":
            messagebox.showerror("Error","All Fields are Required !!!!!")
        elif self.var_check.get()==0:
            messagebox.showerror("Errror","Please agree to our terms and conditions")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error", "Password && Confirm Password Must Be Same")
        elif not self.var_email.get().endswith('@gmail.com'):
            messagebox.showerror("Error", "Email must end with @gmail.com")
        elif not (self.var_fname.get().isalpha() and self.var_lname.get().isalpha()):
            messagebox.showerror("Error", "First name and Last name must contain only alphabetic characters")
        elif not (self.var_contact.get().isdigit() and len(self.var_contact.get()) == 10):
            messagebox.showerror("Error", "Contact number must be exactly 10 digits")
        elif not self.is_valid_password(self.var_pass.get()):
            messagebox.showerror("Error",
                                 "Password must be between 8 and 120 characters long, contain at least one special symbol (@, #, $, &, *, !, %, ^), at least two numeric values, and at least one letter.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already Exists, Please try another Email")
            else:
                my_cursor.execute("insert into register values (%s,%s,%s,%s,%s,%s,%s)",(
                                                                    self.var_fname.get(),
                                                                    self.var_lname.get(),
                                                                    self.var_contact.get(),
                                                                    self.var_email.get(),
                                                                    self.var_SecurityQ.get(),
                                                                    self.var_SecurityA.get(),
                                                                    self.var_pass.get()
            
                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")



    def is_valid_password(self, password):
        # Password must be between 8 and 120 characters
        if not (8 <= len(password) <= 120):
            return False
        # Check for at least one special symbol
        special_symbols = '@#$&*!%/^'
        if not any(char in special_symbols for char in password):
            return False
        # Check for at least two numeric values
        if len(re.findall(r'\d', password)) < 2:
            return False
        # Check for at least one alphabetical character
        if not any(char.isalpha() for char in password):
            return False
        return True





        

if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
