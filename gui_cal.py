import tkinter as tk


caluculation=""

def add_to_caluculation(symbol):
    global caluculation
    caluculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,caluculation)

def evaluate():
    global caluculation
    try:
        caluculation=str(eval(caluculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,caluculation)
    except:
        text_result.insert(1.0,"Error")
        clear()

def clear():
    global caluculation
    caluculation=""
    text_result.delete(1.0,"end")


root =tk.Tk()
root.geometry("350x350")
text_result=tk.Text(root,height=1,width=16,font=("arial",24))
text_result.grid(columnspan=5)
btn1=tk.Button(root,text="1",command=lambda:add_to_caluculation(1),width=4,font=("arial",24))
btn1.grid(row=2,column=1)
btn2=tk.Button(root,text="2",command=lambda:add_to_caluculation(2),width=4,font=("arial",24))
btn2.grid(row=2,column=2)
btn3=tk.Button(root,text="3",command=lambda:add_to_caluculation(3),width=4,font=("arial",24))
btn3.grid(row=2,column=3)

btn4=tk.Button(root,text="4",command=lambda:add_to_caluculation(4),width=4,font=("arial",24))
btn4.grid(row=3,column=1)
btn5=tk.Button(root,text="5",command=lambda:add_to_caluculation(5),width=4,font=("arial",24))
btn5.grid(row=3,column=2)
btn6=tk.Button(root,text="6",command=lambda:add_to_caluculation(6),width=4,font=("arial",24))
btn6.grid(row=3,column=3)

btn7=tk.Button(root,text="7",command=lambda:add_to_caluculation(7),width=4,font=("arial",24))
btn7.grid(row=4,column=1)
btn8=tk.Button(root,text="8",command=lambda:add_to_caluculation(8),width=4,font=("arial",24))
btn8.grid(row=4,column=2)
btn9=tk.Button(root,text="9",command=lambda:add_to_caluculation(9),width=4,font=("arial",24))
btn9.grid(row=4,column=3)
btn0=tk.Button(root,text="0",command=lambda:add_to_caluculation(0),width=4,font=("arial",24))
btn0.grid(row=5,column=2)


btnplus=tk.Button(root,text="+",command=lambda:add_to_caluculation("+"),width=4,font=("arial",24))
btnplus.grid(row=2,column=4)
btnminus=tk.Button(root,text="-",command=lambda:add_to_caluculation("-"),width=4,font=("arial",24))
btnminus.grid(row=3,column=4)
btnmulti=tk.Button(root,text="*",command=lambda:add_to_caluculation("*"),width=4,font=("arial",24))
btnmulti.grid(row=4,column=4)
btndivide=tk.Button(root,text="/",command=lambda:add_to_caluculation("/"),width=4,font=("arial",24))
btndivide.grid(row=5,column=4)
btnclose=tk.Button(root,text=")",command=lambda:add_to_caluculation("("),width=4,font=("arial",24))
btnclose.grid(row=5,column=3)
btnopen=tk.Button(root,text="(",command=lambda:add_to_caluculation(")"),width=4,font=("arial",24))
btnopen.grid(row=5,column=1)
btnequal=tk.Button(root,text="=",command=evaluate,width=8,font=("Arial",24))
btnequal.grid(row=6,column=3,columnspan=2)
btnclear=tk.Button(root,text="C",command=clear,width=8,font=("Arial",24))
btnclear.grid(row=6,column=1,columnspan=2)




root.mainloop()



