import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pytube
import time


root = tk.Tk()
root.title("Youtube Downloader")
root.iconbitmap("stis.ico")
root.geometry("700x500")
root.maxsize(700,450)
root.minsize(700,500)



#Program
def download():
        link = text.get("1.0","end-1c")

        if link == '':
                messagebox.showerror("YouTube Downloader", "Paste Link Yotube Disini") 
        else:
                yt = pytube.YouTube(link)
                stream = yt.streams.first()
                time.sleep(2)
                text.delete(1.0,'end') 
                text.insert('end','Wait Downloading ......')
                time.sleep(5)
                stream.download('C:/Users/GMP/Downloads')
                messagebox.showinfo("YouTube Downloader",'Video telah berhasil didownload')


#Background Image
background_1 = Image.open('white.jpg')
background_2 = background_1.resize((700, 500), Image.ANTIALIAS)
background_3 = ImageTk.PhotoImage(background_2)
background_final = tk.Label(root, image=background_3)
background_final.place(relwidth=1, relheight=1)

# header label
header = Label(root,width="300",height="2")
header.place(x=0,y=0)

#youtube logo image
yt_logo = ImageTk.PhotoImage(Image.open('youtube.png'))
logo = Label(root, image = yt_logo,borderwidth=0)
logo.place(x=10,y=10)

#caption label
caption = Label(root,text="YouTube Downloader",font=('verdana',10,'bold'))
caption.place(x=50,y=10)

#logo Download
logo_1 = Image.open('stis.png')
logo_2 = logo_1.resize((128, 128), Image.ANTIALIAS)
logo_3 = ImageTk.PhotoImage(logo_2)
logo_final = Label(root, image = logo_3)
logo_final.place(x=300,y=110)


#Input Text
text = Text(root,width=60,height=2,font=('verdana',10,'bold'))
text.place(x=100,y=242) 
text.insert('end','Paste link video disini')

#Tombol Downlaods
button = Button(root,text="Download",relief=RIDGE,font=('verdana',10,'bold'),bg="#4C98FF",fg="white",command=download)
button.place(x=330,y=300)

root.mainloop()


