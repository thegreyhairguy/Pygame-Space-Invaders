from tkinter import *


window = Tk()

window.geometry("500x500")
window.title("Denomination Calclator")
window.config(bg="#96031A")
window.resizable(False,False)

#functions--------------------------

def newWindow():
  window2 = Tk()
  window2.title("Denomination Calculator")
  window2.geometry("500x300")
  window2.config(bg="#FAA916")


  Label(window2, text="Enter the amount", bg="#FAA916").place(x=50, y=50)
  entmain = Entry(window2)
  entmain.place(x=180, y=50)

  lb1 = Label(window2, text="2000", bg="#FAA916")
  lb1.place(x=80, y=100)
  ent1= Entry(window2)
  ent1.place(x=180, y=100)

  lb2 = Label(window2,text="500", bg="#FAA916").place(x=80, y=150)
  ent2= Entry(window2)
  ent2.place(x=180, y=150)

  lb3 = Label(window2,text="100", bg="#FAA916").place(x=80, y=200)
  ent3= Entry(window2)
  ent3.place(x=180, y=200)
  
  def calculate():
    global amount
    amount = int(entmain.get())
    note2000 = amount//2000
    amount = amount%2000
    note500 = amount//500
    amount = amount%500
    note100 = amount//100

    ent1.insert(END,"2000 x "+str(note2000))
    ent2.insert(END,"500 x "+str(note500))
    ent3.insert(END,"100 x "+str(note100))

  def clear():
    entmain.delete(0,END)
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)



  btnCal = Button(window2, text="Calculate",border=0, command=calculate)
  btnCal.place(x=180, y=250)
  btnClear = Button(window2, text="Clear", border=0,command=clear)
  btnClear.place(x=280, y=250)


  window2.mainloop()







#design-----------------------
Label(window,text="Deomination Calculator",font=("Sans Serif",20,"bold"),bg="#FBFFFE",fg="#1B1B1E").pack(padx=20,pady=100)


Bt1 = Button(window,text="Open",font=("Sans Serif",20,"bold"),bg="#FBFFFE",border=0,command=newWindow)
Bt1.pack(pady=100)





window.mainloop()