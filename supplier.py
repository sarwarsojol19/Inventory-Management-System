from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Filling Station Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #=========================
        
        #====Search Variables====
        
        self.var_searchtxt=StringVar()
        
        #====Content Variables====
        
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        #====self.root====
        
        #====Option====
        
        lbl_search=Label(self.root,text="Invoice No",font=("arial",15,),bg="white")
        lbl_search.place(x=550,y=80)
        
        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=("arial",15),bg="lightyellow").place(x=650,y=80,height=35)
        txt_button=Button(self.root,text="Search",command=self.search,font=("arial",15),bg="#4caf50",cursor="hand2").place(x=900,y=80,width=110,height=35)
        
        #====Title===
        
        title=Label(self.root,text="Supplier Details",font=("arial",20,"bold"),bg="#0f4d7d",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)
        
        #====Content====
        
        #====Row_01====
        
        lbl_supplier_invoice=Label(self.root,text="Invoice No",font=("arial",15),bg="white").place(x=50,y=80)
        txt_empid=Entry(self.root,textvariable=self.var_sup_invoice,font=("arial",15),bg="lightyellow").place(x=180,y=80,width=180)
        
        #====Row_02====

        lbl_name=Label(self.root,text="Name",font=("arial",15),bg="lightyellow").place(x=50,y=120)          
        txt_name=Entry(self.root,textvariable=self.var_name,font=("arial",15),bg="lightyellow").place(x=180,y=120,width=180)
        
        #====Row_03====

        lbl_contact=Label(self.root,text="Contact",font=("arial",15),bg="white").place(x=50,y=160)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("arial",15),bg="lightyellow").place(x=180,y=160,width=180)
        
        #====Row_04==== 
        
        lbl_desc=Label(self.root,text="Description",font=("arial",15),bg="lightyellow").place(x=50,y=200)
        self.txt_desc=Text(self.root,font=("arial",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=200,width=300,height=100)
        
        #====Buttons====
        
        btn_add=Button(self.root,text="Save",command=self.add,font=("arial",15),bg="#2196f3",fg="white",cursor="hand2").place(x=50,y=310,width=110,height=35)
        btn_update=Button(self.root,text="Update",command=self.update,font=("arial",15),bg="#4caf50",fg="white",cursor="hand2").place(x=170,y=310,width=110,height=35)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("arial",15),bg="#f44336",fg="white",cursor="hand2").place(x=290,y=310,width=110,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("arial",15),bg="#607d8b",fg="white",cursor="hand2").place(x=410,y=310,width=110,height=35)

        #====Supplier Details====
        
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=550,y=140,width=500,height=300)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.suppilerTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X) 
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.suppilerTable.xview)
        scrolly.config(command=self.suppilerTable.yview)
            
        self.suppilerTable.heading("invoice",text="Invoice No")
        self.suppilerTable.heading("name",text="Name")
        self.suppilerTable.heading("contact",text="Contact")
        self.suppilerTable.heading("desc",text="Description")
        
        self.suppilerTable["show"]="headings"
        
        self.suppilerTable.column("invoice",width=100)
        self.suppilerTable.column("name",width=100)
        self.suppilerTable.column("contact",width=100)
        self.suppilerTable.column("desc",width=100)       
        self.suppilerTable.pack(fill=BOTH,expand=1)
        self.suppilerTable.bind("<ButtonRelease-1>",self.get_data)
        
        self.show()
        
#======================================================================= 

    #====Adding Data from Database==== 

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invalid Invoice Number try different",parent=self.root)
                else:
                    cur.execute("Insert into supplier(invoice,name,contact,desc) values(?,?,?,?)",(
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),  
                    ))
                    con.commit()
                    messagebox.showinfo("Success!","Invoice added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    #====Showing Data from Database====
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.suppilerTable.delete(*self.suppilerTable.get_children())
            for row in rows:
                self.suppilerTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    #====Get Data from Database====
                
    def get_data(self,ev):   
        f=self.suppilerTable.focus()
        content=(self.suppilerTable.item(f))
        row=content['values']
        self.var_sup_invoice.set(row[0]),
        self.var_name.set(row[1]),
        self.var_contact.set(row[2]),
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[3]),

    #====Update Data in Database====      

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No. must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),
                        self.var_sup_invoice.get(),    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 

    #====Delete Data in Database====      

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:       
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice No must be required", parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice Number",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op== True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier deleted successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 
    
    #====Clear Data in Database====     

    def clear(self):
        self.var_sup_invoice.set(""),
        self.var_name.set(""),
        self.var_contact.set(""),
        self.txt_desc.delete('1.0',END),
        self.var_searchtxt.set("")
        self.show() 
        
    #====Search====
    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice Number should be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.suppilerTable.delete(*self.suppilerTable.get_children())
                    self.suppilerTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)     
        #====Footer====
        
        lbl_footer=Label(self.root,text="Filling Station Management System | Devloped by Sarwar Hossain. For any query, Please contact at +8801719544363",font=("roboto",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X) 
        
if __name__=="__main__":
    root=Tk()
    obj=supplierClass(root)
    root.mainloop() 
