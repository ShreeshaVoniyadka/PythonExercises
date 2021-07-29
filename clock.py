import tkinter as tk
from time import strftime
window=tk.Tk()
window.title('Time is Precious')
window.resizable(0,0)

def time():
    string=strftime('%H:%M:%S %p')
    clockTime.config(text=string)
    clockTime.after(1000,time)
clockTime = tk.Label(window, font = ('calibri', 40, 'bold'), background = 'black', foreground = 'white')

clockTime.pack(anchor = 'center')
time() 
window.mainloop()