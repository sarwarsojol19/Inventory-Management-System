from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Filling Station Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #====Content Variables====
        
        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        #====Title===
        
        title=Label(self.root,text="Manage Product Category",font=("time new romans",20,"bold"),bg="#184a45",fg="white").pack(side=TOP,fill=X)

        #====Search====

        lbl_name=Label(self.root,text="Enter Category Name",font=("time new romans",20),bg="white").place(x=20,y=50)          
        txt_name=Entry(self.root,textvariable=self.var_name,font=("time new romans",20),bg="lightyellow").place(x=20,y=100,width=250)
        btn_add=Button(self.root,text="ADD",command=self.add,font=("time new romans",15),bg="#2196f3",fg="white",cursor="hand2").place(x=20,y=150,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("time new romans",15),bg="#f44336",fg="white",cursor="hand2").place(x=150,y=150,width=110,height=35)

        #====Category Details====
        
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=550,y=45,width=500,height=200)
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        
        self.categoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X) 
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        
        self.categoryTable.heading("cid",text="Category ID")
        self.categoryTable.heading("name",text="Name")
        
        self.categoryTable["show"]="headings"
        
        self.categoryTable.column("cid",width=100)
        self.categoryTable.column("name",width=100)      
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
        #====Images====
        self.im1=Image.open("images/cat.jpg")
        self.im1=self.im1.resize((500,200),Image.ANTIALIAS)
        self.im1=ImageTk.PhotoImage(self.im1)
        self.lbl_im1= Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=20, y=260)
        
        self.im2=Image.open("images/category.jpg")
        self.im2=self.im2.resize((500,200),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)
        
        self.lbl_im2= Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=550, y=260)
        
        self.show()
#======================================================================= 

    #====Adding Data from Database==== 

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category Name must be required", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invalid Category Name try again!!",parent=self.root)
                else:
                    cur.execute("Insert into category(name) values(?)",(
                        self.var_name.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success!","Category ID added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    #====Showing Data from Database====
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    #====Get Data from Database====
                
    def get_data(self,ev):   
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1]),

    #====Delete Data in Database====      

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:       
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error","Category No must be required", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Category ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op== True:
                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","category deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    #====Clear Data====
    
    def clear(self):
        self.var_cat_id.set(""),
        self.var_name.set(""),
        self.show() 

if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop() 
