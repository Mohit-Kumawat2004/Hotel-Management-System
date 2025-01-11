from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
    
        #==========Variables for Mysql Tables===========#
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofday=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        #=====================================================TITLE==============================================#
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #=================================LOGO==================================================================#
        img2=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\logohotel.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        #=======================================LABEL_FRAME============================================#
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #=======================================LABELS_AND_ENTRY=======================================#
        #Customer Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=20)
        enty_contact.grid(row=0,column=1,sticky=W)


        #Fetch Small Button=============================================#
        btnFetchData=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data:",font=("arial",9,"bold"),bg="black",fg="gold",width=9)    #small fetch add button
        btnFetchData.place(x=347,y=5)

        #Check in Date==========================================================#
        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_in Date: ",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        #Check out Date========================================================#
        lbl_Check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check_Out Date: ",padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txt_Check_out.grid(row=2,column=1)


#================================Room Booking Type==========================================================#
        label_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type: ",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide=my_cursor.fetchall()
        
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)


#==================================Available Room==============================================================#
        lblRoomAvailable=Label(labelframeleft,font=("arial",12,"bold"),text="Available Room: ",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        #txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        #txtRoomAvailable.grid(row=4,column=1)


        conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()
        
        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)


#============================================Meal==============================================================#
        lblMeal=Label(labelframeleft,font=("arial",12,"bold"),text="Meal: ",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)


        #NoOfdays==============================================================#
        lblNoOfdays=Label(labelframeleft,font=("arial",12,"bold"),text="No Of Days: ",padx=2,pady=6)
        lblNoOfdays.grid(row=6,column=0,sticky=W)
        txtNoOfdays=ttk.Entry(labelframeleft,textvariable=self.var_noofday,font=("arial",13,"bold"),width=29)
        txtNoOfdays.grid(row=6,column=1)


        #Paid tax==============================================================#
        lblNoOfdays=Label(labelframeleft,font=("arial",12,"bold"),text="No Of Days: ",padx=2,pady=6)
        lblNoOfdays.grid(row=7,column=0,sticky=W)
        txtNoOfdays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtNoOfdays.grid(row=7,column=1)


        #Sub Total==============================================================#
        lblNoOfdays=Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total: ",padx=2,pady=6)
        lblNoOfdays.grid(row=8,column=0,sticky=W)
        txtNoOfdays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("arial",13,"bold"),width=29)
        txtNoOfdays.grid(row=8,column=1)


        #Final and total Cost==============================================================#
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost: ",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        lblIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        lblIdNumber.grid(row=9,column=1)


        #============Bill Button===========================================================#
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=10)    #add button
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        #=====================================BUTTONS FOR ROOMS=====================================#
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)    #add button
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)     #update button
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.Delete_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)     #delete button
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)         #reset button
        btnReset.grid(row=0,column=3,padx=1)


        #=================Right Side Image==========================#
        img3=Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\bed.jpg")
        img3=img3.resize((520,300),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=769,y=55,width=520,height=230)


        #=====================================Table Frame Search System=====================================#
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By: ",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)


        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1)


        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        #=============================Buttons For Searching Data====================================#
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)



        #=======================Showing Tables Data========================#
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)  #scroll bar creation horizontal
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)        #scroll bar creation vertically

        self.room_table=ttk.Treeview(details_table,column=("Contact","Checkin","CheckOut","RoomType","RoomAvailable","Meal",
                                            "NoOfDays"),xscrollcommand=scroll_x.set,
                                             yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)    #movements for scrollbar
        scroll_y.config(command=self.room_table.yview)      #movements for scrollbar


        #=====================Table Creations===================================#
        self.room_table.heading("Contact",text="Contact")
        self.room_table.heading("Checkin",text="Check-in")
        self.room_table.heading("CheckOut",text="Check-Out")
        self.room_table.heading("RoomType",text="Room Type")
        self.room_table.heading("RoomAvailable",text="RoomAvailable")
        self.room_table.heading("Meal",text="Meal")
        self.room_table.heading("NoOfDays",text="NoOfDays")

        self.room_table["show"]="headings"
        [self.room_table.column(column, width=100) for column in ["Contact", "Checkin", "CheckOut", "RoomType","RoomAvailable","Meal","NoOfDays"]]        
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)  #fetch data from mysql workbench to tkinter app
        self.fetch_data()



    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values (%s,%s,%s,%s,%s,%s,%s)",(
                                    self.var_contact.get(),
                                    self.var_checkin.get(),
                                    self.var_checkout.get(),
                                    self.var_roomtype.get(),
                                    self.var_roomavailable.get(),
                                    self.var_meal.get(),
                                    self.var_noofday.get()
                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room has Successfully Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wroooong:{str(es)}",parent=self.root)


    def update_data(self):
        if self.var_contact.get() =="":
            messagebox.showerror("Error","Please enter Mobile Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s, check_out=%s, roomtype=%s, roomavailable=%s, meal=%s, noOfdays=%s where Contact=%s",(
                                    self.var_checkin.get(),
                                    self.var_checkout.get(),
                                    self.var_roomtype.get(),
                                    self.var_roomavailable.get(),
                                    self.var_meal.get(),
                                    self.var_noofday.get(),
                                    self.var_contact.get()
                         ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Updated","Room Details is Successfully Updated",parent=self.root)   



    def Delete_data(self):
        Delete_data=messagebox.askyesno("Hotel Management System Asks You","Do You Want to Delete Data",parent=self.root)
        if Delete_data>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset_data(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofday.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")




    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofday.set(row[6])


    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%' ")
        rows=my_cursor.fetchall()
        if len (rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        



    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofday.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Triple"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Triple"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Triple"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Quad"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Quad"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Quad"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Queen"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Queen"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Queen"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="King"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="King"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="King"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Twin"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Twin"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Twin"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Suite"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Suite"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Suite"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Murphy Room"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Murphy Room"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Murphy Room"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Connecting Rooms"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Connecting Rooms"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Connecting Rooms"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofday.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs." +str("%.2f"%((q5)*0.1))
            ST="Rs." +str("%.2f"%((q5)))
            TT="Rs." +str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        





    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number>>>",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Errror","This Number is not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=437,y=55,width=316,height=210)

                lblName=Label(showDataframe,text="Name: ",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)


                #================Gender Fetch Page===================================#
                conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender: ",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #================Email Fetch Page===================================#
                conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Email: ",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                #================Nationality Fetch Page===================================#
                conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality: ",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                
                #================Address Fetch Page===================================#
                conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbladdress=Label(showDataframe,text="Address: ",font=("arial",12,"bold"))
                lbladdress.place(x=0,y=120)

                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)


                #================Mobile Fetch Page===================================#
                conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
                my_cursor=conn.cursor()
                query=("select Mobile from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblmobile=Label(showDataframe,text="Mobile: ",font=("arial",12,"bold"))
                lblmobile.place(x=0,y=150)

                lbl6=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl6.place(x=90,y=150)


                #=====================Id Proof Fetch Page===============================#
                conn=mysql.connector.connect(host="localhost",username="root",password="admin",database="management")
                my_cursor=conn.cursor()
                query=("select Idproof from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblidproof=Label(showDataframe,text="Id Proof: ",font=("arial",12,"bold"))
                lblidproof.place(x=0,y=180)

                lbl6=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl6.place(x=90,y=180)







if __name__ == "__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.resizable(0,0)
    root.mainloop()
