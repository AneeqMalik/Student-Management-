from tkinter import*
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import pyodbc


screen=Tk()
screen.title("STUDENT DATABASE")
screen.config(bg='white')
screen.geometry('1920x1080')

#Backgroud Image
bg = ImageTk.PhotoImage(file="img (1).v1.jpg")
#Background Image label
bg_label=Label(screen,image=bg)
bg_label.place(x=0,y=0, relwidth=1, relheight=1)

# Title label
title_label = Label(screen, text="STUDENT DATABASE ",bd=10,relief=RIDGE, height=2,bg='#000324',fg="Gold",font=('Brush Script MT', 30,'italic','underline','bold'))
title_label.pack()
def enter():
    m = Tk()
    m.title("STUDENT DATABASE")
    m.geometry("1920x1080")
    title = Label(m, text="Student Management System", bd=10, relief=RIDGE, font=("times new roman", 40, "bold"),
                  bg="#53a1f5", fg="red")
    title.pack(side=TOP, fill=X)

    def View():
        con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=e:\student.accdb;'))
        cursor1 = con.cursor()
        cursor1.execute("select * from STUDENTDETAIL ORDER by StudentID")
        rows = cursor1.fetchall()
        if len(rows) != 0:
            for i in rows:
                Student_table.insert('', END, values=i)
        con.close()

    def add():
        con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=e:\student.accdb;'))
        cursor1 = con.cursor()

        cursor1.execute(
            f"INSERT INTO STUDENTDETAIL(StudentID,FirstName,LastName,Gender,ContactNo) values('{ROll_NO_e.get()}','{first_name_e.get()}','{last_name_e.get()}','{combo_gender.get()}',{contact_no_e.get()})")
        con.commit()
        View()
        messagebox.showinfo("Student Database", "One Record Has Been Added")
        con.close()

    def delete():
        con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=e:\student.accdb;'))
        cursor1 = con.cursor()
        cursor1.execute(f"DELETE FROM STUDENTDETAIL where StudentID = {ROll_NO_e.get()}")
        con.commit()
        View()
        messagebox.askyesno("Student Database", "One Record Is Deleted")
        con.close()

    def update():
        con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=e:\student.accdb;'))
        cursor1 = con.cursor()
        cursor1.execute(
            f"UPDATE STUDENTDETAIL set FirstName='{first_name_e.get()}',LastName='{last_name_e.get()}',Gender='{combo_gender.get()}',ContactNo={contact_no_e.get()} WHERE StudentID={ROll_NO_e.get()}")
        con.commit()
        View()
        messagebox.askyesno("Student Database", "Do Want To Update Existing Details")
        con.close()

    def clear():
        for i in Student_table.get_children():
            Student_table.delete(i)

    def search():
        con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=e:\student.accdb;'))
        cursor2 = con.cursor()
        cursor2.execute("SELECT FirstName FROM STUDENTDETAILS Where FirstName = 'txt_Search'")
        for row in cursor2.fetchall():
            print (row)

    # MANAGEMENT FRAME:
    Manage_Frame = Frame(m, bd=4, relief=RIDGE, bg="#53a1f5")
    Manage_Frame.place(x=20, y=100, width=1000, height=1080)
    m_title = Label(Manage_Frame, text="Manage Students", bg="#53a1f5", fg="white",
                    font=("times new roman", 30, "bold"))
    m_title.grid(row=0, columnspan=2, pady=20)
    # DETAILS FRAME:
    Detail_Frame = Frame(m, bd=4, relief=RIDGE, bg="white")
    Detail_Frame.place(x=500, y=100, width=1010, height=1080)
    detail_search = Label(Detail_Frame, width=10, text="SEARCH BY", bg="#53a1f5", fg="white",
                          font=("times new roman", 15, "bold"))
    detail_search.grid(row=0, column=0, pady=10, padx=20)

    combo_search = ttk.Combobox(Detail_Frame, width=10, textvariable="", font=("times new roman", 13, "bold"),
                                state='readonly')
    combo_search['values'] = ("StudentID", "FirstName", "Contact")
    combo_search.grid(row=0, column=1, padx=20, pady=10)

    txt_Search = Entry(Detail_Frame, textvariable="", relief=GROOVE, font=("times new roman", 13, "bold"))
    txt_Search.grid(row=0, column=2, padx=20, pady=10)
    search_butt = Button(Detail_Frame, text="Search", width=10, command=search).grid(row=0, column=3, padx=20, pady=10)
    show_all_butt = Button(Detail_Frame, text="Show All", width=10, command=View).grid(row=0, column=4, padx=20,
                                                                                       pady=10)
    # Table Frame
    Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="white")
    Table_Frame.place(x=10, y=70, width=1010, height=1080)
    Student_table = ttk.Treeview(Table_Frame, height=1000,
                                 columns=("column1", "column2", "column3", "column4", "column5"), show="headings")
    Student_table.heading("#1", text="ROLL NO")
    Student_table.heading("#2", text="FIRST NAME")
    Student_table.heading("#3", text="LAST NAME")
    Student_table.heading("#4", text="Gender")
    Student_table.heading("#5", text="CONTACT")
    Student_table.pack()

    # Button Frame:
    button_frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="#53a1f5")
    button_frame.place(x=15, y=500, width=450)

    add_butt = Button(button_frame, text="ADD", width=10, command=add).grid(row=0, column=0, padx=10, pady=10)
    update_butt = Button(button_frame, text="UPDATE", width=10, command=update).grid(row=0, column=1, padx=10, pady=10)
    delete_butt = Button(button_frame, text="DELETE", width=10, command=delete).grid(row=0, column=2, padx=10, pady=10)
    clear_butt = Button(button_frame, text="CLEAR", width=10, command=clear).grid(row=0, column=3, padx=10, pady=10)
    # Labels:
    ROll_NO = Label(Manage_Frame, text="ROLL NO", bg="#53a1f5", fg="white",
                    font=("times new roman", 14, "bold"))
    ROll_NO.grid(row=1, column=0, padx=20, pady=10)
    ROll_NO_e = Entry(Manage_Frame, relief=GROOVE)
    ROll_NO_e.grid(row=1, column=1, padx=20, pady=20)
    first_name = Label(Manage_Frame, text="FIRST NAME", bg="#53a1f5", fg="white",
                       font=("times new roman", 14, "bold"))
    first_name.grid(row=2, column=0, padx=20, pady=10)
    first_name_e = Entry(Manage_Frame, relief=GROOVE)
    first_name_e.grid(row=2, column=1, padx=20, pady=20)

    last_name = Label(Manage_Frame, text="LAST NAME", bg="#53a1f5", fg="white",
                      font=("times new roman", 14, "bold"))
    last_name.grid(row=3, column=0, padx=20, pady=10)
    last_name_e = Entry(Manage_Frame, relief=GROOVE)
    last_name_e.grid(row=3, column=1, padx=20, pady=20)

    contact_no = Label(Manage_Frame, text="CONTACT NO", bg="#53a1f5", fg="white",
                       font=("times new roman", 14, "bold"))
    contact_no.grid(row=5, column=0, padx=20, pady=10)
    contact_no_e = Entry(Manage_Frame, relief=GROOVE)
    contact_no_e.grid(row=5, column=1, padx=20, pady=20)

    gender = Label(Manage_Frame, text="GENDER", bg="#53a1f5", fg="white",
                   font=("times new roman", 14, "bold"))
    gender.grid(row=7, column=0, padx=20, pady=10)
    combo_gender = ttk.Combobox(Manage_Frame, font=("times new roman", 10, "bold"), state='readonly')
    combo_gender['values'] = ("MALE", "FEMALE")
    combo_gender.grid(row=7, column=1, padx=20, pady=10)

    main_f = Frame(m)
    main_f.pack()

# Buttons
def quit():
    quit = messagebox.askyesno("STUDENT DATABASE", "Do you want to leave?")
    # here 1 means ok or yes:
    if quit == 1:
        screen.destroy()
welcome_button = Button(screen,width=25,bd=10,relief=RIDGE, text="ENTER TO DATABASE", fg='GOLD',bg="#000324", font=('Brush Script MT', 28, 'bold','italic'),
                    command=enter)
welcome_button.pack(pady=140)
exit_button = Button(screen,bd=10,relief=RIDGE, text="Exit", fg="GOLD", width=25,bg="#000324",font=('Brush Script MT', 28, 'bold','italic'), command=quit)
exit_button.pack(pady=100)


screen.mainloop()