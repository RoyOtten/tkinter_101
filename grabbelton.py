import random
import tkinter

window = tkinter.Tk()
window.geometry('300x300')
listitems = ['step','auto','fiets','bal','actiefiguur','laptop','pc','wc',]
 
def RandomGrabbel():
    if len(listitems) == 0:
        window.destroy()
    randomitem = random.choice(listitems) 
    listitems.remove(randomitem)
    label['text'] = randomitem
    
label = tkinter.Label()
label.pack()

button = tkinter.Button(text='Click Me!',command=RandomGrabbel)
button.pack()

window.mainloop()