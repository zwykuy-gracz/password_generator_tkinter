from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json

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
    new_data = {website_url.lower(): {
        'email': username,
        'password': password,
    }}

    if len(website_url) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Fill empty fields')
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            generated_passwrod.delete(0, END)

def search_website():
    website_url = website_entry.get()
    website = website_url.lower()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No data file found")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website.title(), message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showinfo(title='Error', message=f"No details for {website} exists.")

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
website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)
website_entry.focus()
website_button = Button(text='Search', width=15, command=search_website)
website_button.grid(column=2, row=1)

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