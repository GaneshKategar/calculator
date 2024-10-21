from tkinter import *
from tkinter import ttk
import tkinter as tk

root=Tk()


#global variables
num=''
num2=''
sym=''


def calc(): 

    global num
    global num2
    global sym
    
    try:
        num = int(num)
        num2 = int(num2)
   
    except:
        res.configure(text='Enter Values')

    if sym == '+':
        print("Result: ",num+num2)
        result=num+num2
        res.configure(text=result)
        
    elif sym == '-':
        print("Result: ",num - num2)
        result=num-num2
        res.configure(text=result)

    elif sym == '*':
        print("Result: ",num * num2)
        result=num*num2
        res.configure(text=result)

    elif sym == "/":
        print("Result: ",num / num2)
        result=num/num2
        res.configure(text=result)
        
    else:
        print("Enter A valid Symbol")
        #    print(num,"\n",num2)


    num=''
    num2=''
    sym=''
        

    


def no0():
    global num
    global num2

    num = str(num)
    num2 = str(num2)


    if sym=='':
        num += '0'
        print(num)
        txt.configure(text=num)
    else:
        # num2 = num2*10
        num2 += '0'
        print("num 2: ",num2)
        txt2.configure(text=num2)


def no1():
    
    global num
    global num2

    num = str(num)
    num2 = str(num2)
    
    if sym=='':
        num += '1'
        print("num 1: ",num)
        txt.configure(text=num)
        return num
        
    else:
        num2 += '1'
        print("num 2: ",num2)
        txt2.configure(text=num2)
        return num2


def no2():
    
    global num
    global num2

    num = str(num)
    num2 = str(num2)

    if sym=='':
        num += '2'
        print("num 1: ",num)
        txt.configure(text=num)
        return num
    else:
        num2 += '2'
        print("num 2: ",num2)
        txt2.configure(text=num2)
        return num2

def no3():
    
    global num
    global num2

    num = str(num)
    num2 = str(num2)

    if sym=='':
        num += '3'
        print("num 1: ",num)
        txt.configure(text=num)
        return num
    else:
        num2 += '3'
        print("num 2: ",num2)
        txt2.configure(text=num2)
        return num2

def no4():
    
    global num
    global num2

    num = str(num)
    num2 = str(num2)

    if sym=='':
        num += '4'
        print("num 1: ",num)
        txt.configure(text=num)
        return num
    else:
        num2 += '4'
        print("num 1: ",num2)
        txt2.configure(text=num2)
        return num2

def no5():
    
    global num
    global num2

    num = str(num)
    num2 = str(num2)
    
    if sym=='':
        num += '5'
        print("num 1: ",num)
        txt.configure(text=num)
        return num
    else:
        num2 += '5'
        print("num 2: ",num2)
        txt2.configure(text=num2)
        return num2

def no6():
    
    global num
    global num2

    num = str(num)
    num2 = str(num2)

    if sym=='':
        num += '6'
        print("num 1: ",num)
        txt.configure(text=num)
        return num
    else:
        num2 += '6'
        print("num 2: ",num2)
        txt2.configure(text=num2)
        return num2
    

def no7():
    
    global num
    global num2

    num = str(num)
    num2 = str(num2)
    
    if sym=='':
        num += '7'
        print("num 1: ",num)
        txt.configure(text=num)
        return num
    else:
        num2 += '7'
        print("num 2: ",num2)
        txt2.configure(text=num2)
        return num2

def no8():
    
    global num
    global num2

    num = str(num)
    num2 = str(num2)
    
    if sym=='':
        num += '8'
        print("num 1: ",num)
        txt.configure(text=num)
        return num
    else:
        num2 += '8'
        print("num 2: ",num2)
        txt2.configure(text=num2)
        return num2

def no9():
    
    global num
    global num2

    num = str(num)
    num2 = str(num2)
    
    if sym=='':
        num += '9'
        print("num 1: ",num)
        txt.configure(text=num)
        return num
    else:
        num2 += '9'
        print("num 2: ",num2)
        txt2.configure(text=num2)
        return num2


def plus():
    global sym
    sym='+'
    print("Symbol :",sym)
    symtxt.configure(text='+')

def sub():
    global sym
    sym = '-'
    print("Symbol :",sym)
    symtxt.configure(text='-')


