from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation
all_characters = letters + digits + punctuation

def password_generator():
    password = ''
    for _ in range(10):
        password += random.choice(all_characters)
    generated_passwrod.insert(END, password)
    pyperclip.copy(generated_passwrod)
    return password

def save_to_file():
    website_url = website_entry.get()
    username = email_entry.get()
    password = generated_passwrod.get()

    if len(website_url) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Fill empty fields')
    else:
        is_ok = messagebox.askokcancel(title=website_url, message='Correct data?')
        
        if is_ok:
            with open("data.txt", 'a') as file:
                file.write(f"{website_url} | {username} | {password}\n")

            website_entry.delete(0, END)
            generated_passwrod.delete(0, END)


window = Tk()
window.title("Password Manager")
# window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
website_entry = Entry(width=45)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)
email_entry = Entry(width=45)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, "paul@mail.com")

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
generated_passwrod = Entry(width=25)
generated_passwrod.grid(column=1, row=3)
generate_button = Button(text="generate password", command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=40, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()