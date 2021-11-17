import tkinter
from tkinter import *
from tkinter import Toplevel, messagebox, filedialog

from PIL import ImageTk,Image

t=Tk()
t.geometry('800x500')

p=Image.open("C:\\Users\\keerthana\\Desktop\\employeereg\\image.jpg")
p=p.resize((800,500))
p=ImageTk.PhotoImage(p)

pic=tkinter.Label(t,image=p)
pic.place(x=0,y=0)

Label(text='Employee id: ',fg='white',bg='navy blue').place(x=10,y=10)
em=Entry()
em.place(x=100,y=12)

Label(text='Name: ',fg='white',bg='navy blue').place(x=10,y=40)
na=Entry()
na.place(x=100,y=42)

Label(text='Age: ',fg='white',bg='navy blue').place(x=10,y=70)
ag=Entry()
ag.place(x=100,y=72)

Label(text='Salary: ',fg='white',bg='navy blue').place(x=10,y=100)
sa=Entry()
sa.place(x=100,y=102)

Label(text='Location: ',fg='white',bg='navy blue').place(x=10,y=130)
lo=Entry()
lo.place(x=100,y=132)


def abcd():
                import pymysql
                x=pymysql.connect(host='localhost',
                user='root',
                password='root1',
                db='avodha',
                charset='utf8mb4')
                cur=x.cursor()
                a=em.get()
                b=na.get()
                c=ag.get()
                d=sa.get()
                e=lo.get()
                cur.execute('insert into employee values(%s,%s,%s,%s,%s)',(a,b,c,d,e))
                x.commit()
                x.close()
                tkinter.messagebox.showinfo('Thank you','Name {} Registered successfully....'.format(b))

                

Button(text='submit',command=abcd,fg='black',bg='red',font=('verdana',10,'bold')).place(x=250,y=130)

Label(text='UPDATE',fg='black',bg='blue',font=('verdana',20,'bold')).place(x=10,y=170)

Label(text='DELETE',fg='black',bg='blue',font=('verdana',20,'bold')).place(x=370,y=170)

Label(text='SEARCH',fg='black',bg='blue',font=('verdana',20,'bold')).place(x=380,y=340)


Label(text='Enter id to update: ',fg='white',bg='navy blue').place(x=5,y=230)
ue=Entry()
ue.place(x=150,y=230)


Label(text='Enter name to update: ',fg='white',bg='navy blue').place(x=5,y=270)
un=Entry()
un.place(x=150,y=270)
Label(text='Enter age to update: ',fg='white',bg='navy blue').place(x=5,y=310)
ua=Entry()
ua.place(x=150,y=310)
Label(text='Enter salary to update: ',fg='white',bg='navy blue').place(x=5,y=350)
us=Entry()
us.place(x=150,y=350)
Label(text='Enter Location to update: ',fg='white',bg='navy blue').place(x=5,y=390)
ul=Entry()
ul.place(x=150,y=390)
Label(text='Enter Employee id to delete: ',fg='white',bg='navy blue').place(x=350,y=230)
dl=Entry()
dl.place(x=370,y=270)
Label(text='Enter Employee id to search: ',fg='white',bg='navy blue').place(x=360,y=390)
sl=Entry()
sl.place(x=370,y=420)


def upd():
                import pymysql
                x=pymysql.connect(host='localhost',
                user='root',
                password='root1',
                db='avodha',
                charset='utf8mb4')
                cur=x.cursor()
                uew=ue.get()
                unw=un.get()
                uaw=ua.get()
                usw=us.get()
                ulw=ul.get()
                cur.execute('update employee set name=%s,age=%s,salary=%s,location=%s where employee_id=%s',(unw,uaw,usw,ulw,uew))
                x.commit()
                messagebox.showinfo('Notifications', 'employee_id {} Modified successfully...'.format(uew))

Button(text='apply',command=upd,fg='black',bg='red',font=('verdana',10,'bold')).place(x=200,y=415)
sc=Scrollbar()
sc.pack(side=RIGHT,fill=Y)
tx=Text(height=15,width=25,yscrollcommand=sc.set)
sc.config(command=tx.yview)
tx.place(x=550,y=10)
tx.insert(INSERT,('click on view data button\nto see\ndata sets'))

def delete():
                import pymysql
                x=pymysql.connect(host='localhost',
                user='root',
                password='root1',
                db='avodha',
                charset='utf8mb4')
                cur=x.cursor()
                dew=dl.get()
                cur.execute( 'delete from employee where employee_id=%s',(dew))
                x.commit()
                messagebox.showinfo('Notifications', 'employee_id {} deleted successfully...'.format(dew))
                x.close()
sc=Scrollbar()
sc.pack(side=RIGHT,fill=Y)
tx=Text(height=15,width=25,yscrollcommand=sc.set)
sc.config(command=tx.yview)
tx.delete('1.0',END)
tx.place(x=550,y=10)
tx.insert(INSERT,('click on view data button\nto see\ndata sets'))


           
Button(text='Delete Data',command=delete,fg='black',bg='red',font=('verdana',10,'bold')).place(x=400,y=300)

def search():
                import pymysql
                x=pymysql.connect(host='localhost',
                user='root',
                password='root1',
                db='avodha',
                charset='utf8mb4')
                cur=x.cursor()
                sew=sl.get()

                cur.execute('select * from employee where employee_id=%s',(sew))
                v=cur.fetchall()
                vn=[','.join(map(str,xd))for xd in v]
                
                tx.delete('1.0',END)
                tx.insert(INSERT,('DATA SETS ARE\n-------------\n'))
                for i in vn:
                                tx.insert(INSERT,('%s\n\n'%i))

Button(text='Search Data',command=search,fg='black',bg='red',font=('verdana',10,'bold')).place(x=400,y=460)



def view():
                import pymysql
                x=pymysql.connect(host='localhost',
                user='root',
                password='root1',
                db='avodha',
                charset='utf8mb4')
                cur=x.cursor()
                cur.execute('select * from employee')
                v=cur.fetchall()
                vn=[','.join(map(str,xd))for xd in v]
                
                tx.delete('1.0',END)
                tx.insert(INSERT,('DATA SETS ARE\n-------------\n'))
                for i in vn:
                                tx.insert(INSERT,('%s\n\n'%i))

Button(text='view Data',command=view,fg='black',bg='red',font=('verdana',10,'bold')).place(x=620,y=260)


t.mainloop()










