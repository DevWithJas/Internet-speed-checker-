from cgitb import grey
import math
import tkinter as tk
from tkinter import messagebox
from turtle import speed 
from PIL import Image, ImageTk
import pyspeedtest 


root = tk.Tk()
root.geometry("300x450")
root.resizable(0,0)
root.title("Internet download speed")
root.iconbitmap("D:\\PYTHON BASIC PROJECTS\\Intenet speed checking tool\\Antenna.ico")
from tkinter import messagebox 

#creating function
st = pyspeedtest.SpeedTest("www.google.com")
def SpeedTest():
    speed = str(math.floor(st.download()/1000)) + "Kb/s"
    messagebox.showinfo(speed)

#logo
logo = Image.open("D:\\PYTHON BASIC PROJECTS\\Intenet speed checking tool\\Internetdownload_Internet_10807.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.pack()

new_label = tk.Label(root, text = "Test download speed", font=("Areal",18,"bold"),fg="green")
new_label.pack(padx=20,pady=20)

#creating Buttons 
button1 = tk.Button(root,text="check",command= SpeedTest ,font=("Areal",18,))
button1.pack(padx=10,pady=10)
button2 = tk.Button(root,text="Exit",command = root.destroy, font=("Areal",20,))
button2.pack(padx=20,pady=10)

#creating label 
new_label2 = tk.Label(root, text= "Thanks", font=("Areal",20,"bold"), bg = "black", fg="white")
new_label2.pack(padx=10,pady=10, fill="both", expand=True)



root.mainloop()
