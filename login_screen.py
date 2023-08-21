from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
#windows
windows = Tk()
windows.title('Login Window')
windows.resizable(0,0)
windows.geometry('490x240+200+200')

#database
def login():
    if emailEntry.get()=='':
        messagebox.showerror('Alert','Please enter your email')
    elif passwordEntry.get()=='':
        messagebox.showerror('Alert','Please enter your password')

    else:
        db = pymysql.connect(host='localhost',user= 'root',password='Ayush@123',database='Personal_Registration_Form')
        cur = db.cursor()
        
        query = 'select * from P_details where email=%s'
        cur.execute(query,(emailEntry.get()))
        row = cur.fetchone()
        
        query2 = 'select * from P_details where password=%s'
        cur.execute(query2,(passwordEntry.get()))
        row1 = cur.fetchone()

        #if row == None and row1 == None:
        if row == None:
        
            messagebox.showerror('Alert','Incorrect email or password')
            return 
        elif row1 == None:
            messagebox.showerror('Alert','Incorrect email or password')
        else:
            messagebox.showinfo('Success','Login Successful')
            import windownew

        emailEntry.delete(0,END)
        passwordEntry.delete(0,END)

        #windows.destroy()
        #import windownew

#check button configuration
def show():
    passwordEntry.configure(show='*')
    check.configure(command=hide,text='')

def hide():
    passwordEntry.configure(show='')
    check.configure(command=show,text='')
    
#event/binding

def On_FocusEmailIn(event):
    emailEntry.delete(0,END)

def On_FocusEmailOut(event):
    name=emailEntry.get()
    if name == '':
        emailEntry.insert(0,'Email')

def On_FocusPasswordIn(event):
    passwordEntry.delete(0,END)

def On_FocusPasswordOut(event):
    name = passwordEntry.get()
    if name == '':
        passwordEntry.insert(0,'Password')

def newone():
    windows.destroy()
    import Personal_Registration_Form

def fgtpass():
    windows.destroy()
    import forgotpass
#frame
frame = Frame(windows,width=700,height=400,bg='black')
frame.place(x=0,y=0)

#Lable
LogoImage = PhotoImage(file='Gmail-logo.png')
emailLabel = Label(frame,text='Email:',fg='#97ffff',image=LogoImage,compound=LEFT,bg='black',
                   font=('Calibre',14,'bold'))
emailLabel.grid(row=1,column=0,pady=20,padx=3)

passwordImage = PhotoImage(file='padlock.png')
passwordLabel = Label(frame,text='Password:',fg='#97ffff',image=passwordImage,compound=LEFT,bg='black',
                   font=('Calibre',14,'bold'))
passwordLabel.grid(row=3,column=0,pady=10,padx=3)

#entry fields

emailEntry = Entry(frame,width=39,bd=3)
emailEntry.grid(row=1,column=2,columnspan=2,padx=57)

passwordEntry = Entry(frame,width=39,bd=3)
passwordEntry.grid(row=3,column=2,columnspan=2)

loginbtn = Button(frame,text='LOGIN',bg='#7f7fff',pady=10,width=23,fg='white',font=('open sans',9,'bold'),
                  cursor='hand2',border=0,borderwidth=5,command=login)
loginbtn.grid(row=9,columnspan=5,pady=30)

donthaveacctLabel = Label(frame,text = 'Dont\'t have an account?',fg='#97ffff',bg='black',pady=4,
                          font=('Harrington', 9,'bold'))
donthaveacctLabel.place(x=0,y=170)

createnewacct = Button(frame,width=15,text='Create One',border=0,bg='white',cursor='hand2',fg='black',font=('tahoma',8,'bold'),command=newone)
createnewacct.place(x=10,y=199)

fogtpw = Button(frame,text='Forgot Password?',fg='#97ffff',border=0,cursor='hand2',bg='black',font=('Harrington',9,'bold'),command=fgtpass)
fogtpw.place(x=310,y=140)

#string information

emailEntry.insert(0,'@email.com')
passwordEntry.insert(0,'password')

#event binding

emailEntry.bind('<FocusIn>',On_FocusEmailIn)
emailEntry.bind('<FocusOut>',On_FocusEmailOut)

passwordEntry.bind('<FocusIn>',On_FocusPasswordIn)
passwordEntry.bind('<FocusOut>',On_FocusPasswordOut)

#check box

check = Checkbutton(frame,text='',bg='black',command=show)
check.place(x=440,y=110)
windows.mainloop()