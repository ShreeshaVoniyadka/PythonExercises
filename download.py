from tkinter import *
from pytube import YouTube
root=Tk()

root.geometry('500x500')

root.resizable(0,0)

root.title('u tube downloader ')

Label(root,text="download video",font=("calibri",15,"italic bold")).pack()

link=Stringval()
Label(root,text="paste the link here",font =("calibri",15,"italic bold")).place(x=160,y=60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()