def mul():
    global sym
    sym = '*'
    print("Symbol :",sym)
    symtxt.configure(text='*')

def div():
    global sym
    sym = '/'
    print("Symbol :",sym)
    symtxt.configure(text='/')
    
def clr():

    global num,num2,sym

    del(num,num2)


    num = ''
    num2 = ''
    sym = ''
    txt.configure(text='')
    txt2.configure(text='')
    symtxt.configure(text=' ')
    res.configure(text='')
    
    print(num)
    print(num2)


def back():

    global num,num2,sym

    if num2!=0:
        del(num2)
        num2=''
        print("num2 ",num2)
        txt.configure(text=num)
    elif num!=0:
        del(num)
        num=''
        sym=''
        print("num ",num)
        txt2.configure(text=num2)
    else:
        print(num," ",num2)


root.title("CALCULATOR")

root.geometry('700x250')

frame = ttk.Frame(root,padding=10)
frame.grid()








btn = ttk.Button(frame,text='Calculate',command=calc)
btn0 = ttk.Button(frame,text='0',command=no0,width=20)
btn1 = ttk.Button(frame,text='1',command=no1,width=20)
btn2 = ttk.Button(frame,text='2',command=no2,width=20)
btn3 = ttk.Button(frame,text='3',command=no3,width=20)
btn4 = ttk.Button(frame,text='4',command=no4,width=20)
btn5 = ttk.Button(frame,text='5',command=no5,width=20)
btn6 = ttk.Button(frame,text='6',command=no6,width=20)
btn7 = ttk.Button(frame,text='7',command=no7,width=20)
btn8 = ttk.Button(frame,text='8',command=no8,width=20)
btn9 = ttk.Button(frame,text='9',command=no9,width=20)
btnplus = ttk.Button(frame,text='+',command=plus,width=20)
btnsub = ttk.Button(frame,text='-',command=sub,width=20)
btnmul = ttk.Button(frame,text='*',command=mul,width=20)
btndiv = ttk.Button(frame,text='/',command=div,width=20)
btnclr = ttk.Button(frame,text='C',command=clr,width=20)
btnback = ttk.Button(frame,text='<',command=back,width=20)




txt = ttk.Label(frame,textvariable='')
txt2 = ttk.Label(frame,textvariable='')
txt3 = ttk.Label(frame,textvariable='')
symtxt = ttk.Label(frame,textvariable='')
res = ttk.Label(frame,textvariable='')


#ordering the grid


res.grid(column=4,row=7,ipadx=20,ipady=15)
txt.grid(column=1,row=7,ipadx=20,ipady=15)
txt2.grid(column=3,row=7,ipadx=20,ipady=15)
symtxt.grid(column=2,row=7,ipadx=20,ipady=15)
btn.grid(column=5,row=7)







btn0.grid(column=3,row=8,ipadx=10,ipady=9)
btn1.grid(column=1,row=9,ipadx=10,ipady=9)
btn2.grid(column=2,row=9,ipadx=10,ipady=9)
btn3.grid(column=3,row=9,ipadx=10,ipady=9)
btn4.grid(column=1,row=10,ipadx=10,ipady=9)
btn5.grid(column=2,row=10,ipadx=10,ipady=9)
btn6.grid(column=3,row=10,ipadx=10,ipady=9)
btn7.grid(column=1,row=11,ipadx=10,ipady=9)
btn8.grid(column=2,row=11,ipadx=10,ipady=9)
btn9.grid(column=3,row=11,ipadx=10,ipady=9)
btnplus.grid(column=4,row=8,ipadx=10,ipady=9)
btnsub.grid(column=4,row=9,ipadx=10,ipady=9)
btnmul.grid(column=4,row=10,ipadx=10,ipady=9)
btndiv.grid(column=4,row=11,ipadx=10,ipady=9)
btnclr.grid(column=2,row=8,ipadx=10,ipady=9)
btnback.grid(column=1,row=8,ipadx=10,ipady=9)


root.mainloop()



def main():
    root=Tk()
    root.title("CALCULATOR")

    root.geometry('700x250')

    frame = ttk.Frame(root,padding=10)
    frame.grid()


if __name__=='__main__':

    main()
