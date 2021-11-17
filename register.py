import tkinter
import tkinter.messagebox
from PIL import ImageTk,Image
from subprocess import call
t=tkinter.Tk()
t.title('employee')
t.geometry('800x500')

p=Image.open("C:\\Users\\keerthana\\Desktop\\employeereg\\image.jpg")
p=p.resize((500,500))
p=ImageTk.PhotoImage(p)

pic=tkinter.Label(t,image=p)
pic.place(x=0,y=0)

a=tkinter.Label(text="Employee creation",bg="white",fg="black",font=('Times New Roman',35,'underline','bold'))
a.place(x=70,y=10)


b=tkinter.Label(text="Employee id",bg="white",fg="black",font=('Times New Roman',18,'bold'))
b.place(x=10,y=120)

c=tkinter.Entry(width=30)
c.place(x=275,y=120)

d=tkinter.Label(text="Name",bg="white",fg="black",font=('Times New Roman',18,'bold'))
d.place(x=10,y=160)

e=tkinter.Entry(width=30)
e.place(x=275,y=160)

f=tkinter.Label(text="Age",bg="white",fg="black",font=('Times New Roman',18,'bold'))
f.place(x=10,y=200)

g=tkinter.Entry(width=30)
g.place(x=275,y=200)

h=tkinter.Label(text="Salary",bg="white",fg="black",font=('Times New Roman',18,'bold'))
h.place(x=10,y=240)

i=tkinter.Entry(width=30)
i.place(x=275,y=240)

j=tkinter.Label(text="Location",bg="white",fg="black",font=('Times New Roman',18,'bold'))
j.place(x=10,y=280)

k=tkinter.Entry(width=30)
k.place(x=275,y=280)



def abcd():
       Employee_id=c.get()
       Name=e.get()
       Age=g.get()
       Salary=i.get()
       Location=k.get()



       if(Employee_id=="" or Name==""or Age==""or Salary==""or Location==""):
              tkinter.messagebox.showerror('error','please complete fields')
       import pymysql
       x=pymysql.connect(host='localhost',user='root',password='root1',db='avodha')
       cur=x.cursor()
       cur.execute("insert into employee values('"+Employee_id+"','"+Name+"','"+Age+"','"+Salary+"','"+Location+"')")
       x.commit()
       x.close()
       tkinter.messagebox.showinfo('Thank you','Thanks for visiting')
       t.destroy()

       call(['python','next.py'])


f=tkinter.Button(text="Submit",bg="white",fg="black",font=('times new roman',20,'bold'),command=abcd)
f.place(x=225,y=350)



t.mainloop()
