from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
import re
import itertools

db = pymysql.connect("localhost","root","","userdb")
cursor = db.cursor()
root = Tk()
root.title("Medical database management")
root.geometry("900x600")
nameofcompny=StringVar()
domfd=StringVar()
doexp=StringVar()
price_medition=StringVar()
def additom():
    global cursor
    global itom_name
    global price_medition
    global nameofcompny
    global domfd
    global doexp
    itom_name = e1.get()
    quantity = int(e2.get())
    quantity1 = e2.get()
    query="SELECT * FROM admin WHERE medition_name='{}'".format(itom_name)
    cursor.execute(query)
    mdata=cursor.fetchall()
    itom_lista=[item for t in mdata for item in t]
    price_medition=quantity*int(itom_lista[6])
    
    query = "INSERT INTO treeview(medition_name,compny_name,mfd,exp_d,quantity,price) VALUES('{}','{}','{}','{}','{}','{}')".format(itom_name,itom_lista[2],itom_lista[3],itom_lista[4],quantity1,price_medition)
    try:
        cursor.execute(query)
        db.commit()
        e1.delete(0,END)
        e2.delete(0,END)
        tree_view()
        messagebox.showinfo("Success","User added successfully")
    except:
        db.rollback()
        messagebox.showerror("Error","Error in query1")
        
def delete_itom():
        global cursor
        delete_itom = e4.get()  
        query = "DELETE FROM treeview WHERE medition_name = '{}'".format(delete_itom)
        try:
                cursor.execute(query)
                if cursor.rowcount > 0 :
                        db.commit()
                        e4.delete(0,END)
                        tree_view()
                        messagebox.showinfo("Success","itom delete successfully")   
        except Exception as e:
                db.rollback()
                print(e)
                messagebox.showerror("Error","itom not delete")
def add_new_itom():
    global cursor
    itom_name = itomadd.get()
    itom_compny = itomadd1.get()
    exp_d = itomadd3.get()
    quantity = itomadd4.get()
    price = itomadd5.get()
    mfd = itomadd2.get()
    query = "INSERT INTO admin(medition_name,compny_name,mfd,exp_d,quantity,price)VALUES('{}','{}','{}','{}','{}','{}')".format(itom_name,itom_compny,mfd,exp_d,quantity,price)
    try:
        cursor.execute(query)
        db.commit()
        itomadd.delete(0,END)
        itomadd1.delete(0,END)
        itomadd2.delete(0,END)
        itomadd3.delete(0,END)
        itomadd4.delete(0,END)
        itomadd5.delete(0,END)
        messagebox.showinfo("Success","User added itom  successfully")
    except Exception as e:
        db.rollback()
        print(e)
        messagebox.showerror("Error","itom not add")
def remove_itom():
    global cursor
    itom_name = removitom.get()
    query = "DELETE FROM admin WHERE medition_name = '{}'".format(itom_name)
    try:
        cursor.execute(query)
        db.commit()
        removitom.delete(0,END)
        messagebox.showinfo("Success","itom remove successfully")
    except Exception as e:
                db.rollback()
                print(e)
                messagebox.showerror("Error","itom not remove")

