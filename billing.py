from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk, messagebox
import sqlite3
import os
import time
import tempfile

class billClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.cart_list=[]
        self.chk_print=0
        
        # ====title====
        
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Papri Filling Station", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0,y=0,relwidth=1)

        # ====btn_logout====
        
        btn_logout = Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"),
                            bg="yellow", cursor="hand2").place(x=1150, y=10, width=150, height=50)

        # ====clock====
        
        self.lbl_clock = Label(self.root,text="Welcome to Papri Filling Station\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.root.config(bg="white")
        
        #====Product Frame====
        
        #====Variables====
        
        self.var_search=StringVar()
        
        #====Frame_01====
        
        productFrame1=Frame(self.root,bd=4,relief=RIDGE)
        productFrame1.place(x=6,y=110,width=400,height=560)
        
        pTitle=Label(productFrame1,text="All Products",font=("times new roman",20,"bold"),bg="#262626",fg="white")
        pTitle.pack(side=TOP,fill=X)
        
        #====Frame_02====
        
        productFrame2=Frame(productFrame1,bd=2,relief=RIDGE,bg="white")
        productFrame2.place(x=2,y=42,width=388,height=90)
        
        lbl_search=Label(productFrame2,text="Search Product by Name",font=("times new roman",15,"bold"),bg="white",fg="green")
        lbl_search.place(x=2,y=5)
        
        lbl_name=Label(productFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white",)
        lbl_name.place(x=2,y=45)
        
        txt_name=Entry(productFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow",)
        txt_name.place(x=130,y=47,width=140,height=22)
        
        btn_search=Button(productFrame2,text="Search",command=self.search,font=("times new roman",13),bg="#2196f3",fg="white",cursor="hand2")
        btn_search.place(x=288,y=45,width=90,height=25)
        
        btn_show_all=Button(productFrame2,text="Show All",command=self.show,font=("times new roman",13),bg="#083531",fg="white",cursor="hand2")
        btn_show_all.place(x=288,y=10,width=90,height=25)
        
        #====Frame03====
        
        productFame3=Frame(productFrame1,bd=3,relief=RIDGE)
        productFame3.place(x=2,y=140,width=388,height=385)
        scrolly=Scrollbar(productFame3,orient=VERTICAL)
        scrollx=Scrollbar(productFame3,orient=HORIZONTAL)
        
        self.product_Table=ttk.Treeview(productFame3,columns=("pid","name","price","quantity","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X) 
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)
            
        self.product_Table.heading("pid",text="Pro ID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("quantity",text="Quantity")
        self.product_Table.heading("status",text="Status")
        self.product_Table["show"]="headings"
        
        self.product_Table.column("pid",width=40)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=60)
        self.product_Table.column("quantity",width=80)
        self.product_Table.column("status",width=80)        
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        
    
        lbl_note=Label(productFrame1,text="Note: 'Enter 0 quantity to remove product from cart'",font=("times new roman",11),bg="white",fg="red",anchor="w")
        lbl_note.pack(side=BOTTOM,fill=X)
        
        #====Cal Cart Frame====
        
        cal_cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        cal_cart_Frame.place(x=410,y=110,width=530,height=380)
        
        #====Calculator Frame====
        
        #====Variable====
        
        self.var_cal_input=StringVar()
        
        #====Calculator input====
        
        cal_Frame=Frame(cal_cart_Frame,bd=2,relief=RIDGE,bg="white")
        cal_Frame.place(x=5,y=32,width=267,height=340)
        
        self.text_cal_input=Entry(cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=22,bd=10,relief=GROOVE,state="readonly",justify=RIGHT)
        self.text_cal_input.grid(row=0,columnspan=4)
        
        #====Calculatorrs Buttons====
        
        #====Row01====
        
        btn_7=Button(cal_Frame,text="7",font=("arial",15,"bold"),command=lambda:self.get_input(7),cursor="hand2",bd=5,width=4,pady=11).grid(row=1,column=0)
        btn_8=Button(cal_Frame,text="8",font=("arial",15,"bold"),command=lambda:self.get_input(8),cursor="hand2",bd=5,width=4,pady=11).grid(row=1,column=1)
        btn_9=Button(cal_Frame,text="9",font=("arial",15,"bold"),command=lambda:self.get_input(9),cursor="hand2",bd=5,width=4,pady=11).grid(row=1,column=2)
        btn_sum=Button(cal_Frame,text="+",font=("arial",15,"bold"),command=lambda:self.get_input('+'),cursor="hand2",bd=5,width=4,pady=11).grid(row=1,column=3)
        
        #====Row02====
        
        btn_4=Button(cal_Frame,text="4",font=("arial",15,"bold"),command=lambda:self.get_input(4),cursor="hand2",bd=5,width=4,pady=11).grid(row=2,column=0)
        btn_5=Button(cal_Frame,text="5",font=("arial",15,"bold"),command=lambda:self.get_input(5),cursor="hand2",bd=5,width=4,pady=11).grid(row=2,column=1)
        btn_6=Button(cal_Frame,text="6",font=("arial",15,"bold"),command=lambda:self.get_input(6),cursor="hand2",bd=5,width=4,pady=11).grid(row=2,column=2)
        btn_sub=Button(cal_Frame,text="-",font=("arial",15,"bold"),command=lambda:self.get_input('-'),cursor="hand2",bd=5,width=4,pady=11).grid(row=2,column=3)
        
        #====Row03====
        
        btn_3=Button(cal_Frame,text="3",font=("arial",15,"bold"),command=lambda:self.get_input(3),cursor="hand2",bd=5,width=4,pady=11).grid(row=3,column=0)
        btn_2=Button(cal_Frame,text="2",font=("arial",15,"bold"),command=lambda:self.get_input(2),cursor="hand2",bd=5,width=4,pady=11).grid(row=3,column=1)
        btn_1=Button(cal_Frame,text="1",font=("arial",15,"bold"),command=lambda:self.get_input(1),cursor="hand2",bd=5,width=4,pady=11).grid(row=3,column=2)
        btn_mul=Button(cal_Frame,text="*",font=("arial",15,"bold"),command=lambda:self.get_input('*'),cursor="hand2",bd=5,width=4,pady=11).grid(row=3,column=3)
        
        #====Row04====
        
        btn_0=Button(cal_Frame,text="0",font=("arial",15,"bold"),command=lambda:self.get_input(0),cursor="hand2",bd=5,width=4,pady=16).grid(row=4,column=0)
        btn_c=Button(cal_Frame,text="C",font=("arial",15,"bold"),command=self.clear_cal,cursor="hand2",bd=5,width=4,pady=16).grid(row=4,column=1)
        btn_eq=Button(cal_Frame,text="=",font=("arial",15,"bold"),command=self.perform_cal,cursor="hand2",bd=5,width=4,pady=16).grid(row=4,column=2)
        btn_div=Button(cal_Frame,text="/",font=("arial",15,"bold"),command=lambda:self.get_input('/'),cursor="hand2",bd=5,width=4,pady=16).grid(row=4,column=3)
        
        
        #====Cart Frame====
        
        caTitle=Label(cal_cart_Frame,text="Cart Bill Area",font=("times new roman",15,"bold"),bg="orange",fg="white")
        caTitle.pack(side=TOP,fill=X)
        
        cartFrame=Frame(cal_cart_Frame,bd=3,relief=RIDGE)
        cartFrame.place(x=280,y=30,width=245,height=342)
        scrolly=Scrollbar(cartFrame,orient=VERTICAL)
        scrollx=Scrollbar(cartFrame,orient=HORIZONTAL)
        self.cartTitle=Label(cartFrame,text="Cart\t Total Product [0]",font=("times new roman",12,"bold"),bg="gray")
        self.cartTitle.pack(side=TOP,fill=X)
        
        self.cartTable=ttk.Treeview(cartFrame,columns=("pid","name","price","quantity"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X) 
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)
            
        self.cartTable.heading("pid",text="Pro ID")
        self.cartTable.heading("name",text="Name")
        self.cartTable.heading("price",text="Price")
        self.cartTable.heading("quantity",text="Quantity")
        self.cartTable["show"]="headings"
        
        self.cartTable.column("pid",width=50)
        self.cartTable.column("name",width=100)
        self.cartTable.column("price",width=50)
        self.cartTable.column("quantity",width=50)       
        self.cartTable.pack(fill=BOTH,expand=1)
        self.cartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        
        #====ADD Cart Buttons====
        
        #====variables====
        
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_stock=StringVar()
        
        add_cartwidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        add_cartwidgetsFrame.place(x=410,y=490,width=530,height=120)
        
        lbl_p_name=Label(add_cartwidgetsFrame,text="Product Name",font=("times new roman",12),bg="white",)
        lbl_p_name.place(x=5,y=5)
        
        txt_p_name=Entry(add_cartwidgetsFrame,textvariable=self.var_pname,font=("times new roman",12),bg="lightyellow",state="readonly")
        txt_p_name.place(x=5,y=35,width=190,height=22)
        
        lbl_p_price=Label(add_cartwidgetsFrame,text="Price per QTY",font=("times new roman",12),bg="white",)
        lbl_p_price.place(x=230,y=5)
        
        txt_p_price=Entry(add_cartwidgetsFrame,textvariable=self.var_price,font=("times new roman",12),bg="lightyellow",state="readonly")
        txt_p_price.place(x=230,y=35,width=100,height=22)
        
        lbl_p_quantity=Label(add_cartwidgetsFrame,text="Quantity",font=("times new roman",12),bg="white",)
        lbl_p_quantity.place(x=390,y=5)
        
        txt_p_quantity=Entry(add_cartwidgetsFrame,textvariable=self.var_quantity,font=("times new roman",12),bg="lightyellow")
        txt_p_quantity.place(x=390,y=35,width=100,height=22)
        
        btn_clear_cart=Button(add_cartwidgetsFrame,text="Clear",command=self.clear_cart,font=("times new roman",13,"bold"),bg="light gray",cursor="hand2")
        btn_clear_cart.place(x=6,y=70,width=150,height=30)
        
        btn_add_cart=Button(add_cartwidgetsFrame,text="ADD | Update Cart",command=self.add_update_cart,font=("times new roman",13,"bold"),bg="orange",cursor="hand2")
        btn_add_cart.place(x=220,y=70,width=200,height=30)
        
        #=======Show Stock Frame========
        
        show_stockFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        show_stockFrame.place(x=410,y=610,width=530,height=60)
        
        self.lbl_inStock=Label(show_stockFrame,text="In Stock",font=("times new roman",13,"bold"),bg="blue",fg="white")
        self.lbl_inStock.place(x=2,y=5,width=520,height=50)
        
        #==========Billing Area==========
        
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=950,y=110,width=390,height=410)
        
        bTitle=Label(billFrame,text="Customer Bill Area",font=("times new roman",20,"bold"),bg="red",fg="white")
        bTitle.pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
        #=====Billing Buttons=====
        
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=950,y=520,width=390,height=150)
        
        self.lbl_amnt=Label(billMenuFrame,text="Bill Amnt \n[0]",font=("times new roman",13,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=378,height=68)
        
        #====buttons====
        
        btn_print=Button(billMenuFrame,text="Print",command=self.print_bill,font=("times new roman",13,"bold"),cursor="hand2",bg="green",fg="white")
        btn_print.place(x=2,y=75,width=110,height=70)
        
        btn_clear_all=Button(billMenuFrame,text="Clear All",command=self.clear_all,font=("times new roman",13,"bold"),cursor="hand2",bg="gray",fg="white")
        btn_clear_all.place(x=114,y=75,width=110,height=70)
        
        btn_generate=Button(billMenuFrame,text="Generate/Save Bill",command=self.generate_bill,font=("times new roman",13,"bold"),cursor="hand2",bg="purple",fg="white")
        btn_generate.place(x=226,y=75,width=158,height=70)
        
        # ====Footer====
        
        lbl_footer = Label(self.root,text="Inventory Management System | Devloped by Sarwar Hossain. For any query, Please contact at +8801719544363",font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        
        self.show()
        self.bill_updates()
        # self.bill_top()
        self.update_date_time()
#=====================================================================================================================
    
    #====All Functions====
    
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)
        
    def clear_cal(self):
        self.var_cal_input.set('')
        
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
    
    #=======Showing Data from Product Table=======
    
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select pid,name,price,quantity,status from product where status='Active'")
            rows=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    #====Search====
    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("Select pid,name,price,quantity,status from product where name LIKE '%"+self.var_search.get()+"%' and status='Active'" )
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root) 
        
        #====Get Data==== 
          
    def get_data(self,ev):   
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']    
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_quantity.set('1')
    
    def get_data_cart(self,ev):   
        f=self.cartTable.focus()
        content=(self.cartTable.item(f))
        row=content['values']    
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_quantity.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_stock.set(row[4])
        
    def add_update_cart(self):
        if self.var_pid.get()=='':
           messagebox.showerror("Error","Please select Product from the list",parent=self.root)
        elif self.var_quantity.get()=='':
           messagebox.showerror("Error","Quantity is required",parent=self.root)
        elif int(self.var_quantity.get())>int(self.var_stock.get()):
           messagebox.showerror("Error","Invalid Quantity",parent=self.root) 
             
        else:
            price_cal=(int(self.var_quantity.get())*float(self.var_price.get()))
            price_cal=float(price_cal)
            price_cal =self.var_price.get()
            
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_quantity.get(),self.var_stock.get()]
            
            #=====Update Cart====
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                index_=+1
            if present=='yes':
                op=messagebox.askyesno("Confermation","Product is already present\nDo you want to Update| Remove from the cart list",parent=self.root)
                if op==TRUE:
                    if self.var_quantity.get()=='0':
                        self.cart_list.pop(index_)
                    else:
                        # self.cart_list[index_][2]=price_cal #price
                        self.cart_list[index_][3]=self.var_quantity.get() #Quantity
            else:
                
                self.cart_list.append(cart_data)
            self.show_cart()
            self.bill_updates()
            
    def bill_updates(self):
        self.bill_amnt=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*float(row[3]))
        self.lbl_amnt.config(text=f"Bill Amount (Taka)\n[{str(self.bill_amnt)}]")
        self.cartTitle.config(text=f"Cart\t Total Product [{str(len(self.cart_list))}]")
            
    def show_cart(self):
        try:
            self.cartTable.delete(*self.cartTable.get_children())
            for row in self.cart_list:
                self.cartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
    
    def generate_bill(self):
        if len(self.cart_list)==0:
            messagebox.showerror("Error","Please add product to cart!!!",parent=self.root)
        else:
            self.bill_top()
            self.bill_middle()
            self.bill_bottom()
        fp=open(f"bill/{str(self.invoice)}.txt","w")
        fp.write(self.txt_bill_area.get('1.0',END))
        fp.close()
        messagebox.showinfo("Saved","Bill has been Generated/Saved in Backend",parent=self.root)
        self.chk_print=1
        
    #=====Billing Top=====
    
    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%y"))
        bill_top_temp=f'''
\t Papri Filling Station
\t Propitor: MD. Wajed Ali
\t Boraibari,Gongachora,Rangpur
{str("="*45)}
 Bill No: {str(self.invoice)}\t\t\t Date: {str(time.strftime("%d/%m/%y"))}
{str("="*45)}
 Product Name: \t\t\tQty\tPrice
{str("="*45)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)
        
    #=====Billing Middle=====
    
    def bill_middle(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                
                if int(row[3])==int(row[4]):
                    status='Inactive'
                elif int(row[3])!=int(row[4]):
                    status='Active'
                    
                price=float(row[2])*int(row[3])
                price=str(price)
                self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tTaka "+price)
                
                #====Update Quantity in Product Table=====
                
                cur.execute("update product set quantity=?,status=? where pid=?",(
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    #=====Billing Bottom=====
    
    def bill_bottom(self):
        bill_bottom_temp= f'''
{str("="*45)}
 Bill Amount\t\t\t\tTaka {self.bill_amnt}
{str("="*45)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)
        
    #====Clear Cart====
    
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_quantity.set('')
        self.lbl_inStock.config(text=f"In Stock ")
        self.var_stock.set('')
    
    #====Clear All====
    
    def clear_all(self):
        del self.cart_list[:]
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart\t Total Product [0]")
        self.var_search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print=0
        self.lbl_amnt.config(text=f"Bill Amount (Taka)\n[0]")
    
    #=========Update Date & Time==========
      
    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f"Welcome to Papri Filling Station\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)
    
    #=====Bill Print=====
    
    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo("Print","Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Print","Please generate bill, to print receipt ",parent=self.root)
            
            
    #====Logout====
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")
        
if __name__ == "__main__":
    root = Tk()
    obj = billClass(root)
    root.mainloop()
