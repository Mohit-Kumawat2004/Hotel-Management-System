from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from room import RoomBooking
from details import DetailsRoom
from report import ReportRoom
from datetime import datetime  


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
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
