from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        title = Label(self.root, text="Student Management System", font=("gaudy old style", 20, "bold"), bg="#033054",
                      fg="white").place(x=0, y=0, width=1350, height=60)

        # ==============All Vartiables======================================

        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.stream_var = StringVar(root)
        self.course_var = StringVar()

        self.search_by_var = StringVar()
        self.search_txt = StringVar()

        # =============entry fiel d to update course list==========
        self.Course_list = []
        # self.fetch_course()
        # =============Manage Frame=========================================
        Manage_Frame = Frame(self.root, bd=4, bg="white")
        Manage_Frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(Manage_Frame, text="Manage Students", bg="white", fg="#033054",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=1, pady=5 )
        # roll
        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="white", fg="black", font=("times new roman", 10, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"),
                         relief=GROOVE,bg="light yellow")
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        # name
        lbl_name = Label(Manage_Frame, text="Name", bg="white", fg="black", font=("times new roman", 10, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_Frame,width=28, textvariable=self.name_var, font=("times new roman", 10, "bold"),
                         relief=GROOVE,bg="light yellow")
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        # email
        lbl_email = Label(Manage_Frame, text="Email", bg="white", fg="black", font=("times new roman", 10, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_Frame,width=28, textvariable=self.email_var, font=("times new roman", 10, "bold"),
                          relief=GROOVE,bg="light yellow")
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        # gender
        lbl_gender = Label(Manage_Frame, text="Gender", bg="white", fg="black", font=("times new roman", 10, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame,width=28, textvariable=self.gender_var, font=("times new roman", 10, "bold"),
                                    state="readonly")
        combo_gender['values'] = ("male", "female", "others")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        # contac
        lbl_contac = Label(Manage_Frame, text="Contact", bg="white", fg="black", font=("times new roman", 10, "bold"))
        lbl_contac.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contac = Entry(Manage_Frame,width=28, textvariable=self.contact_var, font=("times new roman", 10, "bold"),
                           relief=GROOVE,bg="light yellow")
        txt_contac.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        # dob
        lbl_dob = Label(Manage_Frame, text="DOB", bg="white", fg="black", font=("times new roman", 10, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_Frame,width=28, textvariable=self.dob_var, font=("times new roman", 10, "bold"),
                        relief=GROOVE,bg="light yellow")
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        # address
        lbl_address = Label(Manage_Frame, text="Address", bg="white", fg="black",
                            font=("times new roman", 10, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_address = Text(Manage_Frame, width=25, height=3,bg="light yellow")
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        # stream
        lbl_stream = Label(Manage_Frame, text="Stream", bg="white", fg="black", font=("times new roman", 10, "bold"))
        lbl_stream.grid(row=8, column=0, pady=10, padx=20, sticky="w")

        self.combo_stream = ttk.Combobox(Manage_Frame,width=28, textvariable=self.stream_var, font=("times new roman", 10, "bold"),
                                    state="readonly")
        self.combo_stream['values'] = ("Select", "Science", "Commerce", "Arts")
        self.combo_stream.grid(row=8, column=1, pady=10, padx=20, sticky="w")
        self.combo_stream.bind("<<ComboboxSelected>>",self.fetch_course)

        # COURSE

        self.lbl_course = Label(Manage_Frame, text="Course", bg="white", fg="black", font=("times new roman", 10, "bold"))
        self.lbl_course.grid(row=9, column=0, pady=10, padx=20, sticky="w")
        self.combo_course = ttk.Combobox(Manage_Frame,width=28, textvariable=self.course_var, font=("times new roman", 10, "bold"),
                                    state="readonly")
        self.combo_course['values'] = self.Course_list
        self.combo_course.grid(row=9, column=1, pady=10, padx=20, sticky="w")


        # ==============button================================================
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="white")
        btn_Frame.place(x=20, y=520, width=410, )

        Addbtn = Button(btn_Frame, text="ADD", width=10, command=self.add_student,
                        cursor="hand2",bg="#2196f3", fg="white",).grid(row=0, column=0, padx=10,
                                             pady=10)
        updatebtn = Button(btn_Frame, text="UPDATE", width=10, command=self.update_stdnt,
                           cursor="hand2", bg="#00cc00",
                                 fg="white").grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="DELETE", width=10, command=self.delete,
                           cursor="hand2", bg="#ff6600",
                                 fg="white").grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="CLEAR", width=10, command=self.clear,
                          cursor="hand2", bg="#666699", fg="white").grid(row=0, column=3, padx=10, pady=10)





        # =============detail Frame=========================================

        Detail_Frame = Frame(self.root,relief=RIDGE, bg="white")
        Detail_Frame.place(x=500, y=100, width=830, height=580)

        # Search
        lbl_search = Label(Detail_Frame, text="Search By", bg="white", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by_var, width=10,
                                    font=("times new roman", 10, "bold"), state="readonly")
        combo_search['values'] = ("roll", "name", "course", "stream")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

        txt_search = Entry(Detail_Frame, textvariable=self.search_txt, width=10, font=("times new roman", 10, "bold"),
                           bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10,
                           cursor="hand2", command=self.search,bg="#2196f3", fg="white",).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10,
                            cursor="hand2", command=self.show,bg="red", fg="white",).grid(row=0, column=4, padx=10, pady=10)
        # ================Table======================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="blue")
        Table_Frame.place(x=10, y=50, width=795, height=510)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_Frame, columns=(
            "roll", "name", "email", "stream", "course", "gender", "contact", "dob", "Address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Roll No")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("stream", text="Stream")
        self.Student_table.heading("course", text="Course")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="DOB")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("stream", width=100)
        self.Student_table.column("course", width=100)

        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=150)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_data)
        # self.fetch_data()
        self.show()

    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        cur.execute("select * from student where " + str(self.search_by_var.get()) + " LIKE '%" + str(
            self.search_txt.get()) + "%' ")
        rows = cur.fetchall()

        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    def choto(self,ev):
        print(self.stream_var.get())


    def fetch_course(self,ev):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        print(self.stream_var.get())
        val=self.stream_var.get()
        print(val)
        try:
            #cur.execute('select name from course')
            cur.execute("select name from course where stream LIKE '%" + str(self.stream_var.get()) + "%' ")
            rows = cur.fetchall()
            self.Course_list.clear()
            for row in rows:
                self.Course_list.append(row[0])
            print(self.Course_list)
            self.combo_course['values']=self.Course_list


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def add_student(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        try:
            if self.Roll_No_var.get() == "":
                messagebox.showerror("Error", "Student name Should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=%s", (self.Roll_No_var.get()))
                row = cur.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "Student name already present", parent=self.root)

                else:
                    cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                                           self.name_var.get(),
                                                                                           self.email_var.get(),
                                                                                           self.stream_var.get(),
                                                                                           self.course_var.get(),
                                                                                           self.gender_var.get(),
                                                                                           self.contact_var.get(),
                                                                                           self.dob_var.get(),
                                                                                           self.txt_address.get('1.0',
                                                                                                                END)
                                                                                           ))

                    con.commit()
                    cur.execute("insert into result values(%s,'','','','','','')", (self.Roll_No_var.get(),
                                                                                           ))
                    con.commit()
                    cur.execute("insert into fees values(%s,'','','','','','')", (self.Roll_No_var.get(),
                                                                                    ))
                    con.commit()
                    messagebox.showinfo("Success", "student added Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def show(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def get_data(self,ev):
        r = self.Student_table.focus()
        content = self.Student_table.item(r)
        row = content["values"]
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.stream_var.set(row[3])
        self.course_var.set(row[4])
        self.gender_var.set(row[5])
        self.contact_var.set(row[6])
        self.dob_var.set(row[7])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[8])

    def clear(self):
        self.show()
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.stream_var.set("")
        self.course_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0", END)

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        try:
            if self.Roll_No_var.get() == "":
                messagebox.showerror("Error", "roll Should be required", parent=self.root)
            else:
                cur.execute("select * from student where roll=%s", (self.Roll_No_var.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "please Select roll from list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete this student record",
                                             parent=self.root)
                    if op == True:
                        cur.execute("delete from student where roll=%s", (self.Roll_No_var.get(),))
                        con.commit()
                        cur.execute("delete from result where roll=%s", (self.Roll_No_var.get(),))
                        con.commit()
                        cur.execute("delete from fees where roll=%s", (self.Roll_No_var.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course deleted Successfully", parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def update_stdnt(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        try:
            if self.Roll_No_var.get() == "":
                messagebox.showerror("Error", "Roll number is required", parent=self.root)
            else:
                cur.execute("select * from student where roll=%s", (self.Roll_No_var.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select student details from list", parent=self.root)
                else:
                    cur.execute(
                        "update student set name=%s,email=%s,stream=%s,course=%s,gender=%s,contact=%s,dob=%s,address=%s where roll=%s",
                        (
                            self.name_var.get(),
                            self.email_var.get(),
                            self.stream_var.get(),
                            self.course_var.get(),
                            self.gender_var.get(),
                            self.contact_var.get(),
                            self.dob_var.get(),
                            self.txt_address.get('1.0', END),
                            self.Roll_No_var.get(),
                        ))

                    con.commit()
                    messagebox.showinfo("Success", "updation Successfull", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


root = Tk()
root.resizable(False,False)
ob = Student(root)
root.mainloop()
