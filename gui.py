# import socket
# from bs4 import BeautifulSoup
# import time
# import re
# import json
# from requests.adapters import HTTPAdapter
# import execjs
from tkinter import ttk
from tkinter import *
import threading
from tkinter.filedialog import *
import sys
from bin2txt import *
import os

# from tkinter import simpledialog

'''
软件名: BIN_2_TXT
版本: 1.0
更新时间: 2021.06.18
打包命令: pyinstaller -F -w gui.py
'''

# 实例化TK
root = Tk()

# 主窗口配置
root.wm_title("BIN_2_TXT V 1.0")
root["bg"] = "white"
root.wm_geometry('{}x{}'.format(600, 150))
root.wm_attributes("-alpha", 0.95)
root.resizable(width=False, height=False)
# root.maxsize(width=960, height=640)
# root.minsize(width=600, height=400)
# root.iconbitmap("./icon.ico")

frame_top1 = Frame(root, height=100, width=600, relief="sunken")
frame_top1.pack(padx=10,  # 外间距x
                pady=10,  # 外间距y
                # ipadx=10,  # 内间距x
                # ipady=10  # 内间距y
                )
frame_top2 = Frame(root, height=100, width=600, relief="sunken")
frame_top2.pack(padx=10,  # 外间距x
                pady=10,  # 外间距y
                # ipadx=10,  # 内间距x
                # ipady=10  # 内间距y
                )


# 多线程
def thread_it(func, *args):
    """ 多线程 """
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)
    t.start()
    # t.join()


def select_path():
    """选择保存目录"""
    folder = askdirectory()
    entry_rf_name.delete(0, END)
    entry_rf_name.insert(0, folder)

    if not folder:
        # print('目录错误!!!', 'error')
        sys.exit()

    with open('config.ini', 'w', encoding="UTF-8") as f:
        f.write(folder)


def select_file():
    """选择保存目录"""
    # 选择文件目录
    rf_path = askopenfilename(filetypes=[('Hex files', '*.*')])
    entry_rf_name.delete(0, END)
    entry_rf_name.insert(0, rf_path)

    if not rf_path:
        # print('目录错误!!!', 'error')
        sys.exit()

    # 保存txt文件路径
    wf_path = os.path.dirname(entry_rf_name.get()) + '/' +\
              os.path.splitext(os.path.basename(entry_rf_name.get()))[0] + ".h"

    entry_wf_name.delete(0, END)
    entry_wf_name.insert(0, wf_path)

    with open('config.ini', 'w', encoding="UTF-8") as f:
        f.write(rf_path + "\r")
        f.write(wf_path)


# 创建输入框
entry_rf_name = Entry(frame_top1, width=60, relief='groove')
entry_rf_name.pack(side="left",
                       padx=10,  # 外间距x
                       pady=10,  # 外间距y
                       )
bottom_folder = Button(frame_top1, text='选择文件',
                       command=lambda: thread_it(select_file, ), width=10, height=1, relief='groove')
bottom_folder.pack(
    padx=10,  # 外间距x
    pady=10,  # 外间距y
)
entry_wf_name = Entry(frame_top2, width=60)
entry_wf_name.pack(side="left",
                   padx=10,  # 外间距x
                   pady=10,  # 外间距y
                   )
bottom_parse = Button(frame_top2, text='开始转换',
                      command=lambda: thread_it(exec, ),
                      width=10, height=1, relief='groove')
bottom_parse.pack(
    padx=10,  # 外间距x
    pady=10,  # 外间距y
)

# 读取配置
if os.path.exists('config.ini'):
    with open('config.ini', encoding="UTF-8") as rd:
        entry_rf_name.insert(0, rd.readline())
        entry_wf_name.insert(1, rd.readline())


def WriteLog(file, text):
    """ 写文件功能函数 """
    # 在当前路径下，以写的方式打开一个名为'*.txt'，如果不存在则创建
    with open(file, 'w+', encoding='utf-8') as f:
        # 将text里的数据写入到文本中
        f.write(text)
        # 清空字符串
    f.close()


def exec():
    if not entry_rf_name.get():
        sys.exit()

    if not entry_wf_name.get():
        sys.exit()
    bin2txt(entry_rf_name.get().replace("\r", "").replace("\n", ""), entry_wf_name.get())
    print("finish.")


root.mainloop()
