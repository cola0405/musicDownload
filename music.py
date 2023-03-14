import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
def m_folder(name):
    isExists = os.path.exists(name)
    if not isExists:
        os.mkdir(name)
def get_music(url):
    print(url)
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'lxml')
    js=soup.find_all('script')[1].text
    song_name_index=js.index('title')+8
    song_end=js.index('            author')-4
    song_name=js[song_name_index:song_end]
    author_index=js.index('author')+8
    author_end=js.index('            url')-4
    author=js[author_index:author_end]
    url_index=js.index('url:')+6
    url_end=js.index('            pic')-4
    song_url='https://www.hifini.com/'+js[url_index:url_end]
    res=requests.get(song_url,headers=headers)
    fd=open('song/'+song_name+'-'+author+'.mp3','ab')
    fd.write(res.content)
    fd.close()
    tkinter.messagebox.showinfo('提示', '下载成功')


def window_init(w):
    w.title("音乐爬虫")
    w.geometry("200x100")
    t1 = tk.StringVar()
    t1.set('')
    URL_text = tk.Entry(w, textvariable=t1)
    URL_text.pack(side='left')
    b=ttk.Button(w, text="下载", width=7, command=lambda :get_music(URL_text.get()))
    b.pack(side='right')

if __name__=='__main__':
    m_folder('song')
    window = tk.Tk()
    window_init(window)
    window.mainloop()

