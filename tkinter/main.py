import tkinter as tk

app = tk.Tk()
app.title("Calculater")

app.geometry("600x400")

fn = tk.Label(app, text="enter a firts number")
fn.pack()
n1 = tk.Entry(app)
n1.pack()
sn = tk.Label(app, text="Enter a second number")
sn.pack()
n2 = tk.Entry(app)
n2.pack()
resutl = tk.Label(app, text="result")
resutl.pack()

def add():
    first_number = int(n1.get())
    second_number = int(n2.get())

    total = first_number + second_number
    resutl.config(text="Result: " + str(total))
    n1.delete(0, tk.END)
    n2.delete(0, tk.END)

button = tk.Button(app, text ="add number", command=add)    
button.pack()

app.mainloop()