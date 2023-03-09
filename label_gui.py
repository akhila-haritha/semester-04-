#Importing libraries
import tkinter as tk

#Creating a window
window = tk.Tk()
window.title("Student")
window.geometry('650x500')

#Adding a widget - Label
name = tk.Label(window,text="Name",bg="gray",font="Poppins",padx=2,pady=2).place(x=60,y=100)
reg_no = tk.Label(window,text="Registration Number",bg="gray",font="Poppins",padx=2,pady=2).place(x=60,y=140)
dept = tk.Label(window,text="Department",bg="gray",font="Poppins",padx=2,pady=2).place(x=60,y=180)
section = tk.Label(window,text="Section",bg="gray",font="Poppins",padx=2,pady=2).place(x=60,y=220)

#Creating an eventloop
window.mainloop()
