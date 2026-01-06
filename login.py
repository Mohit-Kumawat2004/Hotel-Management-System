from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox 
import random
import time
import datetime
from datetime import datetime
import mysql.connector
import re
from hotel import HotelManagementSystem
from customer import Cust_Win
from room import RoomBooking
from details import DetailsRoom
from report import ReportRoom



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=223)

        self.txtpass=ttk.Entry(frame,font=("times new roman",20,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)

        # ======icon image==========
        img2=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\LoginIconAppl.png")
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)


        img3=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\kir.png")
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)

        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #register button
        registerbtn=Button(frame,text="New User Register",command=self.register_link_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #forget password button
        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=370,width=160)



    def register_link_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()==""or self.txtpass.get()=="":
            messagebox.showerror("ERROR","All Field Required")
        elif self.txtuser.get()=="aman" and self.txtpass.get()=="008":
            messagebox.showinfo("Success","Welcome To Our Hotel")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                           self.txtuser.get(), 
                                                           self.txtpass.get()
                ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Errrorrr","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select Security Question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please Enter the Answer", parent=self.root2)
        elif self.txt_newpassword.get() == "":
            messagebox.showerror("Error", "Please Enter the New Password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="management")
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s AND SecurityQ=%s AND SecurityA=%s"
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please Enter Correct Answer", parent=self.root2)
            else:
                query = "UPDATE register SET password=%s WHERE email=%s"
                value = (self.txt_newpassword.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Information", "Your Password has been Reset Successfully, Please Login with New Password", parent=self.root2)

                
            
            

#=======================================Forgot Password Window========================================#
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email address to reset the password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="admin",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please Enter the valid User Name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password Window")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password Window",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                #Row3====================
                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"))
                self.combo_security_Q["values"]=("Select","Your Favourite Movie","Your Pet Name","Your Favourite Game","Your Favourite Rifle Name","Your Dream Company Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answers",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=170)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=200,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=260)

                self.txt_newpassword=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpassword.place(x=50,y=290,width=250)


                btn=Button(self.root2,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green",command=self.reset_pass)
                btn.place(x=120,y=350)


                



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #===================Variables============================#
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

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15),show="*")
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



class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #================1st_Image========================#
        img1=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\hotel1.png")
        img1=img1.resize((1550,140), Image.Resampling.LANCZOS) #convert high level to low level
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #=================LOGO==========================#
        img2=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\logohotel.png")
        img2=img2.resize((230,140),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        #==================TITLE==========================#
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM", font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #=====================IN_FRAME===================#
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)



        # Add time and date labels
        self.time_label = Label(self.root, font=("times new roman", 17, "bold"), bg="black", fg="gold")
        self.time_label.place(x=10, y=150)
        self.date_label = Label(self.root, font=("times new roman", 17, "bold"), bg="black", fg="gold")
        self.date_label.place(x=1320, y=150)

        self.update_time()
        self.update_date()
 

        #=======================MENU=====================#
        lbl_menu=Label(main_frame,text="MENU", font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #=====================BUTTON_ FRAME==============#
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.room_booking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="IMAGES",command=self.report_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)
        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        #======RIGHT_SIDE_IMAGE============#
        img3=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\slide3.jpg")
        img3=img3.resize((1310,590),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)


        #================DOWN_SIDE_1==========================#
        img4=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\myh.jpg")
        img4=img4.resize((230,210),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)

        #================DOWN_SIDE_2==========================#
        img5=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\khana.jpg")
        img5=img5.resize((230,190),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def room_booking(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def report_room(self):
        self.new_window=Toplevel(self.root)
        self.app=ReportRoom(self.new_window)


    def update_time(self):
        # Update the time every 1000 milliseconds (1 second)
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

    def update_date(self):
        # Update the date once
        current_date = datetime.now().strftime("%B %d, %Y")
        self.date_label.config(text=current_date)

    
    def logout(self):
        self.root.destroy()
        




if __name__ == "__main__":
    main()
















    
