import tkinter

from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("300x500")
window.config(padx=20, pady=20, bg="teal")

Label(window, text="Calculator", bg="black", fg="white",
      font=("Arial", 25)).pack(pady=0)

reslbl = Label(window, width=12, font=("Arial", 25), bg="white", fg="black")
reslbl.pack(pady=10)

frame = Frame(window, bg="Orange", width=200, height=300)
frame.pack(pady=20)

#req Functions


def get_digit(digit):
  current = reslbl['text']
  new = current + str(digit)
  reslbl.config(text=new)


def get_operator(op):
  global first_num, operator
  first_num = int(reslbl['text'])
  operator = op
  reslbl.config(text="")


def clear():
  reslbl.config(text="")


def get_result():
  global first_num,second_number,operator
  second_number = int(reslbl['text'])
  if operator == "+":
    reslbl.config(text=first_num + second_number)
  elif operator == "-":
    reslbl.config(text=first_num - second_number)
  elif operator == "*":
    reslbl.config(text=first_num * second_number)
  elif operator == "/":
    reslbl.config(text=first_num / second_number)
  else:
    if second_number ==0:
      reslbl.config(text='Error')
    else:
      reslbl.config(text=str(first_num / second_number))



#row 1 frame
btn7 = Button(frame,
              text="7",
              font=("Arial", 20),
              bg="white",
              fg="black",
              width=2,
              height=1,
              command=lambda: get_digit(7))
btn7.grid(row=0, column=0)

btn8 = Button(frame,
              text="8",
              font=("Arial", 20),
              bg="white",
              fg="black",
              width=2,
              height=1,
              command=lambda: get_digit(8))
btn8.grid(row=0, column=1)

btn9 = Button(frame,
              text="9",
              font=("Arial", 20),
              bg="white",
              fg="black",
              width=2,
              height=1,
              command=lambda: get_digit(9))
btn9.grid(row=0, column=2)

btnplus = Button(frame,
                 text="+",
                 font=("Arial", 20),
                 bg="white",
                 fg="black",
                 width=2,
                 height=1,
                 command=lambda: get_operator("+"))
btnplus.grid(row=0, column=3)

#row 2 frame
btn4 = Button(frame,
              text="4",
              font=("Arial", 20),
              bg="white",
              fg="black",
              width=2,
              height=1,
              command=lambda: get_digit(4))
btn4.grid(row=1, column=0)

btn5 = Button(frame,
              text="5",
              font=("Arial", 20),
              bg="white",
              fg="black",
              width=2,
              height=1,
              command=lambda: get_digit(5))
btn5.grid(row=1, column=1)

btn6 = Button(frame,
              text="6",
              font=("Arial", 20),
              bg="white",
              fg="black",
              width=2,
              height=1,
              command=lambda: get_digit(6))
btn6.grid(row=1, column=2)

btnminus = Button(frame,text="-",font=("Arial", 20),bg="white",fg="black",width=2,height=1,command=lambda: get_operator("-"))
btnminus.grid(row=1, column=3)

#row 3 frame
btn1 = Button(frame,text="1",font=("Arial", 20),bg="white",fg="black",width=2,height=1,command=lambda: get_digit(1))
btn1.grid(row=2, column=0)

btn2 = Button(frame,text="2",font=("Arial", 20),bg="white",fg="black",width=2,height=1,command=lambda: get_digit(2))
btn2.grid(row=2, column=1)

btn3 = Button(frame,text="3",font=("Arial", 20),bg="white",fg="black",width=2,height=1,command=lambda: get_digit(3))
btn3.grid(row=2, column=2)

btnmul = Button(frame,text="x",font=("Arial", 20),bg="white",fg="black",width=2,height=1,command=lambda: get_operator("*"))
btnmul.grid(row=2, column=3)

#row 4 frame
btnAC = Button(frame,
               text="AC",
               font=("Arial", 20),
               bg="white",
               fg="black",
               width=2,
               height=1,
               command=lambda: clear())
btnAC.grid(row=3, column=0)

btn0 = Button(frame,
              text="0",
              font=("Arial", 20),
              bg="white",
              fg="black",
              width=2,
              height=1,
              command=lambda: get_digit(0))
btn0.grid(row=3, column=1)

btneq = Button(frame,
               text="=",
               font=("Arial", 20),
               bg="white",
               fg="black",
               width=2,
               height=1,
               command=lambda:get_result())
btneq.grid(row=3, column=2)

btndiv = Button(frame,
                text="/",
                font=("Arial", 20),
                bg="white",
                fg="black",
                width=2,
                height=1,
                command=lambda: get_operator("/"))
btndiv.grid(row=3, column=3)

window.mainloop()
