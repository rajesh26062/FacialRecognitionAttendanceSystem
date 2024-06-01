from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import PIL

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Face Recognition Attendance Management System")

        # Header image
        img = Image.open(r"C:\Rajesh\Projects\attendance-management-system-face-recognition-main\Images_GUI\banner2.png")
        img = img.resize((1280, 130), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Set image as label
        header_label = Label(self.root, image=self.photoimg)
        header_label.place(x=0, y=0, width=1280, height=130)

        # Background image
        bg_img = Image.open(r"C:\Rajesh\Projects\attendance-management-system-face-recognition-main\Images_GUI\bg4.jpg")
        bg_img = bg_img.resize((1280, 500), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg_img)

        # Set image as label
        bg_label = Label(self.root, image=self.photobg1)
        bg_label.place(x=0, y=145, width=1280, height=500)

        # Title section
        title_label = Label(bg_label, text="Developer Information", font=("verdana", 20, "bold"), bg="navyblue",
                            fg="white")
        title_label.place(x=0, y=0, width=1280, height=40)

        # Developer image and information
        developer_img = Image.open(r"C:\Rajesh\Projects\attendance-management-system-face-recognition-main\Images_GUI\phong.png")
        developer_img = developer_img.resize((250, 250), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.ANTIALIAS)
        self.developer_photo = ImageTk.PhotoImage(developer_img)

        developer_image_button = Button(bg_label, image=self.developer_photo, cursor="hand2")
        developer_image_button.place(x=350, y=120, width=250, height=250)

        developer_name_button = Button(bg_label, text="Rajesh and Rahul", cursor="hand2",
                                       font=("tahoma", 10, "bold"), bg="white", fg="navyblue")
        developer_name_button.place(x=350, y=370, width=250, height=50)

        # Information Frame
        info_frame = Frame(bg_label, bd=2, bg="white")
        info_frame.place(x=600, y=120, width=400, height=300)

        developer_info_label = Label(info_frame, text="Developer Information", font=("verdana", 12, "bold"),
                                     bg="white", fg="navyblue")
        developer_info_label.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        # Labels and developer information
        labels = ["Full Name:", "Full Name", "Class:", "Batch", "Roll no"]
        developer_info = ["Rajesh Kishor Chaudhary", "Rahul Varma", "TYCS", "B1", "054,051"]

        for i, label_text in enumerate(labels):
            label = Label(info_frame, text=label_text, font=("verdana", 12, "bold"), bg="white", fg="navyblue")
            label.grid(row=i + 1, column=0, padx=5, pady=12)

            info = Label(info_frame, text=developer_info[i], font=("verdana", 12), bg="white")
            info.grid(row=i + 1, column=1, padx=5, pady=12, sticky=W)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
