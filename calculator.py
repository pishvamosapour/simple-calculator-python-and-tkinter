#import modules ==================================================================

from tkinter import *

#create window ===================================================================

win = Tk()
win.title('calculator')
win.resizable(0 , 0)
e = Entry(win, borderwidth=5, width=35)

#functions =======================================================================

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))
def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)    

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


#crate items =====================================================================


btn1 = Button(win, text='1', padx=40, pady=20, command=lambda:button_click(1))
btn2 = Button(win, text='2', padx=40, pady=20, command=lambda:button_click(2))
btn3 = Button(win, text='3', padx=40, pady=20, command=lambda:button_click(3))

btn4 = Button(win, text='4', padx=40, pady=20, command=lambda:button_click(4))
btn5 = Button(win, text='5', padx=40, pady=20, command=lambda:button_click(5))
btn6 = Button(win, text='6', padx=40, pady=20, command=lambda:button_click(6))

btn7 = Button(win, text='7', padx=40, pady=20, command=lambda:button_click(7))
btn8 = Button(win, text='8', padx=40, pady=20, command=lambda:button_click(8))
btn9 = Button(win, text='9', padx=40, pady=20, command=lambda:button_click(9))

btn0 = Button(win, text='0', padx=39, pady=20, command=lambda:button_click(0))

    
btn_clear = Button(win, text='clear', padx=79, pady=20, command=button_clear)
btn_add = Button(win, text='+', padx=38, pady=20, command=button_add)
btn_equal = Button(win, text='=', padx=87, pady=20, command=button_equal)

btn_subtract = Button(win, text="-", padx=40, pady=20, command=button_subtract)
btn_multiply = Button(win, text="*", padx=41, pady=20, command=button_multiply)
btn_divide = Button(win, text="/", padx=41, pady=20, command=button_divide)

#grid items =======================================================================

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)

btn0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1, columnspan=2)

btn_add.grid(row=5, column=0)   
btn_equal.grid(row=5, column=1, columnspan=2)


btn_subtract.grid(row=6, column=0)
btn_multiply.grid(row=6, column=1)
btn_divide.grid(row=6, column=2)
#win mainloop ======================================================================
win.mainloop()

#===============================================================================================
