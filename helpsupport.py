from tkinter import *
from PIL import Image, ImageTk
import webbrowser

class Helpsupport:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Face Recognition Attendance Management System")

        # Header image
        img = Image.open(r"C:\Rajesh\Projects\attendance-management-system-face-recognition-main\Images_GUI\banner2.png")  # Replace with your image path
        img = img.resize((1280, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # Set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1280, height=130)

        # Background image
        bg1 = Image.open(r"C:\Rajesh\Projects\attendance-management-system-face-recognition-main\Images_GUI\bg1.jpg")  # Replace with your image path
        bg1 = bg1.resize((1280, 500), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # Set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=145, width=1280, height=500)

        # Title section
        title_lb1 = Label(bg_img, text="Help & Support", font=("verdana", 20, "bold"), bg="navyblue", fg="white")
        title_lb1.place(x=0, y=0, width=1280, height=40)

        # Create buttons below the section
        # Student button 1
        std_img_btn = Image.open(r"C:\Rajesh\Projects\attendance-management-system-face-recognition-main\Images_GUI\web.png")  # Replace with your image path
        std_img_btn = std_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.website, image=self.std_img1, cursor="hand2")
        std_b1.place(x=210, y=160, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.website, text="Website", cursor="hand2", font=("tahoma", 15, "bold"),
                          bg="white", fg="navyblue")
        std_b1_1.place(x=210, y=340, width=180, height=45)

        # Detect Face button 2
        det_img_btn = Image.open(r"C:\Rajesh\Projects\attendance-management-system-face-recognition-main\Images_GUI\fb.png")  # Replace with your image path
        det_img_btn = det_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.det_img1 = ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img, command=self.facebook, image=self.det_img1, cursor="hand2")
        det_b1.place(x=440, y=160, width=180, height=180)

        det_b1_1 = Button(bg_img, command=self.facebook, text="Facebook", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        det_b1_1.place(x=440, y=340, width=180, height=45)

        # Attendance System button 3
        att_img_btn = Image.open(r"C:\Rajesh\Projects\attendance-management-system-face-recognition-main\Images_GUI\yt.png")  # Replace with your image path
        att_img_btn = att_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img, command=self.youtube, image=self.att_img1, cursor="hand2")
        att_b1.place(x=670, y=160, width=180, height=180)

        att_b1_1 = Button(bg_img, command=self.youtube, text="Youtube", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        att_b1_1.place(x=670, y=340, width=180, height=45)

        # Help Support button 4
        hlp_img_btn = Image.open(r"C:\Rajesh\Projects\attendance-management-system-face-recognition-main\Images_GUI\gmail.png")  # Replace with your image path
        hlp_img_btn = hlp_img_btn.resize((180, 180), Image.ANTIALIAS)
        self.hlp_img1 = ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img, command=self.gmail, image=self.hlp_img1, cursor="hand2")
        hlp_b1.place(x=900, y=160, width=180, height=180)

        hlp_b1_1 = Button(bg_img, command=self.gmail, text="Gmail", cursor="hand2", font=("tahoma", 15, "bold"),
                          bg="white", fg="navyblue")
        hlp_b1_1.place(x=900, y=340, width=180, height=45)

    def website(self):
        self.new = 1
        self.url = "https://github.com/rajesh26062"
        webbrowser.open(self.url, new=self.new)

    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/"
        webbrowser.open(self.url, new=self.new)

    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com"
        webbrowser.open(self.url, new=self.new)

    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url, new=self.new)

if __name__ == "__main__":
    root = Tk()
    obj = Helpsupport(root)
    root.mainloop()
