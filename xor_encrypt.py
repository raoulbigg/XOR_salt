import uuid
import hashlib
from Tkinter import *
import ttk
import time
 
#Variables 
IV_ord = []
string_ord = []
key_ord = []

#Tkinter
root = Tk()
xor_text = Text(root)
xor_text.grid(row=6, column=1)

#Tkinter variables
string = StringVar()
key1 = StringVar()



def string_input():#plaintext
#STRING
    string_label = Label(root, text="String to encrypt: ").grid(row=1, column=1)
    string_entry = Entry(root, textvariable=string).grid(row=2, column=1)
#KEY
    key_label = Label(root, text="Key to use: ").grid(row=3, column=1)
    key_entry = Entry(root, textvariable=key1).grid(row=4, column=1)
    string_button = Button(root, text="encrypt", fg = "Black", command=lambda: salt() ).grid(row=5, column=1)

def salt():
#IV(SALT)
    IV = uuid.uuid4().hex
    for i in range(len(IV)):
        IV_ord.append(ord(IV[i]))
    xor_text.insert(INSERT,"Salt: " + IV + "\n" )
    xor_text.grid(row=6, column=1)
    xor_text.delete(1.0, END)
    key(IV)

def key(IV):#key
#Get StrinVar() value

    key = key1.get()
    key = key *1000
    string1 = string.get()
#String == ascii
    for q in range(len(string1)):
        string_ord.append(ord(string1[q]))
#Key == ascii
    for r in range(len(key)):
        key_ord.append(ord(key[r]))
    crypt = IV_ord + string_ord
    xor(crypt, string1, IV)

def xor(crypt, string1, IV):#encryption with XOR
#XOR = String ^ key
    try:
        for p in range(len(crypt)):
            crypt[p] ^=  key_ord[p]
    except Exception:
        xor_text.insert(INSERT,"Incorrect String and or Key")
        root.mainloop()
    encrypted =  ''.join(map(chr,crypt))
    xor_text.insert(INSERT,"Encrypting: " + string1 + "\n")
    xor_text.insert(INSERT,"With salt: " + str(IV) +"\n")
    xor_text.insert(INSERT, "\n+--------------------------+"+"\n")
    xor_text.insert(INSERT, "Encrypted.txt is saved in the local folder\n")
    xor_text.insert(INSERT, "\n+--------------------------+")
    xor_text.grid(row=6, column=1)

    f = open("encrypted.txt", "wb+")
    f.write(encrypted.encode("hex"))
    f.close()

    del IV_ord[:]
    del string_ord[:]
    del key_ord[:]

if __name__ == '__main__':
    string_input()
    root.mainloop()
