from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันถึกข้อมูล')
GUI.geometry('500x400')

L1 = Label(GUI,text='เกมเป่ายิงฉุบ' ,font=('Angsana New',30),fg='green')
L1.pack()
#####################################

def Button1():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text )

FB1 = Frame(GUI)
FB1.place(x=200,y=200)
B1 = ttk.Button(FB1,text = 'เงินมีอยู่กี่บาท',command=Button1)
B1.pack(ipadx=20,ipady=20)


GUI.mainloop
