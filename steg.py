from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography
from tkinter import*
from tkinter import ttk
import Tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import time,subprocess
import os
from A import AESCipher
root=Tk()
root.title("Secure STEGANOGRAPHY 'CODED BY:Ismael Al-safadi' ")
AES_KEY = ttk.Entry(root, width=50)
AES_KEY.grid(row=1, column=1, columnspan=2, pady=10)
def filename():
    global path
    path = askopenfilename()
    return path    
TextComments=Text(root,width=35, height=15, font = ('Arial', 12))
TextComments.grid(row=3, column=1,columnspan=2)
ttk.Label(root,text="Message:").grid(row=3, column=0)
buButton=ttk.Button(root,text="Submit")
buButton.grid(row=7,column=3)
var = IntVar()
ttk.Radiobutton(root, text="Hide", variable=var, value=1).grid(row=7, column=1)
ttk.Radiobutton(root, text="Show", variable=var, value=2).grid(row=7, column=2)
ttk.Label(root, text="key").grid(row=1, column=0, pady=10, padx=10)
Name = ttk.Entry(root, width=50)
Name.grid(row=1, column=1, columnspan=2, pady=10)
w = Label(root, text="Secret steganography tool", font=("Secret Steganography", 16,"bold italic"))
w.grid(row=0, column=1)
def ButtonClick(filename):
    try:
        key_key=Name.get()
        message=(TextComments.get(1.0,'end'))
        choice=var.get()
        if choice==1:
            messagebox.showinfo(title="Wait", message="Please wait it will take a minute")
            encrypted_message=AESCipher(key_key).encrypt(message)
            Steganography.encode(path, "secret.jpg", encrypted_message)
            messagebox.showinfo(title="Done", message="Done ^__^ Your message is secure")

        elif choice ==2:
            try:
                secret_text = Steganography.decode(path)
                decrypted_text=AESCipher(key_key).decrypt(secret_text)
            except:
                messagebox.showerror("Wrong password!", "Wrong password ! Please try again ")
            if (decrypted_text =="") or (decrypted_text==" "):
                messagebox.showerror("Wrong password!", "Wrong password ! Please try again ")
            else:
                open_open=open("secure_message.txt","w")
                open_open.writelines(decrypted_text)
                open_open.close()
                messagebox.showinfo(title="Done", message="Done ^__^ Your message was stored in file named'secure_message.txt' in this folder")
    except:
        messagebox.showerror("Ops!", "ERROR!!")        
buButton1 = ttk.Button(root, text="browse")
buButton1.grid(row=7, column=0)
buButton1.config(command=filename)    
buButton.config(command=lambda:ButtonClick(filename))
root.mainloop()
