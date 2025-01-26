# import sqlite3


# conn = sqlite3.connect('database/product.sqlite3')

# cursor = conn.cursor()

# def create_table():
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS products(
#                    id INTEGER PRIMARY KEY AUTOINCREMENT,
#                    name TEXT,
#                    Model TEXT,
#                    Price INTEGER)""")
#     conn.commit()
#     print("table created!")

# create_table()

# def prodcut_data(name,Model,Price):
#     cursor.execute("""
#                 INSERT INTO
#                    products(name,Model,Price)VALUES(?,?,?)""",
#                    (name,Model,Price))
#     conn.commit()
#     print("data insert successfylly")


# name = input("Enter a product name: ")
# Model = input("Enter Model No: ")
# Price = int(input("enter price: "))
# prodcut_data(name,Model,Price)

import sqlite3
import tkinter as tk
from tkinter import messagebox

# Connect to SQLite3 database
conn = sqlite3.connect('database/product.sqlite3')
cursor = conn.cursor()

# Function to create table if not exists
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            Model TEXT,
            Price INTEGER
        )
    """)
    conn.commit()

# Function to insert product data into the database
def product_data(name, model, price):
    cursor.execute("""
        INSERT INTO products(name, Model, Price) VALUES(?, ?, ?)
    """, (name, model, price))
    conn.commit()
    messagebox.showinfo("Success", "Data inserted successfully!")

# Function to handle the form submission
def on_submit():
    name = entry_name.get()
    model = entry_model.get()
    try:
        price = int(entry_price.get())
        if name and model:
            product_data(name, model, price)
        else:
            messagebox.showwarning("Input Error", "Please enter all fields.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid price.")

# Create the table when the program starts
create_table()

# Set up the Tkinter window
root = tk.Tk()
root.title("Product Entry")

# Create input fields
label_name = tk.Label(root, text="Product Name:")
label_name.pack()

entry_name = tk.Entry(root, width=30)
entry_name.pack()

label_model = tk.Label(root, text="Model No:")
label_model.pack()

entry_model = tk.Entry(root, width=30)
entry_model.pack()

label_price = tk.Label(root, text="Price:")
label_price.pack()

entry_price = tk.Entry(root, width=30)
entry_price.pack()

# Create submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
