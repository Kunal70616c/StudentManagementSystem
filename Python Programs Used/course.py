from tkinter import *
from tkinter import ttk, messagebox
import pymysql
from PIL import Image, ImageTk


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("course")
        self.root.geometry("1200x480+170+170")
        self.root.config(bg="white")
        self.root.focus_force()
        # ===========title============
        title = Label(self.root, text="Course Management", font=("gaudy old style", 20, "bold"), bg="#033054",
                      fg="white").place(x=0, y=0, width=1190, height=35)

        # =======variables=========
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.Stream_var = StringVar()
        self.var_search = StringVar()

        # ===========widgets=========
        lbl_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white").place(
            x=10, y=60)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="white").place(
            x=10, y=100)
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="white").place(
            x=10, y=140)
        lbl_stream = Label(self.root, text="Stream", font=("goudy old style", 15, "bold"), bg="white").place(
            x=10, y=180)

        # ====entry fields==============
        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, "bold"),
                                    bg="light yellow").place(x=150, y=60, width=200)

        txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, "bold"),
                             bg="light yellow").place(
            x=150, y=100, width=200)
        txt_charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, "bold"),
                            bg="light yellow").place(
            x=150, y=140, width=200)

        combo_stream = ttk.Combobox(self.root, textvariable=self.Stream_var, font=("times new roman", 10, "bold"),
                                    state="readonly")
        combo_stream['values'] = ("Science", "Commerce", "Arts")
        combo_stream.grid(row=4, column=1, pady=180, padx=150, sticky="w")

        # ==============Buttons====================
        self.btn_add = Button(self.root, text="Save", font=("gaudy old style", 15, "bold"), bg="#2196f3", fg="white",
                              cursor="hand2", command=self.add_course)
        self.btn_add.place(x=90, y=400, width=110, height=40)
        self.btn_update = Button(self.root, text="Update", font=("gaudy old style", 15, "bold"), bg="#00cc00",
                                 fg="white",
                                 cursor="hand2",command=self.update_course)
        self.btn_update.place(x=210, y=400, width=110, height=40)
        self.btn_delete = Button(self.root, text="Delete", font=("gaudy old style", 15, "bold"), bg="#ff0000",
                                 fg="white",
                                 cursor="hand2",command=self.delete)
        self.btn_delete.place(x=330, y=400, width=110, height=40)
        self.btn_clear = Button(self.root, text="Clear", font=("gaudy old style", 15, "bold"), bg="#666699", fg="white",
                                cursor="hand2",command=self.clear)
        self.btn_clear.place(x=450, y=400, width=110, height=40)

        # =========search table=================
        lbl_search_courseName = Label(self.root, text="Search by | Course Name", font=("goudy old style", 15, "bold"),
                                      bg="white").place(
            x=600, y=60)
        self.txt_search_courseName = Entry(self.root, textvariable=self.var_search,
                                           font=("goudy old style", 15, "bold"),
                                           bg="light yellow").place(x=850, y=60, width=180)
        btn_search = Button(self.root, text="Search", font=("gaudy old style", 15, "bold"), bg="#2196f3", fg="white",
                            cursor="hand2",command=self.search)
        btn_search.place(x=1050, y=60, width=110, height=28)

        # ==========Content=====================
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=600, y=100, width=560, height=340)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("course", "duration", "charges", "stream"),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        self.CourseTable.heading("course", text="Course")
        self.CourseTable.heading("duration", text="Duration")
        self.CourseTable.heading("charges", text="Charges")
        self.CourseTable.heading("stream", text="Stream")

        self.CourseTable["show"] = 'headings'
        self.CourseTable.column("course", width=100)
        self.CourseTable.column("duration", width=100)
        self.CourseTable.column("charges", width=100)
        self.CourseTable.column("stream", width=100)

        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    def get_data(self,ev):
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        self.var_course.set(row[0])
        self.var_duration.set(row[1])
        self.var_charges.set(row[2])
        self.Stream_var.set(row[3])

    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.Stream_var.set("")

    def add_course(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course name Should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=%s", (self.var_course.get()))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Course name already present", parent=self.root)
                else:
                    cur.execute("insert into course values(%s,%s,%s,%s)", (self.var_course.get(),
                                                                           self.var_duration.get(),
                                                                           self.var_charges.get(),
                                                                           self.Stream_var.get(),
                                                                           ))

                    con.commit()
                    messagebox.showinfo("Success", "Course added Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)




        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select * from course where name LIKE '%"+str(self.var_search.get())+"%' ")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)




        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update_course(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course name Should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=%s", (self.var_course.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select course from list", parent=self.root)
                else:
                    cur.execute("update course set duration=%s,charges=%s,stream=%s where name=%s", (
                                                                           self.var_duration.get(),
                                                                           self.var_charges.get(),
                                                                           self.Stream_var.get(),
                                                                           self.var_course.get(),
                                                                           ))

                    con.commit()
                    messagebox.showinfo("Success", "Course updated Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course name Should be required", parent=self.root)
            else:
                cur.execute("select * from course where name=%s", (self.var_course.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "please Select course from list", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete this course", parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=%s",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


if __name__=="__main__":
    root = Tk()
    root.resizable(False, False)
    obj = CourseClass(root)
    root.mainloop()
