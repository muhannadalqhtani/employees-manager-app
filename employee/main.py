from tkinter import * 
from tkinter import ttk

root = Tk()
root.title('تطبيق ادارة الموظفين')
root.geometry('1240x615+90+90')
root.resizable(True, True)
root.configure(bg='gray')

# اضافة صورة
logo = PhotoImage(file='logo1.png')
lbl_logo = Label(root, image=logo , bg='gray')
lbl_logo.place(x=10 , y=500)




#========= Entries frame =======
entries_frame = Frame(root, bg='Blue')
entries_frame.place(x=1, y=1, width=360, height=510)

title = Label(entries_frame, text='Employee company ', font=('calibri', 18, 'bold'), bg='gray', fg='white')
title.place(x=10, y=1)

# بيانات الموظفين  
# اسم الموظف 
lblName = Label(entries_frame, text="Name", font=('calibri', 16), bg='gray', fg='white')
lblName.place(x=10, y=50)

# مربع الادخال 
textName = Entry(entries_frame, width=20, font=('calibri', 18), bg='white', fg='black')
textName.place(x=120, y=50)

# اسم الوظيفة
lbljob = Label(entries_frame, text="Job", font=('calibri', 16), bg='gray', fg='white')
lbljob.place(x=10, y=90)

# مربع الادخال 
textjob = Entry(entries_frame, width=20, font=('calibri', 18), bg='white', fg='black')
textjob.place(x=120, y=90)

# الجنس 
lblGender = Label(entries_frame, text="Gender", font=('calibri', 16), bg='gray', fg='white')
lblGender.place(x=10, y=130)

# مربع الادخال 
comboGender = ttk.Combobox(entries_frame, width=10, font=('calibri', 16))
comboGender['values'] = ("Male", "Female", "other")
comboGender.place(x=120, y=130)

# العمر 
lblAge = Label(entries_frame, text="age", font=('calibri', 16), bg='gray', fg='white')
lblAge.place(x=10, y=170)

# مريع الادخال 
textAge = Entry(entries_frame, width=20, font=('calibri', 18), bg='white', fg='black')
textAge.place(x=120, y=170)

# الايميل 
lblEmail = Label(entries_frame, text="@Email", font=('calibri', 16), bg='gray', fg='white')
lblEmail.place(x=10, y=210)

# مريع الادخال 
textEmail = Entry(entries_frame, width=20, font=('calibri', 18), bg='white', fg='black')
textEmail.place(x=120, y=210)

# التواصل
lblContact = Label(entries_frame, text="contact", font=('calibri', 16), bg='gray', fg='white')
lblContact.place(x=10, y=250)

# مريع الادخال 
textContact = Entry(entries_frame, width=20, font=('calibri', 18), bg='white', fg='black')
textContact.place(x=120, y=250)

# مكان السكن 
lblAddress = Label(entries_frame, text="Address :", font=('calibri', 16), bg='gray', fg='white')
lblAddress.place(x=10, y=290)

# مريع الادخال 
textAdress = Text(entries_frame, width=30, height=2, font=('calibri', 18), bg='white', fg='black')
textAdress.place(x=10, y=330)





#========= Define=======

def hide ():

    root.geometry("375x515")
def show():
    root.geometry('1240x615')



btnhide = Button(entries_frame , text='HIDE' ,cursor='hand2', command=hide)
btnhide.place(x=270 , y=10)

btnshow = Button(entries_frame , text='SHOW' ,cursor='hand2', command=show)
btnshow.place(x=320 , y=10)





# الازرار 
btn_frame = Frame(entries_frame, bg='gray', bd=1, relief=SOLID)
btn_frame.place(x=8, y=400, width=335, height=100)

btnAdd = Button(btn_frame, text='Add details', width=14, height=1, font=('calibri', 18), fg='white', bg='#16a085', bd=0)
btnAdd.place(x=4, y=5)

btnEdit = Button(btn_frame, text='Update details', width=14, height=1, font=('calibri', 18), fg='white', bg='#2980b9', bd=0)
btnEdit.place(x=4, y=50)

btnDelete = Button(btn_frame, text='Delete details', width=14, height=1, font=('calibri', 18), fg='white', bg='#c0392b', bd=0)
btnDelete.place(x=170, y=5)

btnClear = Button(btn_frame, text='Clear details', width=14, height=1, font=('calibri', 18), fg='white', bg='#f39c12', bd=0)
btnClear.place(x=170, y=50)

#------- Table Frame --------------
# يمكنك إضافة كود الجدول هنا
#خلفية جدول
tree_fram = Frame(root,bg='white')
tree_fram.place(x=365 , y=1 ,width=875, height=610)
style=ttk.Style()
# تصميم الاعمدة
style.configure("mystyle.Treeview", font=('Calibri',13),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri',13))
#ترقيم الاعمدة
tv = ttk.Treeview (tree_fram, columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
#تسميه الاعمدة
tv.heading("1", text="ID")
tv.column("1",width="40")

tv.heading("2", text="Name")
tv.column("2",width="140")

tv.heading("3", text="Age")
tv.column("3",width="50")

tv.heading("4", text="Job")
tv.column("4",width="120")

tv.heading("5", text="Email")
tv.column("5",width="150")

tv.heading("6", text="Gender")
tv.column("6",width="90")

tv.heading("7", text="Mobile")
tv.column("7",width="150")

tv.heading("8", text="Address")
tv.column("8",width="150")
#يظهر الاكواد بشكل مرتب
tv['show']='headings'
# يظهر في اعلى برنامج
tv.place(x=1 , y=1, height=610 )


root.mainloop()
