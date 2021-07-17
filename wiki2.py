import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

window=Tk()
window.title("Wikipedia")
window.geometry("500x500")

def search_wiki():
    search=entry.get()
    Hasil=wikipedia.summary(search)
    showinfo("information", Hasil)

label=Label(window,text="Search wikipedia")
label.grid(row=0,column=0)

entry=Entry(window)
entry.grid(row=0,column=1)
button=Button(window,text="Search",command=search_wiki)
button.grid(row=1,column=1,padx=10)

window.mainloop()