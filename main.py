from tkinter import *

# ---------------------------- Import Libraries ------------------------------------#


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Canvas setup
canvas = Canvas(width=200, height=200, bg="white")
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1, )

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
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)

# Buttons
button_generate = Button(text="Generate password", width=15)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", width=36)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
