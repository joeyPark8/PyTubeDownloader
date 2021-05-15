import pytube
import tkinter
from tkinter import filedialog

def download():
    global entry_url, entry_path, btn_toggle
    
    url = entry_url.get()
    path = entry_path.get()

    if btn_toggle['text'] == 'video':
        pytube.YouTube(url).streams.get_highest_resolution().download(path)
    else:
        pytube.YouTube(url).streams.get_audio_only().download(path)

def openDirectory():
    global entry_path
    
    dir = filedialog.askdirectory()
    print(dir)
    entry_path.insert(0, dir)

def toggleButton():
    global btn_toggle

    if btn_toggle['text'] == 'video':
        btn_toggle.configure(text='audio')
    else:
        btn_toggle.configure(text='video')

#윈도우 설정
window = tkinter.Tk()
window.title('Youtube downloader')
window.geometry('640x480+100+100')
window.resizable(False, False)

#위젯
lbl_title = tkinter.Label(window, text='Youtube Downloader')
lbl_title.place(x=200, y=0)

lbl_url = tkinter.Label(window, text='video url: ')
lbl_url.place(x=200, y=30)
entry_url = tkinter.Entry(window)
entry_url.place(x=300, y=30)

lbl_path = tkinter.Label(window, text='download path: ')
lbl_path.place(x=200, y=70)
entry_path = tkinter.Entry(window)
entry_path.place(x=300, y=70)
btn_dir = tkinter.Button(window, text='path', command=openDirectory)
btn_dir.place(x=430, y=70)

btn_down = tkinter.Button(window, text='download', command=download)
btn_down.place(x=300, y=110)

btn_toggle = tkinter.Button(window, text='video', command=toggleButton)
btn_toggle.place(x=250, y=160)

#루프
window.mainloop()

