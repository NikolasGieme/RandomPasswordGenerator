import random
import pyperclip
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter.ttk import *
# Imports

window = ThemedTk(theme='breeze')
window.geometry("520x220")
window.title("Random Password Generator")
# Creating the window

global generated_password, password, strength, generated_password_list, encrypted_password_list, encrypted_password, list_chosen, characters
# Globals

lower = ["a", "b", "c", 'd', "e", 'f', "g", "h", "i", "j", "k", 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
upper = ["A", "B", "C", 'D', "E", "F", "G", "H", "I", "J", "K", 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', "a", "b", "c", 'd', "e", "f", "g", "h", "i", "j", "k", 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ["A", "B", "C", 'D', "E", "F", "G", "H", "I", "J", "K", 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z', "a", "b", "c", 'd', "e", "f", "g", "h", "i", "j", "k", 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$',
          '%', '^', '&', '*', '(', ')']
generated_password_list = []
encrypted_password_list = []
encrypted_password = ""
generated_password = ""
list_chosen = ""
strength = IntVar()
variable = StringVar()
characters = 0
# Creating lists and variables


def Characters(*args):
    global characters, number_of_characters
    # Global

    if number_of_characters.get() != "Select Characters":
        characters = int(number_of_characters.get())


def Generate():
    global generated_password, password, strength, generated_password_list, encrypted_password_list, encrypted_password, list_chosen, characters
    # Globals

    random_number = 0
    password.delete(0, END)
    generated_password_list.clear()
    generated_password = ""
    encrypted_password = ""
    # Resetting variables, lists and entries

    if strength.get() == 1:
        list_chosen = lower
    elif strength.get() == 2:
        list_chosen = upper
    elif strength.get() == 3:
        list_chosen = digits
    # Choosing one of three lists depending on the password's strength

    for i in range(0, characters):
        random_number = random.randint(0, len(list_chosen) - 1)
        generated_password += list_chosen[random_number]
        generated_password_list.append(random_number)
    # Creating a random password

    password.insert(END, generated_password)


def Copy(f):
    global password, encryption
    # Globals

    if f == 0:
        pyperclip.copy(str(password.get()))
    elif f == 1:
        pyperclip.copy(str(encryption.get()))
    # Copying the passwords in the user's clipboard


def Encrypt():
    global encrypted_password, encrypted_password_list, generated_password_list, list_chosen, encryption
    # Globals

    encryption.delete(0, END)
    encrypted_password_list.clear()
    # Clearing the list and the entry used in this function

    encrypted_password_list.append(generated_password_list[0])
    if encrypted_password_list[0] <= len(list_chosen):
        encrypted_password += list_chosen[encrypted_password_list[0]]
    else:
        encrypted_password += list_chosen[encrypted_password_list[0] - len(list_chosen)]
    # Setting the first digit or letter for the encrypted password and password list

    for i in range(1, len(generated_password_list)):
        encrypted_password_list.append(generated_password_list[i - 1] + generated_password_list[i])
        if encrypted_password_list[i] < len(list_chosen):
            encrypted_password += list_chosen[encrypted_password_list[i]]
        else:
            encrypted_password += list_chosen[encrypted_password_list[i] - len(list_chosen)]
    # Encrypting the password based on a pattern

    encryption.insert(END, encrypted_password)


Label(window, text="Random Password Generator").grid(row=0, column=0, columnspan=6)
Label(window, text="Password").grid(row=1, column=0)
Label(window, text="Encrypted\nPassword").grid(row=6, column=0)
Label(window, text="Select Strength").grid(row=2, column=3)
# Creating labels

password = ttk.Entry(window)
password.insert(END, generated_password)
password.grid(row=1, column=1)
# Creating password entry

encryption = ttk.Entry(window)
encryption.insert(END, encrypted_password)
encryption.grid(row=6, column=1)
# Creating encrypted password entry

variable.trace("w", Characters)
number_of_characters = ttk.Combobox(window, textvar=variable)
number_of_characters["values"] = ("Select Characters", "6", "8", "10", "12")
number_of_characters.current(0)
number_of_characters.grid(row=2, column=1)
# Creating a menu from which to choose the number of characters

radiobutton = ttk.Radiobutton(window, text="Weak", value=1, var=strength)
radiobutton.grid(row=3, column=3)
radiobutton1 = ttk.Radiobutton(window, text="Medium", value=2, var=strength)
radiobutton1.grid(row=4, column=3)
radiobutton2 = ttk.Radiobutton(window, text="Strong", value=3, var=strength)
radiobutton2.grid(row=5, column=3)
# Creating radiobuttons for the user to choose the password's strength

copy = ttk.Button(window, text="Copy", command=lambda: Copy(0))
copy.grid(row=1, column=2)
copy1 = ttk.Button(window, text="Copy", command=lambda: Copy(1))
copy1.grid(row=6, column=2)
# Creating the "Copy" buttons

generate = ttk.Button(window, text="Generate", command=Generate)
generate.grid(row=1, column=3)
encrypt = ttk.Button(window, text="Encrypt", command=Encrypt)
encrypt.grid(row=1, column=4)
# Creating the "Generate" and "Encrypt" buttons

cb = ttk.Button(window, text="Exit", command=lambda: window.quit())
cb.grid(row=6, column=3)
# Creating the "Exit" button

window.mainloop()
