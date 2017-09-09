from tkinter import *



window=Tk()
window.title("GB's Bookstore")

#create labels
title_lbl=Label(window,text="Title")
title_lbl.grid(row=0, column=0)
title_txt=StringVar() 
entry=Entry(window, textvariable = title_txt)
entry.grid(row=0,column=1)


author_lbl=Label(window,text="Author")
author_lbl.grid(row=0, column=2)
author_txt=StringVar() 
entry=Entry(window, textvariable = author_txt)
entry.grid(row=0,column=3)


year_lbl=Label(window,text="Year")
year_lbl.grid(row=1, column=0)
year_txt=StringVar() 
entry=Entry(window, textvariable = year_txt)
entry.grid(row=1,column=1)


isbn_lbl=Label(window,text="ISBN")
isbn_lbl.grid(row=1, column=2)
isbn_txt=StringVar() 
entry=Entry(window, textvariable = isbn_txt)
entry.grid(row=1,column=3)


#Listbox
list1=Listbox(window, height=8,width=40)
list1.grid(row=2,column=0, rowspan=7, columnspan=2)

#scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=7)

#configure the scroll assigning the list
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)



#create button
btn=Button(window,text="View All",width=12)
btn.grid(row=3,column=3)
#create button
btn=Button(window,text="Search Entry",width=12)
btn.grid(row=4,column=3)
#create button
btn=Button(window,text="Add Entry",width=12)
btn.grid(row=5,column=3)
#create button
btn=Button(window,text="Update",width=12)
btn.grid(row=6,column=3)
#create button
btn=Button(window,text="Delete",width=12)
btn.grid(row=7,column=3)

btn=Button(window,text="Close",width=12)
btn.grid(row=8,column=3)

window.mainloop()