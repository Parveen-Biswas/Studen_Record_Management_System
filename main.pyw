from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os


root = Tk()
root.title("Welcome To SRMS")
root.geometry("1400x700+300+150")
root.resizable(False,False)
# root.overrideredirect(1)


header = Image.open('./Images/mainframe2.png')
header_Resize = header.resize((1400,700))
header_Resize_Image = ImageTk.PhotoImage(header_Resize)
headerLabel = Label(root, image = header_Resize_Image)
headerLabel.pack()

# Labels and Entry
studentId = Label(root, text="Student ID", font=("Times New Roman", 12), bg="#c0c0c0")
studentId.place(x=44,y=60)
studentIdEntry = Entry(root,width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
studentIdEntry.place(x=48, y=85)

studentName = Label(root, text="Student Name", font=("Times New Roman", 12), bg="#c0c0c0")
studentName.place(x=44,y=120)
studentNameEntry = Entry(root,width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
studentNameEntry.place(x=48, y=145)

studentDOB = Label(root, text="DOB (DD/MM/YYYY)", font=("Times New Roman", 12), bg="#c0c0c0")
studentDOB.place(x=280,y=60)
studentDOBEntry = Entry(root,width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
studentDOBEntry.place(x=284, y=85)

studentGender = Label(root, text="Gender", font=("Times New Roman", 12), bg="#c0c0c0")
studentGender.place(x=280,y=120)
genderOptions = ["Male", "Female", "Other"]
valueInside = StringVar()
valueInside.set("Select an Option")
studentGenderEntry = OptionMenu(root, valueInside, *genderOptions)
studentGenderEntry.configure(width=18, border=0, font=("Times New Roman", 12), highlightthickness=2)
studentGenderEntry.place(x=284, y=145)

studentDegree = Label(root, text="Degree", font=("Times New Roman", 12), bg="#c0c0c0")
studentDegree.place(x=524,y=60)
studentDegreeEntry = Entry(root,width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
studentDegreeEntry.place(x=528, y=85)

studentStream = Label(root, text="Stream", font=("Times New Roman", 12), bg="#c0c0c0")
studentStream.place(x=524,y=120)
studentStreamEntry = Entry(root,width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
studentStreamEntry.place(x=528, y=145)

studentPhone = Label(root, text="Phone", font=("Times New Roman", 12), bg="#c0c0c0")
studentPhone.place(x=768,y=60)
studentPhoneEntry = Entry(root,width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
studentPhoneEntry.place(x=772, y=85)

studentEmail = Label(root, text="Email", font=("Times New Roman", 12), bg="#c0c0c0")
studentEmail.place(x=768,y=120)
studentEmailEntry = Entry(root,width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
studentEmailEntry.place(x=772, y=145)

studentAddress = Label(root, text="Address", font=("Times New Roman", 12), bg="#c0c0c0")
studentAddress.place(x=1012,y=60)
studentAddressEntry = Entry(root,width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
studentAddressEntry.place(x=1016, y=85)

# Details Print
def printDetails():
    id = studentIdEntry.get()
    name = studentNameEntry.get()
    dob = studentDOBEntry.get()
    gender = valueInside.get()
    degree = studentDegreeEntry.get()
    stream = studentStreamEntry.get()
    phone = studentPhoneEntry.get()
    email = studentEmailEntry.get()
    address = studentAddressEntry.get()
    # print(f"Student ID: {id}")
    # print(f"Student Name: {name}")
    # print(f"Date of Birth: {dob}")
    # print(f"Gender: {gender}")
    # print(f"Degree: {degree}")
    # print(f"Stream: {stream}")
    # print(f"Phone: {phone}")
    # print(f"Email: {email}")
    # print(f"Address: {address}")

def addInformation():
    id = studentIdEntry.get()
    name = studentNameEntry.get()
    dob = studentDOBEntry.get()
    gender = valueInside.get()
    degree = studentDegreeEntry.get()
    stream = studentStreamEntry.get()
    phone = studentPhoneEntry.get()
    email = studentEmailEntry.get()
    address = studentAddressEntry.get()

    while True:
        if id != "":
            proceedOrNot = messagebox.askyesno("Student Adding", "Are You Sure add Student \nId = {}\nName = {}\nGender = {}\nDate Of Birth = {}\nDegree = {}\nStream = {}\nPhone = {}\nEmail = {}\nAddress = {}".format(id, name, gender, dob ,degree, stream, phone, email, add))
            if proceedOrNot == 1:
            # Inserting data into database
                cursor.execute("insert into student values ('"+id+"', '"+name+"', '"+gender+"', '"+dob+"', '"+degree+"', '"+stream+"', '"+phone+"' , '"+email+"', '"+address+"')")
        
            # Displaying a message box if data is inserted successfully
                messagebox.showinfo("Student Adding", "Successfully added Student \nId = {}\nName = {}\nGender = {}\nDate Of Birth = {}\nDegree = {}\nStream = {}\nPhone = {}\nEmail = {}\nAddress = {}".format(id, name, gender, dob ,degree, stream, phone, email, address))
        
            # Commiting changes to database
                mydb.commit()
            else:
        # Displaying a message box if data is not inserted successfully
                messagebox.showinfo("Unsuccessfull", "Cancelled")
            break
        elif id == "":
            messagebox.showinfo("Error", "Please Fill all the fields")
            break


def refreshInformation():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM student")
    for i in cursor:
        tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3], i[4], i[5],i[6], i[7], i[8]))

def deleteInformation():
    # Getting id of student to delete
    id = studentIdEntry.get()
    print(id)
    proceedOrNot = messagebox.askyesno("Student Information", "Delete Student ?\nId = {} ".format(id))
    if proceedOrNot == 1:
        # Deleting student information from database
        cursor.execute(" delete from student where id = '"+id+"' ")
        # Commiting changes to database
        mydb.commit()
        # Displaying a message box if data is deleted successfully
        messagebox.showinfo("Deleting Student", "Successfully deleted Student \n Id = {}".format(id))
    else:
         # Displaying a message box if data is not deleted successfully
         messagebox.showinfo("Unsuccessfully", "Canceled")

def resetInformation():
    studentIdEntry.delete(0,140)
    studentNameEntry.delete(0,140)
    studentDOBEntry.delete(0,140)
    studentDegreeEntry.delete(0,140)
    studentStreamEntry.delete(0,140)
    studentPhoneEntry.delete(0,140)
    studentEmailEntry.delete(0,140)
    studentAddressEntry.delete(0,140)
    # valueInside.delete(0,140)
    searchEntry.delete(0,140)

def searchInformation():
    id = searchEntry.get()
    name = searchEntry.get()
    email = searchEntry.get()

   # Deleting previous data from treeview
    if tree.get_children() != ():
        tree.delete(*tree.get_children())
   # Fetching data from database
    cursor.execute("select * from student where ID = '"+id+"' or EMAIL = '"+email+"' or NAME = '"+name+"' ")

    for i in cursor:
       tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3], i[4],i[5],i[6], i[7], i[8]))

def editInformation():
    topWindow = Toplevel()
    topWindow.title("Edit Student Information")
    topWindow.geometry("450x200+600+200")
    # topWindow.overrideredirect(1)
    
    # Label and entry
    topStudentIdLabel = Label(topWindow, text="Student ID", font=("Times New Roman", 12))
    topStudentIdLabel.place(x=20,y=20)
    topStudentIdEntry = Entry(topWindow, width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
    topStudentIdEntry.place(x=100, y=20)

    topStudentPhoneLabel = Label(topWindow, text="Phone", font=("Times New Roman", 12))
    topStudentPhoneLabel.place(x=20,y=60)
    topStudentPhoneEntry = Entry(topWindow, width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
    topStudentPhoneEntry.place(x=100, y=60)
    
    topStudentEmailLabel = Label(topWindow, text="Email", font=("Times New Roman", 12))
    topStudentEmailLabel.place(x=20,y=100)
    topStudentEmailEntry = Entry(topWindow, width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
    topStudentEmailEntry.place(x=100, y=100)

    topStudentAddressLabel = Label(topWindow, text="Address", font=("Times New Roman", 12))
    topStudentAddressLabel.place(x=20,y=140)
    topStudentAddressEntry = Entry(topWindow, width=20, font=('Times New Roman',14), bd=0, highlightthickness=2)
    topStudentAddressEntry.place(x=100, y=140)

    # functions
    def editInformationInput():
        id = topStudentIdEntry.get()
        phone = topStudentPhoneEntry.get()
        email = topStudentEmailEntry.get()
        address = topStudentAddressEntry.get()
        # print(id,phone,email, address)
        while True:
            if id != "":
                cursor.execute("UPDATE STUDENT SET PHONE = '"+phone+"', EMAIL = '"+email+"', ADDRESS = '"+address+"'  WHERE ID = '"+id+"' ")
                mydb.commit()
                topWindow.destroy()
                break

            else:
                messagebox.showerror("Error", "Please fill all the fields")
                break

    def cancelExit():
        topWindow.destroy()
        

    # Buttons
    topSaveButton = Button(topWindow, text="Save",width=15, border=0, font=("Times New Roman", 12), bg="red", fg="white", activebackground="white", activeforeground="red", command=editInformationInput)
    topSaveButton.place(x=300, y=20)
    topCancelButton = Button(topWindow, text="Cancel",width=15, border=0, font=("Times New Roman", 12), bg="red", fg="white", activebackground="white", activeforeground="red", command=cancelExit)
    topCancelButton.place(x=300, y=70)



# Make buttons
add = ImageTk.PhotoImage(Image.open("./Images/add.png").resize((150,30)))
addBtn = Button(root, image=add, border=0, activebackground="#c0c0c0", command=addInformation)
addBtn.place(x=44, y=215)

refresh = ImageTk.PhotoImage(Image.open("./Images/refresh.png").resize((150,30)))
refreshBtn = Button(root, image=refresh, border=0, activebackground="#c0c0c0", command=refreshInformation)
refreshBtn.place(x=220, y=215)

reset = ImageTk.PhotoImage(Image.open("./Images/reset.png").resize((150,30)))
resetBtn = Button(root, image=reset, border=0, activebackground="#c0c0c0", command=resetInformation)
resetBtn.place(x=396, y=215)

delete = ImageTk.PhotoImage(Image.open("./Images/delete.png").resize((150,30)))
deleteBtn = Button(root, image=delete, border=0, activebackground="#c0c0c0", command=deleteInformation)
deleteBtn.place(x=572, y=215)

# Search Entry and Button
searchEntry = Entry(root, width=20, border=0 ,font=('poppins', 15), bg="white")
searchEntry.place(x=975,y=219)
search = ImageTk.PhotoImage(Image.open("./Images/search.png").resize((150,30)))
searchBtn = Button(root, image=search, border=0, activebackground="#c0c0c0", command=searchInformation)
searchBtn.place(x=1204, y=215)

edit = ImageTk.PhotoImage(Image.open("./Images/edit.png").resize((150,30)))
editBtn = Button(root, image=edit, border=0, activebackground="#c0c0c0", command=editInformation)
editBtn.place(x=748, y=215)

# Database
mydb = sqlite3.connect(os.path.join(os.path.dirname(__file__), "StudentRecord.db"))
cursor = mydb.cursor()

# Create a table in database if doesn't exist
cursor.execute('''
create table if not exists student (
   ID varchar(30) NOT NULL UNIQUE PRIMARY KEY,
   NAME varchar(50) NOT NULL,
   DOB varchar(10) NOT NULL,
   GENDER varchar(10) NOT NULL,
   DEGREE varchar(10) NOT NULL,
   STREAM varchar(50) NOT NULL,
   PHONE varchar(20) NOT NULL,
   EMAIL varchar(50) NOT NULL UNIQUE,
   ADDRESS varchar(150) NOT NULL
   )
   ''')     

# Create Treeview for display data
tree = ttk.Treeview(root, selectmode='browse', columns=('ID', ' Name', 'DateOfBirth', 'Gender', 'Degree', 'Stream', 'Phone Number', 'Email', 'Address'))
tree.heading('#0', text='ID')
tree.heading('#1', text='Name')
tree.heading('#2', text='Gender')
tree.heading('#3', text='Date of Birth')
tree.heading('#4', text='Degree')
tree.heading('#5', text='Stream')
tree.heading('#6', text='Phone Number')
tree.heading('#7', text='Email')
tree.heading('#8', text='Address')
tree.column('#0', width=130, anchor='center')
tree.column('#1', width=150, anchor='center')
tree.column('#2', width=80, anchor='center')
tree.column('#3', width=150, anchor='center')
tree.column('#4', width=100, anchor='center')
tree.column('#5', width=100, anchor='center')
tree.column('#6', width=140, anchor='center')
tree.column('#7', width=230, anchor='center')
tree.column('#8', width=190, anchor='center')
# tree.pack()
tree.place(x=40,y=263, width=1320, height=418)

# Owner Label
ownerLabel = Label(root, text="Developed by Parveen Biswas at 30 nov 2024", font=("Times New Roman", 8), bg="#c0c0c0")
ownerLabel.place(x=590, y=682)

root.mainloop()