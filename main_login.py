__author__ = '15052401'
from tkinter import*
import os
import tkinter.messagebox as tm




class LoginWindow(Frame):
    def __init__(self, master):

        self.message = StringVar()
        self.message =""


        Label(master, text = "Username").grid(row = 1, column = 1)
        Label(master, text = "Password").grid(row = 2, column = 1)


        self.loginUser = StringVar()
        self.password = StringVar()
        Entry(master, textvariable = self.loginUser).grid(columnspan=2,row = 1, column = 2)
        Entry(master, textvariable = self.password,  show="*").grid(columnspan=2,row = 2, column = 2)

        Button(master, text="Sign In", command = self.logged).grid(row=3, column=2)
        Button(master, text="Register", command = self.register).grid(row=3, column=3)
        Label(master, text=self.message).grid(row=0, column=2)


        var1 = IntVar()
        # Checkbutton(master, text="Remember password", variable=var1).grid(row= 4, columnspan=5)

        master.minsize(width= 250, height=100)
      #  mainloop()


    def logged(self):
        username = self.loginUser.get()
        password = self.password.get()
        match = False
        for item in userDetail:
            if (username == item[0]) and (password == item[1]):
                fN = username + ".txt"
                os.system('py code_merge.py ' + fN)
                match = True



        if (match == False):
            tm.showinfo("Fail", "Error, wrong password or username")

    def register(self):
        username = self.loginUser.get()
        password = self.password.get()
        duplicate = False
        for i in userDetail:
            if username == i[0]:
                tm.showinfo("Error", "Username already exists")
                duplicate = True

        if duplicate == False:
            new = []
            new.append(username)
            new.append(password)
            userDetail.append(new)
            doc = open('details.txt','w')
            doc.truncate()
            for item in userDetail:
                stripe = ""
                stripe += item[0]
                stripe += ','
                stripe += item[1]
                stripe += '\n'
                doc.write(stripe)
            doc.close()

            doc = open(username + '.txt','w')
            doc.truncate()
            doc.write("")
            doc.close()
            self.message="Account created!"
            tm.showinfo("Sucess", "Account created")




root = Tk()
root.wm_title("Login(Task Master)")
logframe = LoginWindow(root)


usernames = []
password = []
arrays = [usernames, password]
doc = open('details.txt','r')
userDetail = []
for item in doc:
    stripe = item.rstrip('\n')
    stripe = stripe.split(',')
    userDetail.append(stripe)


doc.close()
root.mainloop()