def bill_print():
    cursor.execute("select * FROM treeview")
    val=cursor.fetchall()
    print("itom_name    conmpy_name      mf_date    exp_date    quantity    price")
    for i in val:
        print()
        print("{}   {}       {}    {}    {}    {}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
    cursor.execute("select price FROM treeview")
    val1=cursor.fetchall()
    bill=[item for t in val1 for item in t]
    finalbill=0
    for i in bill:
        finalbill+=i
    print("\nfinal bill=> ",finalbill)

def login():
    global cursor
    user_id=e11.get()
    user_password=e22.get()
    query = "SELECT * FROM admin_login" 
    cursor.execute(query)
    login_data=cursor.fetchall()
    data=[item for t in login_data for item in t]
    print(data)
    if data[0]==user_id and data[1]==user_password:
        e11.delete(0,END)
        e22.delete(0,END)
        mainwindow()
    else:
        e11.delete(0,END)
        e22.delete(0,END)
        login_page()
def forget_password():
    global cursor
    forget_id=e11.get()
    query = "SELECT * FROM admin_login"
    cursor.execute(query)
    login_data=cursor.fetchall()
    data=[item for t in login_data for item in t]
    if forget_id==data[2]:
        print("login id=> ",data[0])
        print("login password=> ",data[1])
        mainwindow()
    else:
        e1.delete(0,END)
        forget()    
def forget():
    global cursor
    global e11
    remove_all_widgets()
    db = pymysql.connect("localhost","root","","userdb")
    cursor = db.cursor()
    root.title("Medical database management")
    root.geometry("900x600")
    l = Label(root, text="Forget password Window")
    l.place(x=260, y=10)
    l1 = Label(root, text="enter nick name")
    l1.place(x=50, y=30)
    e11=Entry(root)
    e11.place(x=150, y=30)
    b1 = Button(root, text="reset", command=forget_password)
    b1.place(x=100, y=80)
    b2 = Button(root, text="backto login page", command=login_page)
    b2.place(x=200, y=80)

def addnewitom():
    global itomadd
    global itomadd1
    global itomadd2
    global itomadd3
    global itomadd4
    global itomadd5
    remove_all_widgets()
    db = pymysql.connect("localhost","root","","userdb")
    cursor = db.cursor()
    root.title("Medical database management")
    root.geometry("900x600")
    button1=Button(root,text="close update window",command=mainwindow)
    button1.place(x=80,y=170)
    l = Label(root, text="Adddnew itom WIndow")
    l.place(x=360,y=10)
    l1 = Label(root, text="add_new medition_name")
    l1.grid(row=0, column=1)
    itomadd = Entry(root)
    itomadd = AutocompleteEntry(lista, root)
    itomadd.grid(row=0,column=2)
    l2 = Label(root, text="medition_compny")
    l2.grid(row=1, column=1)
    itomadd1 = Entry(root)
    itomadd1.grid(row=1,column=2)
    l3 = Label(root, text="mfd")
    l3.grid(row=2, column=1)
    itomadd2 = Entry(root)
    itomadd2.grid(row=2,column=2)
    l4 = Label(root, text="exp_d")
    l4.grid(row=3, column=1)
    itomadd3 = Entry(root)
    itomadd3.grid(row=3,column=2)
    l5 = Label(root, text="quantity")
    l5.grid(row=4, column=1)
    itomadd4 = Entry(root)
    itomadd4.grid(row=4,column=2)
    l6 = Label(root, text="price")
    l6.grid(row=5, column=1)
    itomadd5 = Entry(root)
    itomadd5.grid(row=5,column=2)
    button2=Button(root,text="add_medition",command=add_new_itom)
    button2.place(x=80,y=130)
def re_itom():
    global removitom
    remove_all_widgets()
    db = pymysql.connect("localhost","root","","userdb")
    cursor = db.cursor()
    root.title("Medical database management")
    root.geometry("900x600")
    button1=Button(root,text="close update window",command=mainwindow)
    button1.place(x=80,y=170)
    l = Label(root, text="Remove item from admin database")
    l.place(x=360,y=10)
    l1 = Label(root, text="itom name")
    l1.grid(row=0, column=1)
    removitom = Entry(root)
    removitom = AutocompleteEntry(lista, root)
    removitom.grid(row=0,column=2)
    button=Button(root,text="remove itom",command=remove_itom)
    button.place(x=80,y=80)
def  tree_view():
    record= tree.get_children()
    for element in record:
        tree.delete(element)
    cursor.execute("select * FROM treeview")
    val=cursor.fetchall()
    for i in val:
        tree.insert('','end',values=(i[0],i[1],i[2],i[3],i[4],i[5]))
def update_itom():
    global cursor
    itom_name = upitom1.get()
    itom_compny = upitom2.get()
    update_mfd = upitom3.get()
    update_exp = upitom4.get()
    update_quantity = upitom5.get()
    update_price = upitom6.get()
    query ="UPDATE admin SET compny_name ='{}',mfd='{}',exp_d='{}',quantity='{}',price='{}' WHERE medition_name='{}'".format(itom_compny,update_mfd,update_exp,update_quantity,update_price,itom_name)
    try:
        cursor.execute(query)
        z=cursor.fetchall()
        print(z)
        db.commit()
        messagebox.showinfo("Success","itom update successfully")
    except Exception as e:
                db.rollback()
                print(e)
                messagebox.showerror("Error","itom not update")
def updateitom():
    global upitom1
    global upitom2
    global upitom3
    global upitom4
    global upitom5
    global upitom6
    remove_all_widgets()
    db = pymysql.connect("localhost","root","","userdb")
    cursor = db.cursor()
    root.title("Medical database management")
    root.geometry("900x600")
    button1=Button(root,text="close update window",command=mainwindow)
    button1.place(x=80,y=170)
    l = Label(root, text="Update item Window")
    l.place(x=360,y=10)
    l1 = Label(root, text="medition_name")
    l1.grid(row=0, column=1)
    upitom1 = Entry(root)
    upitom1 = AutocompleteEntry(lista, root)
    upitom1.grid(row=0,column=2)
    l2 = Label(root, text="medition_compny")
    l2.grid(row=1, column=1)
    upitom2 = Entry(root)
    upitom2.grid(row=1,column=2)
    l3 = Label(root, text="mfd")
    l3.grid(row=2, column=1)
    upitom3 = Entry(root)
    upitom3.grid(row=2,column=2)
    l4 = Label(root, text="exp_d")
    l4.grid(row=3, column=1)
    upitom4 = Entry(root)
    upitom4.grid(row=3,column=2)
    l5 = Label(root, text="quantity")
    l5.grid(row=4, column=1)
    upitom5 = Entry(root)
    upitom5.grid(row=4,column=2)
    l6 = Label(root, text="price")
    l6.grid(row=5, column=1)
    upitom6 = Entry(root)
    upitom6.grid(row=5,column=2)
    button2=Button(root,text="update_medition_info",command=update_itom)
    button2.place(x=80,y=130)
    
class AutocompleteEntry(Entry):
    def __init__(self, lista, *args, **kwargs):
        
        Entry.__init__(self, *args, **kwargs)
        self.lista = lista        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        
        self.lb_up = False

    def changed(self, name, index, mode):  

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True
                
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]
def remove_all_widgets():
    global root
    for widget in root.winfo_children():
        widget.destroy()

