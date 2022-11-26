from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os

# from course import CourseClass
# from stdnt import Student
# from stdnt import Student

class menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Menu")
        self.root.geometry("1370x700+0+0")
        self.root.config(bg="white")
        # =======icons======
        self.logo_dash = Image.open("images/logo.png")
        resize = self.logo_dash.resize((90,50), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(resize)
        # ========title=======
        title = Label(self.root, text="Admin Page", compound=LEFT, image=self.new_image,
                      font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1,
                                                                                            height=50)

        # =========menu=============
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=50, width=1340, height=80)

        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#57a1f8", fg="white",
                            cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="Students", font=("goudy old style", 15, "bold"), bg="#57a1f8", fg="white",
                             cursor="hand2", command=self.add_Std).place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#57a1f8", fg="white",
                            cursor="hand2", command=self.add_result).place(x=460, y=5, width=200, height=40)
        btn_fees = Button(M_Frame, text="Fees", font=("goudy old style", 15, "bold"), bg="#57a1f8", fg="white",
                          cursor="hand2",command=self.add_fees).place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#57a1f8", fg="white",
                            cursor="hand2",command=self.logout).place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#57a1f8", fg="white",
                          cursor="hand2",command=self.Exet).place(x=1120, y=5, width=200, height=40)

        # =============content window====================================
        self.bg_img = Image.open("images/BG.jpg")
        self.bg_img = self.bg_img.resize((1350, 515), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=10, y=140, width=1350, height=515)

        # # ==========update details===============
        # self.lbl_courses = Label(self.root, text="Total Courses\n [ 0 ]", font=("gaudy old style", 20),
        #                          bg="#00ccff").place(x=350, y=550, width=345, height=100)
        # self.lbl_courses = Label(self.root, text="Total Students\n [ 0 ]", font=("gaudy old style", 20),
        #                          bg="#00ccff").place(x=703, y=550, width=345, height=100)
        # self.lbl_courses = Label(self.root, text="Total results\n [ 0 ]", font=("gaudy old style", 20),
        #                          bg="#00ccff").place(x=1053, y=550, width=300, height=100)

        # ===========footer==============
        footer = Label(self.root, text="Student Management System",
                       font=("goudy old style", 20, "bold"), bg="BLACK", fg="white").pack(side=BOTTOM, fill=X)

    def add_course(self):
        #from course import CourseClass
        #self.new_win = Toplevel(self.root)
        #self.new_obj = CourseClass(self.new_win)
        os.system("python course.py")

    def add_Std(self):
        #from stdnt import Student
        #self.new_win = Toplevel(self.root)
        #self.new_obj = Student(self.new_win)
        os.system("python stdnt.py")

    def add_result(self):
        #from result import RMS
        #self.new_win = Toplevel(self.root)
        #self.new_obj = RMS(self.new_win)
        os.system("python result.py")

    def add_fees(self):
        #from fee import FMS
        #self.new_win = Toplevel(self.root)
        #self.new_obj = FMS(self.new_win)
        os.system("python fee.py")


    def logout(self):
        op=messagebox.askyesno("Confirm","do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def Exet(self):
        op=messagebox.askyesno("Confirm","do you really want to exit?",parent=self.root)
        if op==True:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = menu(root)
    root.mainloop()
