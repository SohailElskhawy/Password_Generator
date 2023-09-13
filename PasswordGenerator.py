import random
import string
from tkinter import *

root=Tk()
root['background'] = "red"
root.title("Password Generator")
root.geometry('300x300')
symp = "!@#$%^&*()_+-"

def generate_password():
    password_label.delete(0,END)
    all_char = string.ascii_letters + string.digits + symp
    char_list =[]
    for i in range(10):
        char_list.append(all_char[random.randint(0,len(all_char)-1)])

    password = ''.join(char_list)
    password_label.insert(0,password)

app_label = Label(root,text="Password Generator",font=(30),fg="blue",bg="red")
app_label.pack()
password_label = Entry(root,font=(30))
password_label.pack()
generate_but = Button(root,text="Generate",fg="blue",bg="red",command=generate_password,font=(30))
generate_but.pack()
root.mainloop()