#Importing libraries
import tkinter as tk

#Creating a window
window = tk.Tk()
window.title('Student Record Application')
window.geometry('550x450')

#Adding widgets
Name = tk.Label(window,text="Name",padx=30,pady=0,font="calibri",fg="black")
Name.grid(row=0,column=0)
txt_name = tk.Entry(window,width=20)
txt_name.grid(row=0,column=20)


id = tk.Label(window,text="ID",padx=30,pady=0,font="calibri",fg="black")
id.grid(row=0,column=60)
txt_id = tk.Entry(window,width=20)
txt_id.grid(row=0,column=80)



major = tk.Label(window,text="Major",padx=30,pady=0,font="calibri",fg="black")
major.grid(row=20,column=0)
txt_major = tk.Entry(window,width=20)
txt_major.grid(row=20,column=20)


age = tk.Label(window,text='Age',padx=30,pady=0,font="calibri",fg="black")
age.grid(row=20,column=60)
txt_age = tk.Entry(window,width=20)
txt_age.grid(row=20,column=80)


sex = tk.Label(window,text="Sex",padx=30,pady=0,font="calibri",fg="black")
sex.grid(row=40,column=0)
txt_sex = tk.Entry(window,width=20)
txt_sex.grid(row=40,column=20)

address = tk.Label(window,text="Address",padx=30,pady=0,font="calibri",fg="black")
address.grid(row=40,column=60)
txt_address = tk.Entry(window,width=20)
txt_address.grid(row=40,column=80)

gpa = tk.Label(window,text="GPA",padx=30,pady=0,font="calibri",fg="black")
gpa.grid(row=60,column=0)
txt_gpa = tk.Entry(window,width=20)
txt_gpa.grid(row=60,column=20)


#adding buttons
view_all = tk.Button(window,text="View All",width=11,fg="black",padx=30,pady=0,font="calibri")
search_entry = tk.Button(window,text="Search Entry",fg="black",padx=30,pady=0,font="calibri")
add_entry = tk.Button(window,text="Add Entry",fg="black",padx=30,pady=0,width=11,font="calibri")
update_selected = tk.Button(window,text="Update Selected",fg="black",pady=0,padx=30,width=11,font="calibri")
del_selected = tk.Button(window,text="Delete Selected",fg="black",pady=0,padx=30,width=11,font="calibri")
close = tk.Button(window,text="Close",fg="black",padx=30,width=11,pady=0,font="calibri")
view_all.place(x=320,y=150)
search_entry.place(x=320,y=190)
add_entry.place(x=320,y=230)
update_selected.place(x=320,y=270)
del_selected.place(x=320,y=310)
close.place(x=320,y=350)



#adding srolltext widget
from tkinter import scrolledtext

p = scrolledtext.ScrolledText(window,width=37,height=10)
p.place(x=0,y=222)



window.mainloop()


