import tkinter as tk
from math import *
from tkinter import messagebox as m_box
win=tk.Tk()
win.geometry('280x370+400+200')
win.config(bg='black')
win.title('Super Calculator')
win.resizable(False,False)
win.focus()

global main_display_var
main_display_var=tk.StringVar()

main_display=tk.Entry(win,width=20,font=('times new roman',25),
                      bg='gold',textvariable=main_display_var)
main_display.grid(row=0)
main_display.focus()
num_display=tk.Frame(win)
num_display.place(x=0,y=45)

def num(number):
    global var
    var = number
    main_display_var.set(main_display_var.get()+str(var))

def back():
    main_display_var.set(main_display_var.get()[0:len(main_display_var.get())-1])
    
def equal():
    try:
        equ=eval(main_display_var.get())
        main_display_var.set(equ)
    except ZeroDivisionError:
        m_box.showerror('Division error','unable to divide by zero')
    except:
        m_box.showinfo('Notification',"Wrong input")
        
sin_btn=tk.Button(num_display,text='sin',command=lambda *args : num('sin(*pi/180)'),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
sin_btn.grid(row=1,column=0)

cos_btn=tk.Button(num_display,text='cos',command=lambda *args : num('cos(*pi/180)'),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
cos_btn.grid(row=1,column=1)

tan_btn=tk.Button(num_display,text='tan',command=lambda *args : num('tan(*pi/180)'),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
tan_btn.grid(row=1,column=2)

pi_btn=tk.Button(num_display,text='\u03C0',command=lambda *args : num('pi'),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
pi_btn.grid(row=2,column=2)

sqrt_btn=tk.Button(num_display,text='sqrt',command=lambda *args : num('**0.5'),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
sqrt_btn.grid(row=2,column=1)

mod_btn=tk.Button(num_display,text='%',command=lambda *args : num('%'),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
mod_btn.grid(row=2,column=0)

back_btn=tk.Button(num_display,text='back',command=back,font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
back_btn.grid(row=2,column=3)

num1_btn=tk.Button(num_display,text='1',command=lambda *args : num(1),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
num1_btn.grid(row=3,column=0)

num2_btn=tk.Button(num_display,text='2',command=lambda *args : num(2),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
num2_btn.grid(row=3,column=1)

num3_btn=tk.Button(num_display,text='3',command=lambda *args : num(3),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
num3_btn.grid(row=3,column=2)

num4_btn=tk.Button(num_display,text='4',command=lambda *args : num(4),font=('times new roman',20)
                   ,bg='light green',fg='blue',width=4)
num4_btn.grid(row=4,column=0)

num5_btn=tk.Button(num_display,text='5',command=lambda *args : num(5),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
num5_btn.grid(row=4,column=1)

num6_btn=tk.Button(num_display,text='6',command=lambda *args : num(6),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
num6_btn.grid(row=4,column=2)

num7_btn=tk.Button(num_display,text='7',command=lambda *args : num(7),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
num7_btn.grid(row=5,column=0)

num8_btn=tk.Button(num_display,text='8',command=lambda *args : num(8),font=('times new roman',20)
                   ,bg='light green',fg='blue',width=4)
num8_btn.grid(row=5,column=1)

num9_btn=tk.Button(num_display,text='9',command=lambda *args : num(9),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
num9_btn.grid(row=5,column=2)

num0_btn=tk.Button(num_display,text='0',command=lambda *args : num(0),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
num0_btn.grid(row=6,column=1)

dot_btn=tk.Button(num_display,text='.',command=lambda *args : num('.'),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
dot_btn.grid(row=6,column=0)

add_btn=tk.Button(num_display,text='+',command=lambda *args : num('+'),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
add_btn.grid(row=6,column=3)

sub_btn=tk.Button(num_display,text='-',command=lambda *args : num('-'),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
sub_btn.grid(row=5,column=3)

mul_btn=tk.Button(num_display,text='*',command=lambda *args : num('*'),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
mul_btn.grid(row=3,column=3)

div_btn=tk.Button(num_display,text='/',command=lambda *args : num('/'),font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
div_btn.grid(row=4,column=3)

def clear():
    main_display_var.set('')
clear_btn=tk.Button(num_display,text='clr',command=clear,font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
clear_btn.grid(row=1,column=3)

eq_btn=tk.Button(num_display,text='=',command=equal,font=('times new roman',20),
                   bg='light green',fg='blue',width=4)
eq_btn.grid(row=6,column=2)

win.mainloop()
