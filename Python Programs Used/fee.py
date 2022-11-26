from tkinter import *
from tkinter import ttk, messagebox
import pymysql


class FMS:
    def __init__(self, root):
        self.root = root
        self.root.title("FEES MANAGENMENT SYSTEM")
        self.root.geometry("1000x500+170+150")
        self.root.config(bg="white")
        self.root.focus_force()
        # =========title=================
        title = Label(self.root, text=" F E E S   M A N A G E M E N T   S Y S T E M ",
                      font=("gaudy old style", 25, "bold"), bg="#033054",
                      fg="white").pack(side=TOP, fill=X)

        # ==============All Vartiables======================================
        self.Roll_No_var = StringVar()

        self.fees_var = StringVar()
        self.sem_var = StringVar()

        self.search_var=StringVar()
        # =============Manage Frame=========================================
        Manage_Frame = Frame(self.root, relief=RIDGE, bg="white")
        Manage_Frame.place(x=10, y=60, width=450, height=420)

        m_title = Label(Manage_Frame, text="Manage Results", bg="white", fg="black",
                        font=("times new roman", 15, "bold"))
        m_title.grid(row=0, columnspan=1, pady=20)
        # roll
        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="white", fg="black", font=("times new roman", 10, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 10, "bold"), bd=5,
                         relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")
        # ============semester===========

        lbl_sem = Label(Manage_Frame, text="Semester", bg="white", fg="black", font=("times new roman", 10, "bold"))
        lbl_sem.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        combo_sem = ttk.Combobox(Manage_Frame, textvariable=self.sem_var, font=("times new roman", 10, "bold"),
                                 state="readonly")
        combo_sem['values'] = ("f1", "f2", "f3", "f4", "f5", "f6")
        combo_sem.grid(row=2, column=1, pady=10, padx=20, sticky="w")
        # result
        lbl_fees = Label(Manage_Frame, text="Fees", bg="white", fg="black",
                           font=("times new roman", 10, "bold"))
        lbl_fees.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        combo_fees = ttk.Combobox(Manage_Frame, textvariable=self.fees_var, font=("times new roman", 10, "bold"),
                                 state="readonly")
        combo_fees['values'] = ("paid","not paid")
        combo_fees.grid(row=3, column=1, pady=10, padx=20, sticky="w")
        # ==============button================================================
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="white")
        btn_Frame.place(x=100, y=300, width=250, height=70)

        updatebtn = Button(btn_Frame, text="UPDATE", width=13, height=2, bg="#006600", fg="white",
                           command=self.update_stdnt, font=("gaudy old style", 9, "bold")).grid(row=0, column=0,
                                                                                                padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="CLEAR", width=13, height=2, command=self.clear, bg="#666699", fg="white",
                          font=("gaudy old style", 9, "bold")).grid(row=0, column=1, padx=10, pady=10)

        Detail_Frame = Frame(self.root, relief=RIDGE, bg="white")
        Detail_Frame.place(x=480, y=60, width=500, height=420)

        lbl_search = Label(Detail_Frame, text="Search By Roll and Semester", bg="white", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_search.place(x=5, y=10)

        lbl_sRoll = Label(Detail_Frame, text="Roll No.", bg="white", fg="black",
                          font=("times new roman", 20, "italic")).place(x=12, y=50)


        self.txt_search_roll = Entry(Detail_Frame, textvariable=self.search_var,
                                           font=("goudy old style", 15, "bold"),
                                           bg="light yellow").place(x=110, y=50)



        searchbtn = Button(Detail_Frame, text="Search", width=10,command=self.search, bg="red", fg="white", font=("gaudy old style", 9, "bold")).place(x=350, y=50)

        # ==========Content=====================
        self.C_Frame = Frame(Detail_Frame, bd=2, relief=RIDGE)
        self.C_Frame.place(x=10, y=100, width=480, height=300)

        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)

        self.result_Table = ttk.Treeview(self.C_Frame, columns=("roll", "sem1", "sem2", "sem3", "sem4", "sem5", "sem6"),
                                        xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.result_Table.xview)
        scrolly.config(command=self.result_Table.yview)

        self.result_Table.heading("roll", text="Roll")
        self.result_Table.heading("sem1", text="Sem 1")
        self.result_Table.heading("sem2", text="Sem 2")
        self.result_Table.heading("sem3", text="Sem 3")
        self.result_Table.heading("sem4", text="Sem 4")
        self.result_Table.heading("sem5", text="Sem 5")
        self.result_Table.heading("sem6", text="Sem 6")

        self.result_Table["show"] = 'headings'
        self.result_Table.column("roll", width=100)
        self.result_Table.column("sem1", width=100)
        self.result_Table.column("sem2", width=100)
        self.result_Table.column("sem3", width=100)
        self.result_Table.column("sem4", width=100)
        self.result_Table.column("sem5", width=100)
        self.result_Table.column("sem6", width=100)
        self.result_Table.pack(fill=BOTH, expand=1)
        # self.CourseTable.bind("<ButtonRelease-1>", self.get_data)


    def update_stdnt(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        try:
            if self.Roll_No_var.get() == "":
                messagebox.showerror("Error", "Roll number is required", parent=self.root)
            else:
                cur.execute("select * from fees where roll=%s", (self.Roll_No_var.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "put the correct roll no", parent=self.root)
                else:
                    cur.execute(
                        "update fees set " + str(self.sem_var.get()) + "=%s where roll=%s",
                        (
                            self.fees_var.get(),
                            self.Roll_No_var.get(),
                        ))

                    con.commit()
                    messagebox.showinfo("Success", "updation Successfull", parent=self.root)
                    #self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        #self.show()
        self.Roll_No_var.set("")
        self.sem_var.set("")
        self.result_var.set("")

    def search(self):
        con = pymysql.connect(host="localhost", user="root", password="1234", database="sms")
        cur = con.cursor()
        cur.execute("select * from fees where roll LIKE '%" + str(self.search_var.get()) + "%' ")
        rows = cur.fetchall()

        if len(rows) != 0:
            self.result_Table.delete(*self.result_Table.get_children())
        for row in rows:
            self.result_Table.insert('', END, values=row)
        con.commit()
        con.close()



if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    obj = FMS(root)
    root.mainloop()
