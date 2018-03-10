from tkinter import *
import random
import time

root = Tk()

root.title("Calculator")

text_Input = StringVar()
operator = ""

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""


"""  Calculator  """
txtDisplay = Entry(font=('arial', 20, 'bold'), textvariable=text_Input, bd=10, insertwidth=2,
                   bg="rosy brown", justify="right")
txtDisplay.grid(columnspan=4)

# Buttons
btn7 = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
              text="7", bg="rosy brown", command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
              text="8", bg="rosy brown", command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
              text="9", bg="rosy brown", command=lambda: btnClick(9)).grid(row=2, column=2)

Addition = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
                  text="+", bg="rosy brown", command=lambda: btnClick("+")).grid(row=2, column=3)

btn4 = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
              text="4", bg="rosy brown", command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
              text="5", bg="rosy brown", command=lambda: btnClick(5)).grid(row=3, column=1)
btn6 = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
              text="6", bg="rosy brown", command=lambda: btnClick(6)).grid(row=3, column=2)

Subtraction = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
                     text="-", bg="rosy brown", command=lambda: btnClick("-")).grid(row=3, column=3)

btn1 = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
              text="1", bg="rosy brown", command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
              text="2", bg="rosy brown", command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
              text="3", bg="rosy brown", command=lambda: btnClick(3)).grid(row=4, column=2)

Multiplication = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
                        text="x", bg="rosy brown", command=lambda: btnClick("*")).grid(row=4, column=3)

btn0 = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
              text="0", bg="rosy brown", command=lambda: btnClick(0)).grid(row=5, column=0)
btnClear = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
                  text="C", bg="rosy brown", command=btnClearDisplay).grid(row=5, column=1)
btnEquals = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
                   text="=", bg="rosy brown", command=btnEqualsInput).grid(row=5, column=2)

Division = Button(padx=16, bd=4, fg="black", font=('arial', 20, 'bold'),
                  text="/", bg="rosy brown", command=lambda: btnClick("/")).grid(row=5, column=3)

root.mainloop()