def login_page():
    global e11
    global e22
    db = pymysql.connect("localhost","root","","userdb")
    cursor = db.cursor()
    root.title("Medical database management")
    root.geometry("900x600")
    l = Label(root, text="Login Window")
    l.place(x=350, y=10)
    l1 = Label(root, text="login id")
    l1.place(x=50, y=30)
    e11=Entry(root)
    e11.place(x=150, y=30)
    l2 = Label(root, text="password")
    l2.place(x=50, y=50)
    e22 = Entry(root)
    e22.place(x=150,y=50)
    b1 = Button(root, text="login", command=login)
    b1.place(x=100, y=80)
    b2 = Button(root, text="forget login_password", command=forget)
    b2.place(x=200, y=80)
def mainwindow():
    global e1
    global e2
    global e4
    global tree
    global lista
    remove_all_widgets()
    db = pymysql.connect("localhost","root","","userdb")
    cursor = db.cursor()
    m=Menu(root)
    root.config(menu=m)
    filemenu=Menu(m,tearoff=False)
    m.add_cascade(label='Admin Window',menu=filemenu)
    filemenu.add_cascade(label='add new medicen',command=addnewitom )
    filemenu.add_cascade(label='remove itom',command=re_itom)
    filemenu.add_cascade(label='update itom',command=updateitom)
    filemenu.add_separator()
    filemenu.add_cascade(label='Exit',command=root.destroy)
    frame = Frame(root)
    frame1=Frame(root)
    frame2=Frame(root)
    cursor.execute("select medition_name FROM admin")
    it=cursor.fetchall()
    lista=[item for t in it for item in t]

    l1 = Label(root, text="itom")
    l1.place(x=50, y=30)

    e1=Entry(frame)
    e1 = AutocompleteEntry(lista, root)
    e1.place(x=90, y=30)

    l2 = Label(frame, text="quantity")
    l2.grid(row=0, column=1)

    e2 = Entry(frame)
    e2.grid(row=0,column=2)

    b1 = Button(root, text="add", command=additom)
    b1.place(x=250, y=50)

    b2 = Button(frame2, text="print", command=bill_print)
    b2.grid(row=0, column=4)

    b4 = Button(root, text="delete", command=delete_itom)
    b4.place(x=800, y=150)
    e4=Entry(frame)
    e4 = AutocompleteEntry(lista, root)
    e4.place(x=670, y=150)

    tree=ttk.Treeview(frame1,columns=(1,2,3,4,5,6),height=5,show='headings')
    tree.pack(side='left')
    tree.heading(1,text='itom_name')
    tree.heading(2,text='compny_name')
    tree.heading(3,text='date_of_manufacturing')
    tree.heading(4,text='date_of_exp')
    tree.heading(5,text='quantity')
    tree.heading(6,text='price')
    tree.column(1,width=100)
    tree.column(2,width=100)
    tree.column(3,width=100)
    tree.column(4,width=100)
    tree.column(5,width=100)
    tree.column(6,width=100)
    scroll=ttk.Scrollbar(frame1,orient='vertical',command=tree.yview)
    scroll.pack(side='right',fill='y')
    tree.configure(yscrollcommand=scroll.set)
    cursor.execute("select * FROM treeview")
    val=cursor.fetchall()
    for i in val:
        tree.insert('','end',values=(i[0],i[1],i[2],i[3],i[4],i[5]))
    frame.place(x=40, y=50)
    frame1.place(x=50, y=100)
    frame2.place(x=330, y=230)
login_page()
root.mainloop()
