import tkinter as tk
from tkinter import *
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import os
import numpy as np
from cv2 import *
import random

window=Tk()
window.geometry("1200x800")
window.title("Image Encryption Decryption")
global count, emig

frp = []
tname = []
con = 1
bright = 0
panelB = None
panelA = None

#get the file name of image is selected
def getfilename(path):
    a = path.split(r'/')
    fname = a[-1]
    a = fname.split('.')
    # print(a)
    a = a[0]
    return a

#  get the path of the image
def getpath(path):
    a = path.split(r'/')
    # print(a)
    fname = a[-1]
    l = len(fname)
    location = path[:-l]
    return location

def openfilename():
    filename = filedialog.askopenfilename(title='Select File')
    return filename

def open_img():
    global x, panelA, panelB
    global count, eimg, location, filename
    count = 0
    x = openfilename() #Selected Image
    img = Image.open(x)
    eimg = img
    img = ImageTk.PhotoImage(img)
    temp = x
    location = getpath(temp)
    filename = getfilename(temp)
    # print(x)
    if panelA is None or panelB is None:
        panelA = Label(image=img)
        panelA.image = img
        panelA.pack(side="left", padx=10, pady=10)
        panelB = Label(image=img)
        panelB.image = img
        panelB.pack(side="right", padx=10, pady=10)
    else:
        panelA.configure(image=img)
        panelB.configure(image=img)
        panelA.image = img
        panelB.image = img

# Encrypt the selected image 
def en_fun():
    global x, image_encrypted, key
    # print(x)
    image_input = cv2.imread(x, 0)
    (x1, y) = image_input.shape
    image_input = image_input.astype(float) / 255.0
    # print(image_input)

    mu, sigma = 0, 0.1  # mean and standard deviation
    key = np.random.normal(mu, sigma, (x1, y)) + np.finfo(float).eps
    # print(key)
    image_encrypted = image_input / key
    cv2.imwrite('image_encrypted.jpg', image_encrypted * 255)

    imge = Image.open('image_encrypted.jpg')
    imge = ImageTk.PhotoImage(imge)
    panelB.configure(image=imge)
    panelB.image = imge
    mbox.showinfo("Encrypt Status", "Image Encryted successfully.")

# Decrypt function
def de_fun():
    global image_encrypted, key
    image_output = image_encrypted * key
    image_output *= 255.0
    cv2.imwrite('image_output.jpg', image_output)

    imgd = Image.open('image_output.jpg')
    imgd = ImageTk.PhotoImage(imgd)
    panelB.configure(image=imgd)
    panelB.image = imgd
    mbox.showinfo("Decrypt Status", "Image decrypted successfully.")


# function defined to same the edited image
def save_img():
    global location, filename, eimg
    print(filename)
    # eimg.save(location + filename + r"_edit.png")
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    eimg.save(filename)
    mbox.showinfo("Success", "Encrypted Image Saved Successfully!")


start1 = tk.Label(text = "Image Encryption\nDecryption", font=("Times New Roman", 38), fg="aquamarine4") # same way bg
start1.place(x = 335, y = 10)

# original image label
start1 = tk.Label(text = "Original\nImage", font=("Times New Roman", 35), fg="aquamarine3") # same way bg
start1.place(x = 90, y = 270)

# edited image label
start1 = tk.Label(text = "Encrypted/\nDecrypted\nImage", font=("Times New Roman", 35), fg="aquamarine3") # same way bg
start1.place(x = 700, y = 240)

# choose button 
chooseb = Button(window, text="Choose",command=open_img,font=("Times New Roman", 20), bg = "green", fg = "white", borderwidth=3, relief="raised")
chooseb.place(x =30 , y =20 )

# save button 
saveb = Button(window, text="Save",command=save_img,font=("Times New Roman", 20), bg = "green", fg = "white", borderwidth=3, relief="raised")
saveb.place(x =170 , y =20 )

# Encrypt button 
enb = Button(window, text="Encrypt",command=en_fun,font=("Times New Roman", 20), bg = "light green", fg = "blue", borderwidth=3, relief="raised")
enb.place(x =150 , y =620 )

# decrypt button 
deb = Button(window, text="Decrypt",command=de_fun,font=("Times New Roman", 20), bg = "orange", fg = "blue", borderwidth=3, relief="raised")
deb.place(x =750 , y =620 )


def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button 
exitb = Button(window, text="EXIT",command=exit_win,font=("Times New Roman", 20), bg = "red", fg = "white", borderwidth=3, relief="raised")
exitb.place(x =880 , y =20 )

window.mainloop()
