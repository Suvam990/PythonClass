import sqlite3
import tkinter as tk
from tkinter import messagebox


product = sqlite3.connect("database/product_info.sqlite3")

cursor = product.cursor()


def create_tabel():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_info(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                    price INTEGER,
                   quntity INTEGER,
                   total INTEGER)""")
    product.commit()
    print("tabel created successfully!!")


def insert_product(name,price,quntity,total):
    cursor.execute("""
        INSERT INTO product_info(name,price,quntity,total) VALUES(?,?,?,?)""",
        (name,price,quntity,total))
    product.commit()
    print("data inserted successfully!")
          

def datas_insert():
    name = entry_name.get()
    price = 20000 

  
    if not name:
        messagebox.showerror("Input Error", "Product name cannot be empty!")
        return

    quantity = 0
    if entry_quntity.get():
        try:
            quantity = int(entry_quntity.get())
        except ValueError:
            messagebox.showerror("Input Error", "Invalid quantity! Please enter a number.")
            return

    total = price * quntity
    insert_product(name, price, quntity, total)
    messagebox.showinfo("Success", "Product added successfully!")
    
    
app=tk.Tk()
app.title("Pfoduct Info")



label_name = tk.Label(app, text="Product Name:")
label_name.pack()

entry_name = tk.Entry(app, width=30)
entry_name.pack()



label_price = tk.Label(app, text="Price: 20000")
label_price.pack()

# entry_price = tk.Entry(app, width=30)
# entry_price.pack()

label_quntity = tk.Label(app, text="quntity")
label_quntity.pack()

entry_quntity = tk.Entry(app, width=30)
entry_quntity.pack()

label = tk.Label(app, text="Product data")
label.pack()
submit_button = tk.Button(app, text="Submit", command=datas_insert())
submit_button.pack(pady=10)







app.mainloop()

# show_info()

# def show_records():
#     cursor.execute("SELECT id, name, quntity, price, (quntity * price) AS total FROM product_info")
#     records = cursor.fetchall()
#     print("ID| Name  | Quantity| Price| Total")
#     print("----------------------------------")
#     for record in records:
#         print(f"{record[0]} | {record[1]} | {record[2]}     |  {record[3]}  | {record[4]}")
# show_records()






