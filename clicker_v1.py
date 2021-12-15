from tkinter import *
root = Tk()

#variable is stored in the root object
root.counter = 0

def clicked():
    root.counter += 1
    L['text'] = 'Button clicked: ' + str(root.counter)
    
def clickedDown():
    root.counter -= 1
    L['text'] = 'button clicked: ' + str(root.counter) 
        
b = Button(root, text="up", command=clicked)
b.pack()

c = Button(root,text= "button down", command= clickedDown)
c.pack() 

L = Label(root, text="No clicks yet.")
L.pack()

root.mainloop()