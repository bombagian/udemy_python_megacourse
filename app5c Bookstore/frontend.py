from tkinter import *
import backend

def get_selected_row(event): #retrieve data for row selected in the listbox
	global selected_tuple #create a global variable 
	index=list1.curselection()[0] #get the index of the selected row 
	selected_tuple=list1.get(index) #get the data related to the index of the selected row

	#below code populate the entry boxes
	title_entry.delete(0,END)
	title_entry.insert(END,selected_tuple[1])
	author_entry.delete(0,END)
	author_entry.insert(END,selected_tuple[2])
	year_entry.delete(0,END)
	year_entry.insert(END,selected_tuple[3])
	isbn_entry.delete(0,END)
	isbn_entry.insert(END,selected_tuple[4])






def view_command():
	list1.delete(0,END) #empty the list from previous date before populate it
	for row in backend.view():
		list1.insert(END,row) #END indicates that the new row will be put at the end of the listbox



def search_command():
	list1.delete(0,END)
	for row in backend.search(title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get()):
		list1.insert(END,row)


def add_command():
	backend.insert(title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get())
	list1.delete(0,END)
	list1.insert(END,(title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get()))



def delete_command():
	backend.delete(selected_tuple[0])#retrieve the value from the global variable.
	view_command()


def update_command():
	backend.update(selected_tuple[0],title_txt.get(),author_txt.get(),year_txt.get(),isbn_txt.get()) #keep ID of selected row and send the changed values
	view_command()


window=Tk()
window.title("GB's Bookstore")

#create labels
title_lbl=Label(window,text="Title")
title_lbl.grid(row=0, column=0)
title_txt=StringVar() 
title_entry=Entry(window, textvariable = title_txt)
title_entry.grid(row=0,column=1)


author_lbl=Label(window,text="Author")
author_lbl.grid(row=0, column=2)
author_txt=StringVar() 
author_entry=Entry(window, textvariable = author_txt)
author_entry.grid(row=0,column=3)


year_lbl=Label(window,text="Year")
year_lbl.grid(row=1, column=0)
year_txt=StringVar() 
year_entry=Entry(window, textvariable = year_txt)
year_entry.grid(row=1,column=1)


isbn_lbl=Label(window,text="ISBN")
isbn_lbl.grid(row=1, column=2)
isbn_txt=StringVar() 
isbn_entry=Entry(window, textvariable = isbn_txt)
isbn_entry.grid(row=1,column=3)


#Listbox
list1=Listbox(window, height=8,width=40)
list1.grid(row=2,column=0, rowspan=7, columnspan=2)

#scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=7)

#configure the scroll assigning the list
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)



list1.bind('<<ListboxSelect>>', get_selected_row)



#create buttons
view_btn=Button(window,text="View All",width=12, command=view_command)
view_btn.grid(row=3,column=3)

search_btn=Button(window,text="Search Entry",width=12, command=search_command)
search_btn.grid(row=4,column=3)

add_btn=Button(window,text="Add Entry",width=12, command=add_command)
add_btn.grid(row=5,column=3)

update_btn=Button(window,text="Update",width=12,command=update_command)
update_btn.grid(row=6,column=3)

delete_btn=Button(window,text="Delete",width=12, command=delete_command)
delete_btn.grid(row=7,column=3)

close_btn=Button(window,text="Close",width=12,command=window.destroy)
close_btn.grid(row=8,column=3)

window.mainloop()