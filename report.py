from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox 

class ReportRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # =====================================================TITLE==============================================#
        lbl_title = Label(self.root, text="ABOUT GRAND HOTEL", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ==================================LOGO==================================================================#
        img2 = Image.open(r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\logohotel.png")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=40)

        # Create a main frame to hold all content
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True)

        # Configure weights for equal-sized frames
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Create 6 frames with equal sizes
        self.frame1 = Frame(self.main_frame)
        self.frame1.grid(row=0, column=0, sticky="nsew")

        self.frame2 = Frame(self.main_frame)
        self.frame2.grid(row=0, column=1, sticky="nsew")

        self.frame3 = Frame(self.main_frame)
        self.frame3.grid(row=0, column=2, sticky="nsew")

        self.frame4 = Frame(self.main_frame)
        self.frame4.grid(row=1, column=0, sticky="nsew")

        self.frame5 = Frame(self.main_frame)
        self.frame5.grid(row=1, column=1, sticky="nsew")

        self.frame6 = Frame(self.main_frame)
        self.frame6.grid(row=1, column=2, sticky="nsew")
 
        # Ensure your image paths are correct and accessible
        image_path1 = r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\imaaage1.jpeg"  # Replace with your actual image path
        image_path2 = r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\imaaage2.jpeg"  # Replace with your actual image path
        image_path3 = r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\imaaage3.jpeg"  # Replace with your actual image path
        image_path4 = r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\imaaage4.jpeg"  # Replace with your actual image path
        image_path5 = r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\imaaage5.jpeg"  # Replace with your actual image path
        image_path6 = r"C:\Users\harsh\OneDrive\Pictures\ImagesHotel\imaaage6.jpeg"  # Replace with your actual image path

        # Load and resize images to the same dimensions (adjust size as needed)
        image_size = (500, 300)  # Define your desired width and height
        img1 = Image.open(image_path1).resize(image_size, Image.Resampling.LANCZOS)
        img2 = Image.open(image_path2).resize(image_size, Image.Resampling.LANCZOS)
        img3 = Image.open(image_path3).resize(image_size, Image.Resampling.LANCZOS)
        img4 = Image.open(image_path4).resize(image_size, Image.Resampling.LANCZOS)
        img5 = Image.open(image_path5).resize(image_size, Image.Resampling.LANCZOS)
        img6 = Image.open(image_path6).resize(image_size, Image.Resampling.LANCZOS)

        # Convert images to PhotoImage format
        self.photoimg1 = ImageTk.PhotoImage(img1)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        # Create labels with images in each frame
        label1 = Label(self.frame1, image=self.photoimg1)
        label1.pack(fill=BOTH, expand=True)

        label2 = Label(self.frame2, image=self.photoimg2)
        label2.pack(fill=BOTH, expand=True)

        label3 = Label(self.frame3, image=self.photoimg3)
        label3.pack(fill=BOTH, expand=True)

        label4 = Label(self.frame4, image=self.photoimg4)
        label4.pack(fill=BOTH, expand=True)

        label5 = Label(self.frame5, image=self.photoimg5)
        label5.pack(fill=BOTH, expand=True)

        label6 = Label(self.frame6, image=self.photoimg6)
        label6.pack(fill=BOTH, expand=True)

if __name__ == "__main__":
    root = Tk()
    obj = ReportRoom(root)
    root.resizable(0,0)
    root.mainloop()
