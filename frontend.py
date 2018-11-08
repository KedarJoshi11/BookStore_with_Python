from tkinter import *
import backend

def view_command():
    list1.delete(0,END)#This deletes everything in the list from 0 to the end.
    for row in backend.view():
        list1.insert(END,row)
# This was done to make the entries appear line by line. Learn more about the methods used above.

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_entry.get(),author_entry.get(),year_entry.get(),isbb_entry.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_entry.get(),author_entry.get(),year_entry.get(),isbb_entry.get())
    list1.delete(0,END)#Delete 0 to END
    list1.insert(END,(title_entry.get(),author_entry.get(),year_entry.get(),isbb_entry.get()))#Insert new values at the END of the list.
# The Bind method in Tkinter is used to bind a function to a widget event.


def get_selected_row(event):
    try:
        global selected_tuple
        #index=list1.curselection()[0]
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        #selected_tuple=list1.get(index)
        #return(selected_tuple)
        e1.delete(0,END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_entry.get(), author_entry.get(), year_entry.get(), isbb_entry.get())


window=Tk() #This creates a window object.
window.wm_title("BookShelf")

l1=Label(window,text="Title")
l1.grid(row=0, column=0)

l2=Label(window,text="Author")
l2.grid(row=0, column=2)

l3=Label(window,text="Year")
l3.grid(row=1, column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1, column=2)

title_entry = StringVar()#This is the function that creates this special objectself.
e1=Entry(window,textvariable=title_entry)
e1.grid(row=0, column=1)

year_entry = StringVar()
e2=Entry(window,textvariable=year_entry)
e2.grid(row=1, column=1)

author_entry = StringVar()
e3=Entry(window,textvariable=author_entry)
e3.grid(row=0, column=3)

isbb_entry = StringVar()
e4=Entry(window,textvariable=isbb_entry)
e4.grid(row=1, column=3)

list1=Listbox(window, height=10, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
# The Bind method in Tkinter is used to bind a function to a widget event.
list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window, text="View All", width=16, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", width=16, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=16, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text = "Update Selection", width=16, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete Selection", width=16, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text = "Close", width=16, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop() #Prevents the created window from disappearing.
