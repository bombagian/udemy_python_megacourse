'''
tkinter has 2 main elements:
1) window: is the container of the widgets (the frame)
2) widgets: all the objects that can be included in the frame (buttons, labels, etc..)

all code must be included between the definition of the window and the mainloop() method
'''

from tkinter import *


def convert():
    pd=float(entry_value.get())*2.20462
    gr=float(entry_value.get())*1000
    ou=float(entry_value.get())*35.274
    
    txtpounds.insert(END,pd)
    txtgrams.insert(END,gr)
    txtounc.insert(END,ou)


window=Tk()
window.title("Pippo")


#create label
lbl=Label(window,text="Kg.")
lbl.grid(row=0, column=0)


#create input text
entry_value=StringVar() 
entry=Entry(window, textvariable = entry_value)
entry.grid(row=0,column=1)


#create button
btn=Button(window,text="Convert",command = convert)
btn.grid(row=0,column=3)

#create output text
txtpounds=Text(window, height=1, width=10)
txtpounds.grid(row=1, column=0)


#create output text
txtgrams=Text(window, height=1, width=10)
txtgrams.grid(row=1, column=1)


#create output text
txtounc=Text(window, height=1, width=10)
txtounc.grid(row=1, column=2)


window.mainloop()



