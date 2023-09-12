from tkinter import *
import random

root=Tk()
root.title("Password Generator")
root.geometry("400x400")

input_password = Entry(root)
old_label = Label(root)
np_label = Label(root)

array_3d =[[['I','J','K','L','M','N','O','P'],["King","Queen"],["!","@","#","$","%","^","&","*"]]]
print(array_3d[0][2][3])

def new_password():
    r1 = random.randint(0,7)
    r2 = random.randint(0,1)
    r3 = random.randint(0,7)
    
    letter1 =str(array_3d[0][0][r1])
    letter2 =(array_3d[0][1][r2])
    letter3 =(array_3d[0][2][r3])
    np_label["text"] = letter1 + "" + letter2 + "" + letter3
    old_label["text"] = "Old password : " + input_password.get()
    
btn = Button(root, text= "New Password", command = new_password)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

np_label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
input_password.place(relx = 0.5, rely = 0.7, anchor = CENTER)
old_label.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()