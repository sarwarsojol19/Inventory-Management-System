from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #====Variables====
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()

        
        #====Product Frame====
        
        product_frame=Frame(self.root,bd=3,relief=RIDGE)
        product_frame.place(x=10,y=10, width=450, height=480)
        
        #====Title===
        
        title=Label(product_frame,text="Product Details",font=("time new romans",20),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        
        #====Product Categories====
        
        #====Row-01====
        
        lbl_cat=Label(product_frame,text="Category",font=("time new romans",15)).place(x=25,y=60)
        cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat, values=self.cat_list,state="readonly",justify=CENTER,font=("time new romans",15))
        cmb_cat.place(x=150,y=60,width=250)
        cmb_cat.current(0)
        
        #====Row-02====
        
        lbl_sup=Label(product_frame,text="Supplier",font=("time new romans",15)).place(x=25,y=110)
        cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup, values=self.sup_list,state="readonly",justify=CENTER,font=("time new romans",15))
        cmb_sup.place(x=150,y=110,width=250)
        cmb_sup.current(0)
        
        #====Row-03====
        
        lbl_name=Label(product_frame,text="Name",font=("time new romans",15)).place(x=25,y=160)
        txt_name=Entry(product_frame,textvariable=self.var_name,font=("time new romans",15),bg="lightyellow").place(x=150,y=160,width=250)
        
        #====Row-04====
        
        lbl_price=Label(product_frame,text="Price",font=("time new romans",15)).place(x=25,y=210)
        txt_price=Entry(product_frame,textvariable=self.var_price,font=("time new romans",15),bg="lightyellow").place(x=150,y=210,width=250)
        
        #====Row-05====
        
        lbl_quantity=Label(product_frame,text="Quantity",font=("time new romans",15)).place(x=25,y=260)
        txt_quntity=Entry(product_frame,textvariable=self.var_quantity,font=("time new romans",15),bg="lightyellow").place(x=150,y=260,width=250)
        
        #====Row-06====
        
        lbl_status=Label(product_frame,text="Status",font=("time new romans",15)).place(x=25,y=310)
        cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status, values=("Active","Inactive"),state="readonly",justify=CENTER,font=("time new romans",15))
        cmb_status.place(x=150,y=310,width=250)
        cmb_status.current(0)
        
        #====Button====
        
        txt_add=Button(product_frame,text="Save",command=self.add,font=("time new romans",15),bg="#2196f3",fg="white",cursor="hand2").place(x=25,y=400,width=80,height=40)
        txt_update=Button(product_frame,text="Update",command=self.update,font=("time new romans",15),bg="#4caf50",fg="white",cursor="hand2").place(x=125,y=400,width=80,height=40)
        txt_delete=Button(product_frame,text="Delete",command=self.delete,font=("time new romans",15),bg="#f44336",fg="white",cursor="hand2").place(x=225,y=400,width=80,height=40)
        txt_clear=Button(product_frame,text="Clear",command=self.clear,font=("time new romans",15),bg="#607d8b",fg="white",cursor="hand2").place(x=325,y=400,width=80,height=40)
        
        #====SearchFrame====
        
        SearchFrame=LabelFrame(self.root,text="Search Product",font=("time new romans",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=475,y=20,width=600,height=90)
        
        #====Option====
        
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=("Select","Category","Supplier","Name"),state="readonly",justify=CENTER,font=("time new romans",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("time new romans",15),bg="lightyellow").place(x=200,y=10)
        txt_button=Button(SearchFrame,text="Search",command=self.search,font=("time new romans",15),bg="#4caf50",cursor="hand2").place(x=480,y=7,height=35)
        
        #====Product Details====
        
        pro_frame=Frame(self.root,bd=3,relief=RIDGE)
        pro_frame.place(x=475,y=120,width=600)
        
        scrolly=Scrollbar(pro_frame,orient=VERTICAL)
        scrollx=Scrollbar(pro_frame,orient=HORIZONTAL)
        
        self.productTable=ttk.Treeview(pro_frame,columns=("pid","Category","Supplier","name","price","quantity","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X) 
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.productTable.xview)
        scrolly.config(command=self.productTable.yview)
        
        self.productTable.heading("pid",text="Pro ID")
        self.productTable.heading("Category",text="Category")
        self.productTable.heading("Supplier",text="Supplier")
        self.productTable.heading("name",text="Name")
        self.productTable.heading("price",text="Price")
        self.productTable.heading("quantity",text="Quantity")
        self.productTable.heading("status",text="Status")
        
        self.productTable["show"]="headings"
        
        self.productTable.column("pid",width=50)
        self.productTable.column("Category",width=50)
        self.productTable.column("Supplier",width=50)
        self.productTable.column("name",width=50)
        self.productTable.column("price",width=50)
        self.productTable.column("quantity",width=50)
        self.productTable.column("status",width=50)        
        self.productTable.pack(fill=BOTH,expand=1)
        self.productTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#======================================================================= 

    #====Fetching Data from Categoy & Supplier Table====
    
    def fetch_cat_sup(self):
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[1])        
            cur.execute("Select * from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[1])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    #====Adding Data from Database==== 

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="Empty":
                messagebox.showerror("Error","All fields are required", parent=self.root)
            else:
                cur.execute("Select * from product where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Product ID is already taken, try different",parent=self.root)
                else:
                    cur.execute("Insert into product(Category,Supplier,name,price,quantity,status) values(?,?,?,?,?,?)",(
                                            self.var_cat.get(),
                                            self.var_sup.get(),
                                            self.var_name.get(),
                                            self.var_price.get(),
                                            self.var_quantity.get(),
                                            self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success!","Product added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    #====Showing Data from Database====
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from product")
            rows=cur.fetchall()
            self.productTable.delete(*self.productTable.get_children())
            for row in rows:
                self.productTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    #====Get Data from Database====
                
    def get_data(self,ev):   
        f=self.productTable.focus()
        content=(self.productTable.item(f))
        row=content['values']
        self.var_pid.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_sup.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_quantity.set(row[5]),
        self.var_status.set(row[6]),
        
    #====Update Data in Database====      
    
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Name must be required", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,quantity=?,status=? where pid=?",(
                                            self.var_cat.get(),
                                            self.var_sup.get(),
                                            self.var_name.get(),
                                            self.var_price.get(),
                                            self.var_quantity.get(),
                                            self.var_status.get(),
                                            self.var_pid.get(),    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 

    #====Delete Data in Database====      

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:       
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Product ID must be required", parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op== True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product deleted successfully", parent=self.root)
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 
    
    #====Clear Data in Database====     

    def clear(self):
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_quantity.set(""),
        self.var_status.set("Active"),
        self.var_pid.set(""),
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show() 
        
        
    #====Search====
    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select serach by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select * from product where "+self.var_searchby.get()+ " LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.productTable.delete(*self.productTable.get_children())
                    for row in rows:
                        self.productTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)     
            
if __name__=="__main__":
    root=Tk()
    obj=productClass(root)
    root.mainloop() 
