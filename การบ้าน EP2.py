import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title("เกมเป่ายิงฉุบ")
GUI.geometry('500x400')

L1 = Label(GUI,text='เกมเป่ายิงฉุบ' ,font=('Angsana New',30),fg='green')
L1.pack()

# ฟังชั้นใช้ในการเลือกออกคำตอบ
def choice_selected(choice):
    print(f"คุณเลือก {choice}.")
    computer_choice = random.choice(["ค้อน", "กระดาษ", "กรรไกร"])
    print(f"บอทเลือก {computer_choice}.")
    
    # สร้างเงื่อนไขการแพ้ชนะ
    if choice == computer_choice:
        result = "เสมอ!"
    elif (choice == "ค้อน" and computer_choice == "กรรไกร")or (choice == "กระดาษ" and computer_choice == "ค้อน")or (choice == "กรรไกร" and computer_choice == "กระดาษ"):
        result = "คุณชนะ!"
    else:
        result = "คุณแพ้!"
        
    # โชว์การแพ้ชนะ
    messagebox.showinfo("Result", result)

FB1 = Frame(GUI)
FB1.place(x=200,y=200)

rock_button = ttk.Button(GUI, text="ค้อน", command=lambda: choice_selected("ค้อน"))
rock_button.pack(ipadx=20,ipady=20)

paper_button = ttk.Button(GUI, text="กระดาษ", command=lambda: choice_selected("กระดาษ"))
paper_button.pack(ipadx=20,ipady=20)

scissors_button = ttk.Button(GUI, text="กรรไกร", command=lambda: choice_selected("กรรไกร"))
scissors_button.pack(ipadx=20,ipady=20)



GUI.mainloop()
