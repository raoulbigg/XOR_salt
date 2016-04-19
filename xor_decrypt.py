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
    string_label = Label(root, text="String to decrypt: ").grid(row=1, column=1)
    string_entry = Entry(root, textvariable=string).grid(row=2, column=1)
#KEY
    key_label = Label(root, text="Key to use: ").grid(row=3, column=1)
    key_entry = Entry(root, textvariable=key1).grid(row=4, column=1)
    string_button = Button(root, text="decrypt", fg = "Black", command=lambda: key() ).grid(row=5, column=1)


def key():#key
#Get StrinVar() value
    xor_text.delete(1.0, END)
    key = key1.get()
    key = key *1000
    string1 = string.get()
    string1 = string1.decode("hex")
#String == ascii
    for q in range(len(string1)):
        string_ord.append(ord(string1[q]))
#Key == ascii
    for r in range(len(key)):
        key_ord.append(ord(key[r]))
    crypt = string_ord
    xor(crypt, string1)

def xor(crypt, string1):#encryption with XOR
#XOR = String ^ key
    try:
        for p in range(len(crypt)):
            crypt[p] ^=  key_ord[p]
    except Exception:
        print "Incorrect string or key"
        root.mainloop()
    decrypted =  ''.join(map(chr,crypt))
    f = open("decrypted.txt", "wb+")
    f.write(decrypted[32:])
    f.close()

    xor_text.insert(INSERT,"\n" + "Decrypted w/o salt: " + decrypted[32:] + "\n")
    xor_text.insert(INSERT, "+--------------------------+")
    xor_text.insert(INSERT,"\n" + "Decrypted.txt is saved in the local folder" +"\n")
    xor_text.insert(INSERT, "+--------------------------+")
    xor_text.grid(row=6, column=1)

    del IV_ord[:]
    del string_ord[:]
    del key_ord[:]

if __name__ == '__main__':
    string_input()
    root.mainloop()
