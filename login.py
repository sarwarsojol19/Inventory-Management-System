from tkinter import*
from PIL import ImageTk #pip install pillow
from tkinter import messagebox
import sqlite3
import os

class login_system:
    def __init__(self,root) :
        self.root=root
        self.root.title("Login to Inventory Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")
        
        #====Variabless====
        
        self.employee_id=StringVar()
        self.password=StringVar()
        #====Image====
        
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200, y=50)
        
        #====Login Frame====
        
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90, width=350, height=450)
        
        title=Label(login_frame,text="LOGIN SYSTEM",font=("times new roma",26,"bold"),bg="white")
        title.place(x=0,y=30,relwidth=1,)
        
        lbl_employee_id=Label(login_frame,text="Employee ID",font=("times new roma",15,"bold"),bg="white",fg="#767171")
        lbl_employee_id.place(x=50,y=100)
        
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roma",15),bg="#ECECEC")
        txt_employee_id.place(x=50,y=140,width=250, height=35)
        
        lbl_pass=Label(login_frame,text="Password",font=("times new roma",15,"bold"),bg="white",fg="#767171")
        lbl_pass.place(x=50,y=190)
        txt_pass=Entry(login_frame,textvariable=self.password,font=("times new roma",15),bg="#ECECEC")
        txt_pass.place(x=50,y=230,width=250, height=35)
        
        btn_login=Button(login_frame,text="Login",command=self.login,font=("times new roma",15),bg="#00B0F0", activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2")
        btn_login.place(x=50,y=280, width=250, height=35)
        
        hr=Label(login_frame,bg="lightgray").place(x=50,y=350,width=250, height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman", 15, "bold")).place(x=150,y=337)
        
        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("times new roman", 15),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=90,y=370)

        #====Animation Image====
        
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")    
        self.im3=ImageTk.PhotoImage(file="images/im3.png") 
        
        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)
        
        self.animate()
        
#===============================All Functions=====================================      
    def animate (self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)
    
    def login (self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error!"," All fields are required.",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user== None:
                    messagebox.showerror("Error!"," Invalid Employee ID or Password",parent=self.root)
                else:
                    if user[0] == "Admin":
                        self.root.destroy()
                        os.system("python dashbord.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)
            
    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.employee_id.get(),))
                email=cur.fetchone()
                if email== None:
                    messagebox.showerror("Error!"," Invalid Employee ID. Try again",parent=self.root)
                else:
                    
                    #====Forget Window====
                    
                    #====Variable====
                    
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_con_pass=StringVar()
                    
                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title("Reset Password")
                    self.forget_win.geometry("400x350+300+100")
                    self.forget_win.focus_force()
                    
                    title=Label(self.forget_win,text="Reset password",font=("times new roman",15,"bold"),bg="#3f51b5",fg="white")
                    title.pack(side=TOP,fill=X)
                    
                    lbl_reset=Label(self.forget_win,text="Enter your OTP send on Registered Email",font=("times new roman",15))
                    lbl_reset.place(x=20,y=60)
                    
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow")
                    txt_reset.place(x=20,y=100,width=250,height=30)
                    
                    self.btn_reset=Button(self.forget_win,text="Submit",font=("times new roman",15),bg="lightblue")
                    self.btn_reset.place(x=280,y=100,width=100,height=30)
                    
                    #====Enter New Password====
                    
                    lbl_new_pass=Label(self.forget_win,text="New password",font=("times new roman",15),)
                    lbl_new_pass.place(x=20,y=160,width=200,height=30)
                    
                    txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",12),bg="lightyellow")
                    txt_new_pass.place(x=20,y=190,width=250,height=30)
                    
                    #====Enter Confirm Password====
                    
                    lbl_con_pass=Label(self.forget_win,text="Confirm password",font=("times new roman",15))
                    lbl_con_pass.place(x=20,y=225,width=200,height=30)
                    
                    txt_con_pass=Entry(self.forget_win,textvariable=self.var_con_pass,font=("times new roman",15),bg="lightyellow")
                    txt_con_pass.place(x=20,y=255,width=250,height=30)
                    
                    self.btn_update=Button(self.forget_win,text="Update",state=DISABLED, font=("times new roman",15),bg="lightblue")
                    self.btn_update.place(x=100,y=300,width=100,height=30)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)        
    
root=Tk()
obj=login_system(root)
root.mainloop()