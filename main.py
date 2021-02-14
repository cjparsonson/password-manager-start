from tkinter import *
from tkinter import messagebox
import string
import secrets

# ---------------------------- Import Libraries ------------------------------------#


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
secretG = secrets.SystemRandom()
num_letters = secretG.randint(8, 10)
num_numbers = secretG.randint(2, 4)
num_symbols = secretG.randint(2, 4)

pword_letters = [secrets.choice(letters) for _ in range(num_letters)]
pword_numbers = [secrets.choice(numbers) for _ in range(num_numbers)]
pword_symbols = [secrets.choice(symbols) for _ in range(num_symbols)]

password_list = pword_letters + pword_numbers + pword_symbols
secretG.shuffle(password_list)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    is_valid = False if len(website) <= 0 or len(password) <= 0 else True
    if is_valid:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                    f"\nPassword: {password} \n Is it ok to save?")
        if is_ok:
            with open("pass_data.txt", "a") as file:
                new_entry = f"{website} | {email} | {password}\n"
                file.write(new_entry)
            entry_website.delete(0, "end")
            entry_password.delete(0, "end")
    else:
        messagebox.showinfo(title="Error", message="Please do not leave fields empty")

# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Canvas setup
canvas = Canvas(width=200, height=200, bg="white")
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1, sticky="W")

# Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Text Entries
entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "cjparsonson@gmail.com")
entry_password = Entry(width=25)
entry_password.grid(row=3, column=1, sticky="E")

# Buttons
button_generate = Button(text="Generate password", width=15)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", width=36, command=save)
button_add.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()
