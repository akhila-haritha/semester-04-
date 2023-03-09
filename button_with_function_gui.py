import tkinter as tk
window = tk.Tk()
window.title('Button')
window.geometry('650x500')

def clicked():
  submit.configure(text="The button was clicked!")

submit = tk.Tk(window,text="Click me!",fg="blue",bg="gray",font="Poppins",padx=2,pady=2,command=clicked)
submit.place(x=100,y=25)


window.mainloop()
