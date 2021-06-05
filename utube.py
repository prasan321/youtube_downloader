from tkinter import *
from pytube import YouTube

window = Tk()

window.geometry('500x300')

window.resizable(0,0)

window.title('Video Downloader App')

Label(window, text="YouTube Video Downloader", font=("arial", 20, "bold")).pack()

#link is used to store the youtue video link
link = StringVar()

Label(window, text="Paste the link here: ", font=("arial", 15, "bold")).place(x=160, y=60)

link_entered = Entry(window, width=70, textvariable=link).place(x=32, y=110)

#video downloading
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(window, text="Video is downloaded and save in the project's folder!!!", font=("arial", 15)).place(x=20, y=210)

#
Button(window, text="Download", font='arial 15 bold', bg='yellow', padx=2, command=downloader).place(x=180, y=150)

window.mainloop()