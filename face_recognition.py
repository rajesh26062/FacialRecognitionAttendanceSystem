from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import time

class Face_Recognition:

    def __init__(self, root):
        self.attendance_dict = {}
        self.root = root
        self.root.state('zoomed')
        self.root.title("Face Recognition Based Attendance Management System")

        # This part is image labels setting start
        # first header image
        img = Image.open("Images_GUI/banner2.png")
        img = img.resize((1280, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1280, height=130)

        # background image
        bg1 = Image.open("Images_GUI/bg-reg.png")
        bg1 = bg1.resize((1200, 520), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=180, width=1280, height=500)

        # title section
        title_lb1 = Label(bg_img, text="Face Recognition System", font=("verdana", 20, "bold"),
                          bg="navyblue", fg="white")
        title_lb1.place(x=0, y=0, width=1280, height=40)

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # Training button 1
        std_b1_1 = Button(bg_img, command=self.face_recog, text="Take Attendance", cursor="hand2",
                          font=("tahoma", 12, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=255, y=330, width=180, height=35)

    # =====================Attendance===================

    def mark_attendance(self, i, r, n):
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:S")

        # Check if the student has already been marked for today
        if i in self.attendance_dict and self.attendance_dict[i] == d1:
            print(f"Attendance for Student {i} already marked for today.")
        else:
            with open("attendance.csv", "a", newline="\n") as f:
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")

            # Update the dictionary to record that this student has been marked for today
            self.attendance_dict[i] = d1

    # Mark students who are absent
    def mark_absent_students(self):
        conn = mysql.connector.connect(user='root', password='Pass@123', host='localhost',
                                       database='face_recognition', port=3306)
        cursor = conn.cursor()

        # Get a list of all student IDs from the database
        cursor.execute("select Student_ID from student")
        all_student_ids = cursor.fetchall()
        all_student_ids = [str(id[0]) for id in all_student_ids]

        # Iterate through the IDs
        for student_id in all_student_ids:
            if student_id not in self.attendance_dict:
                cursor.execute("select Name from student where Student_ID=" + student_id)
                n = cursor.fetchone()
                n = "".join(n)

                cursor.execute("select Roll_No from student where Student_ID=" + student_id)
                r = cursor.fetchone()
                r = "".join(r)

                cursor.execute("select Student_ID from student where Student_ID=" + student_id)
                i = cursor.fetchone()
                i = "".join(i)

                if n and r:
                    n = "".join(n)
                    r = "".join(r)
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtString = now.strftime("%H:%M:S")
                    with open("attendance.csv", "a", newline="\n") as f:
                        f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Absent")

    # ================face recognition==================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                conn = mysql.connector.connect(user='root', password='Pass@123', host='localhost',
                                               database='face_recognition', port=3306)
                cursor = conn.cursor()

                cursor.execute("select Name from student where Student_ID=" + str(id))
                n = cursor.fetchone()
                n = "+".join(n)

                cursor.execute("select Roll_No from student where Student_ID=" + str(id))
                r = cursor.fetchone()
                r = "+".join(r)

                cursor.execute("select Student_ID from student where Student_ID=" + str(id))
                i = cursor.fetchone()
                i = "+".join(i)

                if confidence > 77:
                    cv2.putText(img, f"Student_ID:{i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (64, 15, 223), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll-No:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(i, r, n)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face_LBPHFaceRecognizer.create()
        clf.read("clf.xml")

        videoCap = cv2.VideoCapture(0)

        # Set the desired capture duration in seconds (e.g., 30 seconds)
        capture_duration = 10 #seconds

        # Start time
        start_time = time.time()

        while (time.time() - start_time) < capture_duration:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        videoCap.release()
        cv2.destroyAllWindows()

        # After the capture duration, mark the remaining students as Absent
        self.mark_absent_students()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()


