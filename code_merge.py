

__author__ = '15052401'
from tkinter import *
from tkinter import ttk
from operator import itemgetter
import time

taskList = []
fN = ""

class data_tasks:


    def import_tasks(self):#tries=1):

        textFile = open (fN, "r")
        tasks = []
        for line in textFile:
            task = line.split(",")
            for i in range (len(task)):
                x = task[i].strip()
                try:
                    task [i]= int (x)
                except:
                    task [i] = x
            taskList.append(task)
        textFile.close()



    def export_tasks(self):
        print(taskList)
        self.f = open(fN, 'w')
        for task in taskList:
            for i in task:
                self.f.write(i)
                print(i)

                self.f.write(",")
            self.f.write("\n")
        self.f.close


def run_create_task():
    root = Tk()
    #size of the window
    root.geometry("300x200")

    create_task(root)

    root.mainloop()



def update_list_box(listbox,list):
    listbox.delete(*listbox.get_children())
    x=0
    for i in list:
        listbox.insert("" , 0,    text=str(x), values=(i[0],i[1],i[2],i[3]))
        x+=1
    # print (taskList)

def order_done(list):
    complete=[]
    not_complete=[]
    for i in list:
        if str(i[2])== "Yes":
            complete.append(i)
        elif str(i[2])== "No":
            not_complete.append(i)
    complete+=not_complete
    global taskList
    taskList = complete
    # print(complete)
    update_list_box(task_list_box,complete)

def order_reverse(list):
    reverse=[]
    for i in list:
        reverse.insert(0,i);
    global taskList
    taskList = reverse
    update_list_box(task_list_box,reverse)

def order_importance(list):
    very_high=[]
    high=[]
    normal=[]
    low=[]
    for i in list:
        if str(i[1])== "Very High":
            very_high.append(i)
        elif str(i[1])== "High":
            high.append(i)
        elif str(i[1])== "Normal":
            normal.append(i)
        elif str(i[1])== "Low":
            low.append(i)
    low+=normal+high+very_high
    # print(low)
    global taskList
    taskList = low
    update_list_box(task_list_box,low)

def order_alphabetically(list):
    alphabetical=sorted(list, key=itemgetter(0))
    global taskList
    taskList = alphabetical
    update_list_box(task_list_box,alphabetical)

def mark_as_complete():
    iid=task_list_box.focus()
    curitem = task_list_box.item(iid)
    i = int(curitem.get("text"))

    taskList[i][2]= "Yes"
    update_list_box(task_list_box,taskList)

def delete():
    iid=task_list_box.focus()
    curitem = task_list_box.item(iid)
    i = int(curitem.get("text"))
    taskList.pop(i)
    update_list_box(task_list_box,taskList)



class create_task(Frame):

    def __init__(self, slave=None):
        Frame.__init__(self, slave)
        self.slave = slave
        self.init_window()
        self.init_window2()
        self.init_window3()



    #Creation of init_window
    def init_window(self):

        self.slave.title("Create New Task")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.slave)
        self.slave.config(menu=menu)

        # file = Menu(menu, tearoff = 0)
        # file.add_command(label="Save")
        # file.add_command(label="Exit", command=self.client_exit)
        # menu.add_cascade(label="File", menu=file)
        #
        # edit = Menu(menu, tearoff = 0)
        # edit.add_command(label="Undo")
        # menu.add_cascade(label="Edit", menu=edit)
        #
        # Help = Menu(menu, tearoff = 0)
        # Help.add_command(label="1")
        # Help.add_command(label="2")
        # menu.add_cascade(label="Help", menu=Help)



    def init_window2(self):

        qButton = Button(self, text="     OK     ",command=self.ok)
        qButton.place(x=230, y=190)

        quitButton = Button(self, text=" Cancel ", command=self.client_exit)
        quitButton.place(x=10, y=190)

    def init_window3(self):

        # print(self)
        self.l=Label(self,text="Enter new task: ")
        self.l.pack()
        self.e=Entry(self)
        self.e.pack()


        self.month = StringVar(self)
        self.month.set("Month")
        OptionMenu(self, self.month, "01","02","03","04","05","06","07","08","09","10","11","12").place(x=107, y=110)

        self.day = StringVar(self)
        self.day.set("Day")
        OptionMenu(self, self.day, "01","02","03","04","05","06","07","08","09",10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31).place(x=50, y=110)

        self.year = StringVar(self)
        self.year.set("Year")
        OptionMenu(self, self.year, 2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030).place(x=190, y=110)

        self.hour = StringVar(self)
        self.hour.set("Hour")
        OptionMenu(self, self.hour, "00","01","02","03","04","05","06","07","08","09",10,11,12).place(x=30, y=140)

        self.minute = StringVar(self)
        self.minute.set("Min")
        OptionMenu(self, self.minute, "00",10,20,30,40,50).place(x=100, y=140)

        self.sec = StringVar(self)
        self.sec.set("ute")
        OptionMenu(self, self.sec,  "00","01","02","03","04","05","06","07","08","09").place(x=150, y=140)

        self.AP = StringVar(self)
        self.AP.set("AM")
        OptionMenu(self, self.AP, "AM","PM").place(x=200, y=140)

        self.p = StringVar(self)
        self.p.set("Select Priority")
        OptionMenu(self, self.p, "Very High", "High", "Normal", "Low").pack()


