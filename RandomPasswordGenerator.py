import random
import pyperclip
from tkinter import *
window = Tk()
window.geometry("400x200")
window.title("Random Password Generator")
global a, password, k, rb1, bb, cc, enc, aa
lower = ["a", "b", "c", 'd', "e", 'f', "g", "h", "i", "j", "k", 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ["A", "B", "C", 'D', "E", "F", "G", "H", "I", "J", "K", 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "a", "b", "c", 'd', "e", "f", "g", "h", "i", "j", "k", 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ["A", "B", "C", 'D', "E", "F", "G", "H", "I", "J", "K", 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', "a", "b", "c", 'd', "e", "f", "g", "h", "i", "j", "k", 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
bb = []
cc = []
enc = ""
password = ""
Label(window, text="Random Password Generator").grid(row=0, column=0, columnspan=6)
Label(window, text="Password").grid(row=1, column=0)
Label(window, text="Encrypted\nPassword").grid(row=4, column=0)
kk = Entry(window)
kk.insert(END, enc)
kk.grid(row=4, column=1)
rb = IntVar()
rb1 = IntVar()
k = Entry(window)
k.insert(END, password)
k.grid(row=1, column=1)
a = 0
aa = ""


def Gen():
    global a, password, k, rb1, bb, cc, enc, aa
    k.delete(0, END)
    bb.clear()
    password = ""
    enc = ""
    if rb1.get() == 1:
        aa = lower
    elif rb1.get() == 2:
        aa = upper
    elif rb1.get() == 3:
        aa = digits
    for i in range(0, int(rb.get())):
        a = random.randint(0, len(aa)-1)
        password = password + aa[a]
        bb.append(a)
    k.insert(END, password)


def Copy(f):
    global k, kk
    if f == 0:
        pyperclip.copy(str(k.get()))
    elif f == 1:
        pyperclip.copy(str(kk.get()))


def Enc():
    global enc, cc, bb, aa, kk
    kk.delete(0, END)
    cc.clear()
    cc.append(bb[0])
    if cc[0] <= len(aa):
        enc = enc + aa[cc[0]]
    else:
        enc = enc + aa[cc[0] - len(aa)]
    for i in range(1, len(bb)):
        cc.append(bb[i - 1] + bb[i])
        if cc[i] < len(aa):
            enc = enc + aa[cc[i]]
        else:
            enc = enc + aa[cc[i] - len(aa)]
    kk.insert(END, enc)


r = Radiobutton(window, text="characters: 6", value=6, var=rb)
r.grid(row=2, column=1)
ra = Radiobutton(window, text="8", value=8, var=rb)
ra.grid(row=2, column=2)
re = Radiobutton(window, text="10", value=10, var=rb)
re.grid(row=2, column=3)
rc = Radiobutton(window, text="12", value=12, var=rb)
rc.grid(row=2, column=4)
r1 = Radiobutton(window, text="Weak", value=1, var=rb1)
r1.grid(row=3, column=1)
ra1 = Radiobutton(window, text="Medium", value=2, var=rb1)
ra1.grid(row=3, column=2)
rc1 = Radiobutton(window, text="Strong", value=3, var=rb1)
rc1.grid(row=3, column=3)
b = Button(window, text="Copy", command=lambda: Copy(0))
b.grid(row=1, column=2)
ba = Button(window, text="Copy", command=lambda: Copy(1))
ba.grid(row=4, column=2)
c = Button(window, text="Generate", command=Gen)
c.grid(row=1, column=3)
ca = Button(window, text="Encrypt", command=Enc)
ca.grid(row=1, column=4)
cb = Button(window, text="Exit", command=lambda: window.quit())
cb.grid(row=4, column=3)
window.mainloop()
