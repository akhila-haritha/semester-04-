import tkinter as tk

window = tk.Tk()
window.title("Entry widget")
window.geometry('650x500')

txt = tk.Entry(window,width=20)
txt.grid(column=1,row=0)

def clicked():
  res = "Welcome to  " + txt.get()
  submit.configure(text=res)

submit = tk.Button(window,text="Enter",command=clicked)
submit.place(x=100,y=25)

window.mainloop()
