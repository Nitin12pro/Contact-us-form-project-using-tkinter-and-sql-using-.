import tkinter as tk
from PIL  import Image, ImageTk
import mysql.connector
from tkinter import messagebox

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nitin@0097",
    database="meesho"
)
cr=con.cursor()   




def savinginfo():
    full_nm = ent1.get()
    emal_add = ent2.get()
    ph = ent3.get()
    mesg = ent4.get("1.0",tk.END)
    cr.execute(f"insert into contactinfo(full_name,email_address,phone_number,message)values('({full_nm}','{emal_add}','{ph}','{mesg}');")

    con.commit()

    messagebox.showinfo("Success","Your Information Saved Successfully")

    ent1.delete(0,tk.END)
    ent2.delete(0,tk.END)
    ent3.delete(0,tk.END)
    ent4.delete("1.0",tk.END)


    showinfo.config(text=f"Thank You {full_nm} for Contacting Us. We will reach you soon!")




app = tk.Tk()
app.geometry("1100x700")
app.title("My Contact Us Form")
app.configure(background = "#6ce5d7")

frame1 = tk.Frame(app,relief="raised",borderwidth=5,bg="#a0efe6")
frame1.pack(fill="x")





    


c_lbl = tk.Label(frame1,text="Contact Us Now",fg="white",font = ("Monospace",24,"bold"),bg="#a0efe6")
c_lbl.pack()

frame2=tk.Frame(app,relief="sunken",borderwidth=5,background="white")
frame2.pack(fill="x")

img =Image.open("c.jpeg")
new_img=ImageTk.PhotoImage(img)

ig=tk.Label(frame2,image=new_img,height=200,)
ig.pack()

frame3 = tk.Frame(app,relief = "sunken",borderwidth=5)
frame3.pack(fill="x")


frame4 = tk.Frame(frame3)
frame4.grid(row=0,column=0)


frame5 = tk.Frame(frame3)
frame5.grid(row=0,column=1)


lbl0=tk.Label(frame4,text="")
lbl1=tk.Label(frame4,text="Full Name",font=("robort",16,"bold"))
lbl2=tk.Label(frame4,text="Email Address",font=("robort",16,"bold"))


lbl3=tk.Label(frame5,text="Phone Number",font=("robort",16,"bold"))
lbl4=tk.Label(frame5,text="Message",font=("robort",16,"bold"))


lbl5=tk.Label(frame4,text=":",font=("robort",16,"bold"))
lbl6=tk.Label(frame4,text=":",font=("robort",16,"bold"))

lblx=tk.Label(frame5,text="")
lbl7=tk.Label(frame5,text=":",font=("robort",16,"bold"))
lbl8=tk.Label(frame5,text=":",font=("robort",16,"bold"))

ent1=tk.Entry(frame4,font=("robort",16,"bold"))
ent2=tk.Entry(frame4,font=("robort",16,"bold"))



ent3=tk.Entry(frame5,font=("robort",16,"bold"))
ent4=tk.Text(frame5,font=("robort",16,"bold"),height=2,width=10)

lblx.grid(row=0,column=0,padx=20,pady=5)
lbl1.grid(row=1,column=1)
lbl2.grid(row=2,column=1,pady=18)
lbl5.grid(row=1,column=2)
lbl6.grid(row=2,column=2)
ent1.grid(row=1,column=3)
ent2.grid(row=2,column=3)


lbl0.grid(row=0,column=0,padx=10,pady=5)
lbl3.grid(row=1,column=1)
lbl4.grid(row=2,column=1)
lbl7.grid(row=1,column=2)
lbl8.grid(row=2,column=2)
ent3.grid(row=1,column=3)
ent4.grid(row=2,column=3,pady=18)


fram6=tk.Frame(app)
fram6.pack(fill="x")




btn=tk.Button(fram6,text="Submit",font=("robort",16,"bold"),bg="#185850",fg="white",command=savinginfo)
btn.pack()


showinfo =tk.Label(fram6,text="",font=("robort",14),fg="green",bg="#6ce5d7")
showinfo.pack(pady=20,fill="x")

app.mainloop()
