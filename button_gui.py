#Importing libraries
import tkinter as tk

#Creating a window
window = tk.Tk()
window.title('Learning about Button widget')
windoe.geometry('650x500')

#Adding a widget 
submit = tk.Button(window,title="Click me!",fg="Blue",bg="gray",padx=2,pady=2,font="Poppins")
submit.place(x=100,y=25)    

#Creating a mainloop
window.mainloop()
