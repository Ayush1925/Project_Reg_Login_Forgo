from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql

#windows size
windows = Tk()
windows.title('Personal Registration Form')
windows.geometry('540x640+200+10')
windows.resizable(0,0)

#database section

def submit():
    if firstnameEntry.get() == '':
        messagebox.showerror('Alert!','Please Enter Your First Name')
    elif lastnameEntry.get()=='':
        messagebox.showerror('Alert!','Please Enter Your Last Name')
    elif emailEntry.get()=='':
        messagebox.showerror('Alert!','Please Enter Your Email')
    elif gender.get()=='':
        messagebox.showerror('Alert!','Please Select Your Gender')
    elif OM.get()=='':
        messagebox.showerror('Alert!','Please Select Your Country')
    elif usernameEntry.get()=='':
        messagebox.showerror('Alert!','Please Enter Your Username')
    elif passwordEntry.get()=='':
        messagebox.showerror('Alert!','Please Enter Your Password')
    elif confirmpasswordEntry.get()=='':
        messagebox.showerror('Alert!','Please Confirm Your Password')

    elif passwordEntry.get()!=confirmpasswordEntry.get():
        messagebox.showerror('Alert!','Password Do Not Match')

    else:
        db = pymysql.connect(host='localhost',user= 'root',password='Ayush@123',database='Personal_Registration_Form')
        cur = db.cursor()
        
        try:
            query = 'create database Personal_Registration_Form'
            cur.execute(query)
            query = 'use Personal_Registration_Form'
            cur.execute(query)
        
            query = 'create table P_details(id int auto_increment primary key not null,firstname varchar(40),lastname varchar(40),'\
              'email varchar(40),gender varchar(10),country varchar(30),username varchar(30),password varchar(30),'\
              'confirmpassword varchar(30))'
            
            cur.execute(query)
            messagebox.showinfo('Success','Fields Created Successfully')

        except:
            cur.execute('use Personal_Registration_Form')
            query = 'insert into P_details(firstname,lastname,email,gender,country,username,password,'\
            'confirmpassword) values(%s,%s,%s,%s,%s,%s,%s,%s)'

            cur.execute(query,(firstnameEntry.get(),lastnameEntry.get(),emailEntry.get(),gender.get(),OM.get(),usernameEntry.get(),passwordEntry.get(),
                               confirmpasswordEntry.get()))
            
            db.commit()
            db.close()
            messagebox.showinfo('Success','Successful Registration')

            firstnameEntry.delete(0,END)
            lastnameEntry.delete(0,END)
            emailEntry.delete(0,END)
            gender.set(0)
            OM.set(0)
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

firstname = StringVar()
lastname = StringVar()
email = StringVar()
gender = StringVar()
OM = StringVar()
username = StringVar()
password = StringVar()
confirmpassword = StringVar()


#frame
frame = Frame(windows,width=610,height=640,bg='black',bd=8)
frame.place(x=0,y=0)

country = ['Algeria','Australia','Bahamas','Caneda','Denmark','Egypt','France','India','Poland','Brazil']
OM.set('Select Country')
#labels and entry fields

heading = Label(frame,text='Personal Registration Form',fg= '#97ffff',bg='black',font=('Calibre',20,'bold'))
heading.place(x=90,y=3)

firstnamelbl = Label(frame,text='First Name:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
firstnamelbl.place(x=10,y=70)

firstnameEntry = Entry(frame,width=30,borderwidth=2)
firstnameEntry.place(x=240,y=70)

lastnamelbl = Label(frame,text='Last Name:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
lastnamelbl.place(x=10,y=110)

lastnameEntry = Entry(frame,width=30,borderwidth=2)
lastnameEntry.place(x=240,y=110)

emaillbl = Label(frame,text='Email:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
emaillbl.place(x=10,y=150)

emailEntry = Entry(frame,width=30,borderwidth=2)
emailEntry.place(x=240,y=150)

genderlbl = Label(frame,text='Select Gender:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
genderlbl.place(x=10,y=200)

gender.set(0)
genderRadio1 = Radiobutton(frame,text='Male',variable=gender,value='Male',font='Tahoma 13 bold')
genderRadio1.place(x=240,y=200)

genderRadio2 = Radiobutton(frame,text='Female',variable=gender,value='Female',font='Tahoma 13 bold')
genderRadio2.place(x=350,y=200)

countryLableDropdown = Label(frame,text='Select Country:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
countryLableDropdown.place(x=10,y=250)

countryLabelDropdown = OptionMenu(frame,OM,*country)
countryLabelDropdown.place(x=240,y=250)

countryLabelDropdown.config(width=18,font=('Calibre',13,'bold'),fg='black')

usernamelbl = Label(frame,text='Username:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
usernamelbl.place(x=10,y=300)

usernameEntry = Entry(frame,width=30,borderwidth=2)
usernameEntry.place(x=240,y=300)

passwordlbl = Label(frame,text='Password:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
passwordlbl.place(x=10,y=350)

passwordEntry = Entry(frame,width=30,borderwidth=2)
passwordEntry.place(x=240,y=350)

confirmpasswordlbl = Label(frame,text='Confirm Password:',fg='#97ffff',bg='black',font=('Calibre',15,'bold'))
confirmpasswordlbl.place(x=10,y=400)

confirmpasswordEntry = Entry(frame,width=30,borderwidth=2)
confirmpasswordEntry.place(x=240,y=400)

submitbtn = Button(frame,text='Submit',width=15,borderwidth=5,height=2,bg='#7f7fff',fg='white',cursor='hand2',border=2,font=('#57a1f8',16,'bold'),command=submit)
submitbtn.place(x=150,y=500)

bckbtn = Button(frame,text='<<',width=10,border=2,height=2,cursor='hand2',bg='black',fg='white',command=bck)
bckbtn.place(x=0,y=550)

#chekc buttons
check1 = Checkbutton(frame,text='',bg='black',command=show1)
check1.place(x=420,y=350)

check2 = Checkbutton(frame,text='',bg='black',command=show2)
check2.place(x=420,y=400)






windows.mainloop()