#
# test stuff
    def ok(self):
        global task
        task =[]
        task.append(self.e.get())
        task.append(self.p.get().strip())
        task.append("No")
        minutes = (int (self.minute.get())+int (self.sec.get()))
        if self.AP.get() == "PM":
            hours = int (self.hour.get())+12
        else:
            hours = self.hour.get()
        due = str(self.day.get())+"/"+str(self.month.get())+"/"+str(self.year.get())+" > "+str(hours)+":"+str(minutes)
        task.append(due)
        due2 = str(self.year.get())+str(self.month.get())+str(self.day.get())+str(hours)+str(minutes)
        # task.append(due2)
        taskList.append(task)

        # print (task)

        self.slave.destroy()
        update_list_box(task_list_box,taskList)



    def init_window4(self):
        top = self
        mb=  Menubutton ( top, text="     Priority     ", relief=RAISED )
        mb.grid()
        mb.menu  =  Menu ( mb, tearoff = 0 )
        mb["menu"]  =  mb.menu


        mb.menu.add_checkbutton ( label="Very High")
        mb.menu.add_checkbutton ( label="High")
        mb.menu.add_checkbutton ( label="Normal")
        mb.menu.add_checkbutton ( label="Low")

        mb.pack()


    def client_exit(self):
        self.slave.destroy()




def update_time():
    now = time.strftime("%H:%M:%S")
    date = time.strftime("%x")
    x = "Time: "+ now+"  Date: "+ date
    clock.config(text=x)
    master.after(1000, update_time)

def quit_program():
    data.export_tasks()
    master.destroy()





fN = sys.argv[1]
data = data_tasks()
data.import_tasks()

master = Tk()
master.title("Task manager")

task_list_box = ttk.Treeview(master, height="26", columns=("Task", "importnace", "complete", "Due date"), selectmode="extended")
task_list_box.column("Task", stretch=NO, minwidth=0, width=500)
task_list_box.column('importnace', stretch=NO, minwidth=0, width=100)
task_list_box.column('complete', stretch=NO, minwidth=0, width=100)
task_list_box.column('Due date', stretch=NO, minwidth=0, width=130)
task_list_box.column('#0', stretch=NO, minwidth=0, width=0)

task_list_box.heading("Task", text='Task', anchor=CENTER)
task_list_box.heading('importnace', text='Importnace', anchor=CENTER)
task_list_box.heading('complete', text='Complete?', anchor=CENTER)
task_list_box.heading('Due date', text='Due date', anchor=CENTER)

clock=Label(master,text="")
clock.grid(row = 1, column = 3,columnspan=2)
Label(master, text="", command=update_time()).grid(row=0, column=2)



Button(master, text="Mark as complete", command=mark_as_complete, width=20).grid(row=2, column=3)
Button(master, text="Add task",command=run_create_task , width=20).grid(row=1, column=2)
Button(master, text="Order by done",command=lambda: order_done(taskList) , width=20).grid(row=2, column=1)
Button(master, text="Order by importance",command=lambda: order_importance(taskList) , width=20).grid(row=1, column=1)
Button(master, text="Order alaphabetically",command=lambda: order_alphabetically(taskList) , width=20).grid(row=2, column=0)
Button(master, text="Reverse the order",command=lambda: order_reverse(taskList) , width=20).grid(row=1, column=0)
Button(master, text="Delete task",command=lambda: delete() , width=20).grid(row=2, column=2)
Button(master, text="Quit",command=lambda: quit_program() , width=20).grid(row=2, column=4)
# Button(master, text="Edit task",command=lambda: quit_program() ).grid(row=2, column=5)

update_list_box(task_list_box,taskList)

task_list_box.grid(row=0, column=0, columnspan= 5)


master.mainloop()
data.export_tasks()

