import tkinter as tk



app = tk.Tk()
app.title("From")
app.geometry("600x400")

user_name = tk.Label(app, text="Enter a Usernmae")
user_name.pack()
user = tk.Entry(app)
user.pack()

password = tk.Label(app, text = "enter a password")
password.pack()
pass_word = tk.Entry(app)
pass_word.pack()


def data():

    Username = user.get().strip()
    Password = pass_word.get().strip()
    with open("dataRecord.txt", "a") as db:
    
     db.write(f"{Username},{Password}\n")
    

button = tk.Button(app, text="confirm", command=data)
button.pack()
    


app.mainloop()

