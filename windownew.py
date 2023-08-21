from tkinter import *

windows = Tk()
windows.title('Management Ssytem')
windows.geometry('490x240+200+200')
windows.resizable(0,0)

frame = Frame(windows,width=1000,height=1000,bg='black',bd=8)
frame.place(x=0,y=0)

heading = Label(frame,text='Congragulations',fg='#97ffff',bg='black',font=('Calibre',20,'bold'))
heading.place(x=140,y=3)

heading2 = Label(frame,text='You Have Learned A Lot',fg='yellow',bg='black',font=('Calibre',20,'bold'))
heading2.place(x=90,y=100)

windows.mainloop()