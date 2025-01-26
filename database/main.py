import sqlite3

conn = sqlite3.connect('database/collage.sqlite3')
cursor = conn.cursor()

def create_table():
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   email TEXT,
                   age INTEGER,
                   address TEXT
                   )
        """)
    conn.commit
    print("Table create successfully")

# create_table()

def inser_data(name,email,age,address):
    cursor.execute("""INSERT INTO
                students(name,email,age,address)VALUES(?,?,?,?)""",
                (name,email,age,address))
    conn.commit()
    print('Data inserted successsfully')

# name = input("Enter your name: ")
# email =input("Enater your email: ")    
# age = int(input("enter your age: "))
# address= input("enater your address: ")
# inser_data(name,email,age,address)


# def delete_data(id):
#     cursor.execute("""DELETE FROM students WHERE ID=?""",(id,))
#     conn.commit()
#     print("data deleted successfuly")

# delete_data(2)


def update_data(name,email,age,address,id):
    cursor.execute("""UPDATE students SET name=?,email=?,age=?,address=? WHERE id=?""",
                   (name,email,age,address,id))
    conn.commit()
    print("data update successfully")

update_data('jack','jack78@gamil.com','25','america',3)    
