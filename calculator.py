import tkinter as tk
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
import math

main=tk.Tk()
main.title('Calculator')
main.geometry("400x170+300+200")
main.iconbitmap('calculator.ico')

#+++++++++++++++++++++++++++++++++++                INPUT              +++++++++++++++++++++++++++++++++++
value=tk.Variable()
box = tix.Entry(main,textvariable=value,borderwidth=10,width=41,font='arial 20 bold')
box.pack(anchor="n",fill=tk.X)


#+++++++++++++++++++++++++++++++++++          INPUT END                ++++++++++++++++++++++++++++++++++++

#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{             FUNCTIONALITY             }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

def func_one(event=None):
    if value.get()==0:
        box.delete(0,tk.END)
        box.insert(-1,'1')
    else:
        box.insert(tk.END,'1')


def func_two(event=None):
    if value.get()==0:
        box.delete(0,tk.END)
        box.insert(-1,'2')
    else:
        box.insert(tk.END,'2')


def func_three(event=None):
    if value.get()==0:
        box.delete(0,tk.END)
        box.insert(-1,'3')
    else:
        box.insert(tk.END,'3')


def func_four(event=None):
    if value.get()==0:
        box.delete(0,tk.END)
        box.insert(-1,'4')
    else:
        box.insert(tk.END,'4')


def func_five(event=None):
    if value.get()==0:
        box.delete(0,tk.END)
        box.insert(-1,'5')
    else:
        box.insert(tk.END,'5')


def func_six(event=None):
    if value.get()==0:
        box.delete(0,tk.END)
        box.insert(-1,'6')
    else:
        box.insert(tk.END,'6')


def func_seven(event=None):
    if value.get()==0:
        box.delete(0,tk.END)
        box.insert(-1,'7')
    else:
        box.insert(tk.END,'7')


def func_eight(event=None):
    if value.get()==0:
        box.delete(0,tk.END)
        box.insert(-1,'8')
    else:
        box.insert(tk.END,'8')


def func_nine(event=None):
    if value.get()==0:
        box.delete(0,tk.END)
        box.insert(-1,'9')
    else:
        box.insert(tk.END,'9')

def func_zero(event=None):
    if value.get()==0       :
        box.delete(0,tk.END)
        box.insert(-1,'0')
    else:
        box.insert(tk.END,'0')        

operators = ['/','*','-','+']

def func_plus(event=None):
    try:
        for i in operators:
            if i in value.get()[-1]:
                box_len = box.get()
                del_pos = len(box_len)-1
                box.delete(del_pos,tk.END)
                box.insert(tk.END,'+')
                return
    except IndexError:
        box.insert(tk.END,'0')
        box.delete(0,tk.END)
    else:
        box.insert(tk.END,'+')

def func_subtract():
    try:
        for i in operators:
            if i in value.get()[-1]:
                box_len = box.get()
                del_pos = len(box_len)-1
                box.delete(del_pos,tk.END)
                box.insert(tk.END,'-')
                return
    except IndexError:
        box.insert(tk.END,'-')
    else:
        box.insert(tk.END,"-")

def func_multiply():
    try:
        for i in operators:
            if i in value.get()[-1]:
                box_len = box.get()
                del_pos = len(box_len)-1
                box.delete(del_pos,tk.END)
                box.insert(tk.END,'*')
                return
    except IndexError:
        box.insert(tk.END,'9')
        box.delete(0,tk.END)
    else:
        box.insert(tk.END,"*")

def func_divide():
    try:
        for i in operators:
            if i in value.get()[-1]:
                box_len = box.get()
                del_pos = len(box_len)-1
                box.delete(del_pos,tk.END)
                box.insert(tk.END,'/')
                return
    except IndexError:
        box.insert(tk.END,'9')
        box.delete(0,tk.END)
    else:
        box.insert(tk.END,"/")


def func_clear(event=None):
    box.delete(0,tk.END)

def func_delete(event=None):
    box_len = box.get()
    del_pos = len(box_len)-1
    box.delete(del_pos,tk.END)


#   ================    EQUALS    FUNCTION    ===============
def func_equals(event=None):
    try:
        if value.get().isdigit():
            return
        else:
            final_val = eval(str(value.get()))
            value.set(final_val)
            box.delete(0,tk.END)
            box.insert(tk.END,final_val)
    except SyntaxError:
        messagebox.showerror('Invalid Input','You can not start the calculation with : / or * .\n                              OR                                 \n Maybe you didnot type anything.')
    except NameError:
        messagebox.showerror('Invalid Input', 'No operation can be performed with Alphabets or Special Symbols.')
        

    
    


#{{{{{{{{{{{{{{{{{{{{{{{{{   FUNCTIONALITY  END        }}}}}}}}}}}}}}}}}}}}}}}}}

#||||||||||||||||||||||||||||||||||||||            BUTTONS      |||||||||||||||||||||||||||
pos=tk.LabelFrame(main,bg="blue",height=200,borderwidth=10)
pos.pack(side=tk.BOTTOM,fill=tk.BOTH)


one = ttk.Button(pos,text='1',width=10,command=func_one)
two = ttk.Button(pos,text='2',width=10,command=func_two)
three = ttk.Button(pos,text='3',width=10,command=func_three)
four = ttk.Button(pos,text='4',width=10,command=func_four)
five = ttk.Button(pos,text='5',width=10,command=func_five)
six = ttk.Button(pos,text='6',width=10,command=func_six)
seven = ttk.Button(pos,text='7',width=10,command=func_seven)
eight = ttk.Button(pos,text='8',width=10,command=func_eight)
nine = ttk.Button(pos,text='9',width=10,command=func_nine)
zero = ttk.Button(pos,text='0',width=35,command=func_zero)

plus = ttk.Button(pos,text='+',width=10,command=func_plus)
minus = ttk.Button(pos,text='-',width=10,command=func_subtract)
multiply = ttk.Button(pos,text='x',width=10,command=func_multiply)
divide = ttk.Button(pos,text='/',width=10,command=func_divide)
equals = ttk.Button(pos,text='=',width=22,command=func_equals)
delete= ttk.Button(pos,text='<',width=10,command=func_delete)
clear= ttk.Button(pos,text='C',width=10,command=func_clear)


one.grid(row=0,column=0,padx=2)
two.grid(row=0,column=1,padx=2)
three.grid(row=0,column=2,padx=2)
four.grid(row=1,column=0,padx=2)
five.grid(row=1,column=1,padx=2)
six.grid(row=1,column=2,padx=2)
seven.grid(row=2,column=0,padx=2)
eight.grid(row=2,column=1,padx=2)
nine.grid(row=2,column=2,padx=2)
zero.grid(row=3,column=0,padx=2,columnspan=3)

plus.grid(row=0,column=4,padx=2)
minus.grid(row=0,column=5,padx=2)
multiply.grid(row=1,column=4,padx=2)
divide.grid(row=1,column=5,padx=2)
delete.grid(row=2,column=4,padx=2)
clear.grid(row=2,column=5,padx=2)
equals.grid(row=3,column=4,padx=2,columnspan=2)

#|||||||||||||||||||||||||||||||||||    BUTTTONS END        |||||||||||||||||||||||||||||||

main.mainloop()