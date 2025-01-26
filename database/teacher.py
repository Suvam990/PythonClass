import sqlite3
import tkinter as tk
from tkinter import messagebox


conn = sqlite3.connect('database/teacher.sqlite3')
cursor = conn.cursor()

def create_tabel():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   age INTEGER,
                   position TEXT,
                   Subject TEXT,
                   address TEXT)""")
    conn.commit()
    print("tabel create successfully")

create_tabel()

def insert_data(name,age,position,Subject,address):
    cursor.execute("""INSERT INTO
        teacher(name,age,position,Subject,address)VALUES(?,?,?,?,? )""",
        (name,age,position,Subject,address))
    conn.commit()
    messagebox.showinfo("Success","Data insersted successfully")


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# position = input("Enter your position: ")
# Subject = input("Enter your Subject: ")
# address = input("enter your address: ")    
# insert_data(name,age,position,Subject,address)

# def show_data():
#     # cursor.execute("""SELECT * FROM teacher""")
#     cursor.execute("""SELECT name,position,Subject FROM teacher""")
#     data = cursor.fetchall()
#     print(data)

# show_data()    

# def on_summite():
#     name = entry_teacherName.get()
#     age = entry_teacherAge.get()
#     position = entry_teacherPosition.get()
#     Subject =entry_teacherSubject.get()
#     address = entry_teacherAddress.get()
    
#     if name and age and position and Subject and address:
#         insert_data(name,age,position,Subject,address)
#         messagebox.showinfo("Sucess", "data inserted successfuly")




# app = tk.Tk()
# app.title("Product app")


# label_teachername = tk.Label(app, text="Teacher name")
# label_teachername.pack()

# entry_teacherName = tk.Entry(app)
# entry_teacherName.pack()

# label_teacherAge = tk.Label(app, text="Teacher age")
# label_teacherAge.pack()

# entry_teacherAge = tk.Entry(app)
# entry_teacherAge.pack()

# label_teacherPosition = tk.Label(app, text="Teacher Position")
# label_teacherPosition.pack()

# entry_teacherPosition = tk.Entry(app)
# entry_teacherPosition.pack()

# label_teacherSubject = tk.Label(app, text="Teacher Subject")
# label_teacherSubject.pack()

# entry_teacherSubject = tk.Entry(app)
# entry_teacherSubject.pack()

# label_teacherAddress = tk.Label(app, text="Teacher Address")
# label_teacherAddress.pack()

# entry_teacherAddress = tk.Entry(app)
# entry_teacherAddress.pack()

# submmit_button = tk.Button(app, text="Submite", command=on_summite)
# submmit_button.pack()

# app.mainloop()

def delete_data(id):
    cursor.execute("""DELETE FROM teacher WHERE id=?""",(id,))
    conn.commit()
    print("Delete successfuly")

delete_data(5)