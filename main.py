from tkinter import *
import math

root = Tk()
root.resizable(width=False, height=False)
root.title('PyCalculate')

result = StringVar()
result.set('0')

frame = Frame(root)
frame.pack()

title = Label(frame, textvariable=result, font=40, width=20, height=2, anchor='w')
title.grid(row=0, column=0, columnspan=4)

def addNum(num):
    current = result.get()
    if current == '0':
        result.set(str(num))
    else:
        result.set(current + str(num))

def calculate(op):
    current = result.get()
    result.set(current + op)

def clear():
    result.set('0')
    
def equal():
    expression = result.get().replace('^', '**')
    result.set(str(eval(expression)))

def sqrt():
    current = float(result.get())
    result.set(str(math.sqrt(current)))


# Num buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('^', 4, 2), ('/', 4, 3),
]
for (text, row, col) in buttons:
    if text.isdigit() or text == '.':
        action = lambda x=text: addNum(x)
    else:
        action = lambda x=text: calculate(x)
    Button(frame, text=text, width=7, height=3, command=action).grid(row=row, column=col)

# Other buttons
Button(frame, text='C', width=7, height=3, command=clear).grid(row=5, column=0)
Button(frame, text='√', width=7, height=3, command=sqrt).grid(row=5, column=1)
Button(frame, text='=', width=16, height=3, command=equal).grid(row=5, column=2, columnspan=2)

root.mainloop()