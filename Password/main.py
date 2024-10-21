
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


        password_letters = [choice(letters) for _ in range(randint(8,10))]
        password_symbols = [choice(symbols) for _ in range(randint(2,4))]
        password_numbers= [choice(numbers) for _ in range(randint(2,4))]


        password_list=password_letters+password_symbols+password_numbers
        shuffle(password_list)

        password="".join(password_list)

        password_entry.insert(0,password)
        pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webiste=webiste_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data = {
        webiste: {
            "email":email,
            "password":password
        }
    }

    if not webiste or not password:
        messagebox.showinfo(title="remainder",message="YOU LEFT SOME FIELDS BEHIND")
    else:
            with open("data.json","r") as data_file:
                data=json.load(data_file)
                data.update(new_data)
                print(data)


            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
                webiste_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas=Canvas(height=200, width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label=Label(text="Email")
email_label.grid(row=2,column=0)
password_label=Label(text="Password")
password_label.grid(row=3,column=0)


webiste_entry=Entry(width=35)
webiste_entry.grid(row=1,column=1,columnspan=2)
webiste_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"abc@email.com")
password_entry=Entry(width=23)
password_entry.grid(row=3,column=1,pady=0)

generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)






window.mainloop()