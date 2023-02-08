from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3

class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Filling Station Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #=========================
        
        #====Search Variables====
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        #====Content Variables====
        
        self.var_emp_id=StringVar()
        self.var_nid=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        
        
        #====SearchFrame====
        
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("time new romans",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=40,width=600,height=70)
        
        #====Option====
        
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby, values=("Select","Email","Name","Contact"),state="readonly",justify=CENTER,font=("time new romans",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("time new romans",15),bg="lightyellow").place(x=200,y=10)
        txt_button=Button(SearchFrame,text="Search",command=self.search,font=("time new romans",15),bg="#4caf50",cursor="hand2").place(x=410,y=9,height=30)
        
        #====Title===
        
        title=Label(self.root,text="Employee Details",font=("time new romans",15),bg="#0f4d7d",fg="white").pack(side=TOP,fill=X)
        
        #====Content====
        
        #====Row_01====
        
        lbl_empid=Label(self.root,text="Emp ID",font=("time new romans",15),bg="white").place(x=50,y=150)
        lbl_nid=Label(self.root,text="NID",font=("time new romans",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",font=("time new romans",15),bg="white").place(x=750,y=150)
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("time new romans",15),bg="lightyellow").place(x=150,y=150,width=180)
        txt_nid=Entry(self.root,textvariable=self.var_nid,font=("time new romans",15),bg="lightyellow").place(x=500,y=150,width=180)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("time new romans",15),bg="lightyellow").place(x=850,y=150,width=180) 
        
        #====Row_02==== 

        lbl_name=Label(self.root,text="Name",font=("time new romans",15),bg="lightyellow").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("time new romans",15),bg="lightyellow").place(x=350,y=190)
        lbl_doj=Label(self.root,text="D.O.J",font=("time new romans",15),bg="lightyellow").place(x=750,y=190)           
        txt_name=Entry(self.root,textvariable=self.var_name,font=("time new romans",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("time new romans",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_contact=Entry(self.root,textvariable=self.var_doj,font=("time new romans",15),bg="lightyellow").place(x=850,y=190,width=180)
        
        #====Row_03==== 

        lbl_email=Label(self.root,text="Email",font=("time new romans",15),bg="lightyellow").place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",font=("time new romans",15),bg="lightyellow").place(x=350,y=230)
        lbl_pass=Label(self.root,text="User Type",font=("time new romans",15),bg="lightyellow").place(x=750,y=230)     
        txt_email=Entry(self.root,textvariable=self.var_email,font=("time new romans",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("time new romans",15),bg="lightyellow").place(x=500,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype, values=("Admin","Employee"),state="readonly",justify=CENTER,font=("time new romans",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)
        
        #====Row_04==== 
        
        lbl_address=Label(self.root,text="Address",font=("time new romans",15),bg="lightyellow").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("time new romans",15),bg="lightyellow").place(x=500,y=270)
        self.txt_address=Text(self.root,font=("time new romans",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("time new romans",15),bg="lightyellow").place(x=600,y=270,width=110,height=28)
        
        #====Buttons====
        
        txt_add=Button(self.root,text="Save",command=self.add,font=("time new romans",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=30)
        txt_update=Button(self.root,text="Update",command=self.update,font=("time new romans",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=30)
        txt_delete=Button(self.root,text="Delete",command=self.delete,font=("time new romans",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=30)
        txt_clear=Button(self.root,text="Clear",command=self.clear,font=("time new romans",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=30)
        
        #====Footer====
        
        lbl_footer=Label(self.root,text="Filling Station Management System | Devloped by Sarwar Hossain. For any query, Please contact at +8801719544363",font=("roboto",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X) 
        
        #====Employee Details====
        
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=300)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.employeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","nid","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X) 
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.employeeTable.xview)
        scrolly.config(command=self.employeeTable.yview)
            
        self.employeeTable.heading("eid",text="EMP ID")
        self.employeeTable.heading("name",text="Name")
        self.employeeTable.heading("email",text="Email")
        self.employeeTable.heading("nid",text="NID")
        self.employeeTable.heading("contact",text="Contact")
        self.employeeTable.heading("dob",text="DOB")
        self.employeeTable.heading("doj",text="DOJ")
        self.employeeTable.heading("pass",text="Password")
        self.employeeTable.heading("utype",text="User Type")
        self.employeeTable.heading("address",text="Address")
        self.employeeTable.heading("salary",text="Salary")
        
        self.employeeTable["show"]="headings"
        
        self.employeeTable.column("name",width=90)
        self.employeeTable.column("eid",width=100)
        self.employeeTable.column("email",width=100)
        self.employeeTable.column("nid",width=100)
        self.employeeTable.column("contact",width=100)
        self.employeeTable.column("dob",width=100)
        self.employeeTable.column("doj",width=100)
        self.employeeTable.column("pass",width=100)
        self.employeeTable.column("utype",width=100)
        self.employeeTable.column("address",width=100)
        self.employeeTable.column("salary",width=100)        
        self.employeeTable.pack(fill=BOTH,expand=1)
        self.employeeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#======================================================================= 

    #====Adding Data from Database==== 

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required", parent=self.root)
            elif self.var_name.get()=="":
                messagebox.showerror("Error","Name must be required", parent=self.root)
            elif self.var_pass.get()=="":
                messagebox.showerror("Error","Password must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Employee ID is already taken, try different",parent=self.root)
                else:
                    cur.execute("Insert into employee(eid,name,email,nid,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                            self.var_emp_id.get(),
                                            self.var_name.get(),
                                            self.var_email.get(),
                                            self.var_nid.get(),
                                            self.var_contact.get(),
                                            self.var_dob.get(),
                                            self.var_doj.get(),
                                            self.var_pass.get(),
                                            self.var_utype.get(),
                                            self.txt_address.get('1.0',END),
                                            self.var_salary.get()    
                    ))
                    con.commit()
                    messagebox.showinfo("Success!","Employee added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    #====Showing Data from Database====
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from employee")
            rows=cur.fetchall()
            self.employeeTable.delete(*self.employeeTable.get_children())
            for row in rows:
                self.employeeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    #====Get Data from Database====
                
    def get_data(self,ev):   
        f=self.employeeTable.focus()
        content=(self.employeeTable.item(f))
        row=content['values']
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_nid.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END,row[9]),
        self.var_salary.set(row[10])
        
    #====Update Data in Database====      

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required", parent=self.root)
            elif self.var_name.get()=="":
                messagebox.showerror("Error","Name must be required", parent=self.root)
            elif self.var_pass.get()=="":
                messagebox.showerror("Error","Password must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,nid=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                            self.var_name.get(),
                                            self.var_email.get(),
                                            self.var_nid.get(),
                                            self.var_contact.get(),
                                            self.var_dob.get(),
                                            self.var_doj.get(),
                                            self.var_pass.get(),
                                            self.var_utype.get(),
                                            self.txt_address.get('1.0',END),
                                            self.var_salary.get(),
                                            self.var_emp_id.get(),    
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 

    #====Delete Data in Database====      

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:       
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op== True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee deleted successfully", parent=self.root)
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 
    
    #====Clear Data in Database====     

    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_nid.set(""),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Employee"),
        self.txt_address.delete('1.0',END),
        self.var_salary.set("")
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
                cur.execute("Select * from employee where "+self.var_searchby.get()+ " LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.employeeTable.delete(*self.employeeTable.get_children())
                    for row in rows:
                        self.employeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)     

if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop() 
