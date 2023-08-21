from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql

#windows size
windows = Tk()
windows.title('Password Reset Window')
#windows.geometry('540x640+200+10')
windows.geometry('500x550+100+0')
windows.resizable(0,0)

#database section

def submit():
    if usernameEntry.get()=='' or passwordEntry.get()=='' or confirmpasswordEntry.get=='':
        messagebox.showerror('All fields required')
    elif passwordEntry.get()!=confirmpasswordEntry.get():
        messagebox.showerror('Password Mismatch')
    else:
        db = pymysql.connect(host='localhost',user= 'root',password='Ayush@123',database='Personal_Registration_Form')
        cur = db.cursor()
        
        query = 'select * from P_details where username=%s'
        cur.execute(query,(usernameEntry.get()))
        row = cur.fetchone()
        if row == None:
            messagebox.showerror('Incorrect Username')
        else:
            query = 'update P_details set password=%s where username = %s'
            query1 = 'update P_details set confirmpassword=%s where username = %s'
            cur.execute(query,(passwordEntry.get(),usernameEntry.get()))
            cur.execute(query1,(confirmpasswordEntry.get(),usernameEntry.get()))
            
            db.commit()
            db.close()
            messagebox.showinfo('Success','Successfully Updated The Password')
            #windows.destroy()
            

    
        emailEntry.delete(0,END)
        usernameEntry.delete(0,END)
        passwordEntry.delete(0, END)
        confirmpasswordEntry.delete(0, END)

    

def show1():
    passwordEntry.configure(show='#')
    check1.configure(command=hide1)

def hide1():
    passwordEntry.configure(show='')
    check1.configure(command=show1)

def show2():
    confirmpasswordEntry.configure(show='#')
    check2.configure(command=hide2)

def hide2():
    confirmpasswordEntry.configure(show='')
    check2.configure(command=show2)

def bck():
    windows.destroy()
    import login_screen

#section for getting  data from the entry fields

email = StringVar()
username = StringVar()
password = StringVar()
confirmpassword = StringVar()


#frame
frame = Frame(windows,width=610,height=640,bg='black',bd=8)
frame.place(x=0,y=0)

#labels and entry fields

heading = Label(frame,text='Password Reset Window',fg= '#97ffff',bg='black',font=('Calibre',20,'bold'))
heading.place(x=90,y=3)

emaillbl = Label(frame,text='Email:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
emaillbl.place(x=10,y=150)

emailEntry = Entry(frame,width=30,borderwidth=2)
emailEntry.place(x=240,y=150)

usernamelbl = Label(frame,text='Username:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
usernamelbl.place(x=10,y=200)

usernameEntry = Entry(frame,width=30,borderwidth=2)
usernameEntry.place(x=240,y=200)

passwordlbl = Label(frame,text='Password:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
passwordlbl.place(x=10,y=250)

passwordEntry = Entry(frame,width=30,borderwidth=2)
passwordEntry.place(x=240,y=250)

confirmpasswordlbl = Label(frame,text='Confirm Password:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
confirmpasswordlbl.place(x=10,y=300)

confirmpasswordEntry = Entry(frame,width=30,borderwidth=2)
confirmpasswordEntry.place(x=240,y=300)

submitbtn = Button(frame,text='Submit',width=15,borderwidth=5,height=2,bg='#7f7fff',fg='white',cursor='hand2',border=2,font=('#57a1f8',16,'bold'),command=submit)
submitbtn.place(x=150,y=400)

bckbtn = Button(frame,text='<<',width=10,border=2,height=2,cursor='hand2',bg='black',fg='white',command=bck)
bckbtn.place(x=0,y=450)

#chekc buttons
check1 = Checkbutton(frame,text='',bg='black',command=show1)
check1.place(x=420,y=250)

check2 = Checkbutton(frame,text='',bg='black',command=show2)
check2.place(x=420,y=300)






windows.mainloop()