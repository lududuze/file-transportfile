import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from UI_main import Ui_MainWindow,MyMainWindow
from UI_option import Ui_OptionWindow
from UI_file import Ui_FileWindow
from net_server import Server
from net_client import Client
from tkinter import *
from tkinter import messagebox
import os
import pymysql
# 文件传输器类
class TransPorter:
    # 构造函数
    def __init__(self):
        self.__mainWindow = MyMainWindow(self)          # main窗口
        self.__main_ui = Ui_MainWindow(self)            # main窗口ui对象

        self.__optionWindow = QMainWindow()             # option窗口
        self.__option_ui = Ui_OptionWindow(self)        # option窗口ui对象

        self.__fileWindow = QMainWindow()               # file窗口
        self.__file_ui = Ui_FileWindow(self)            # file窗口ui

        self.__server = Server()                        # 服务器对象
        self.__client = Client(self)
        self.__mode = None                              # 工作模式（服务器True/客户端False）
        self.__working = False                          # 正在工作标志
        self.__download = False                         # 上传还是下载

        self.__main_ui.setupUi(self.__mainWindow)       # 在main窗口建立ui
        self.__option_ui.setupUi(self.__optionWindow)   # 在option窗口建立ui
        self.__file_ui.setupUi(self.__fileWindow)       # 在file窗口建立ui

    # 启动传输器
    def Activate(self):
        self.__mainWindow.show() 

    # 作为服务器运行
    def RunAsServer(self,boolean):
        self.__mode = boolean
    
    # 获取工作模式
    def IsServer(self):
        return self.__mode

    # 设置工作状态
    def SetWroking(self,boolean):
        self.__working = boolean

    # 在工作吗
    def IsWorking(self):
        return self.__working

    # 设置任务状态
    def SetDownloadTask(self,boolean):
        self.__download = boolean

    # 是下载文件吗
    def IsDownloadTask(self):
        return self.__download

    # 获取option窗口UI对象
    def GetOptionUI(self):
        return self.__option_ui

    # 获取file窗口UI对象
    def GetFileUI(self):
        return self.__file_ui

    # 获取Mian窗口UI对象
    def GetMainUI(self):
        return self.__main_ui

    # 获取Mian窗口对象
    def GetMainWindow(self):
        return self.__mainWindow
    
    # 获取file窗口对象
    def GetFileWindow(self):
        return self.__fileWindow

    # 获取option窗口对象
    def GetOptionWindow(self):
        return self.__optionWindow

    # 获取服务器对象
    def GetServer(self):
        return self.__server
    
    # 获取客户端对象
    def GetClient(self):
        return self.__client


# import Tank








# Create a Tkinter window
root = Tk()
root.title("文件传输登录")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 280
height = 150
# window_size = '%dx%d+%d+%d' % (width, height, (screen_width-width)/2, (screen_height-height)/2)
window_size = f'{width}x{height}+{round((screen_width-width)/2)}+{round((screen_height-height)/2)}' #round去掉小数
root.geometry(window_size)

# Add username label and entry
username_label = Label(root, text="用户名:")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Add password label and entry
password_label = Label(root, text="密码:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)
def login():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='root',
                         database='user1',
                         charset='utf8mb4',  # mysql字符格式
                         cursorclass=pymysql.cursors.DictCursor)
    username = username_entry.get()
    password = password_entry.get()

    try:
        cursor = db.cursor();

        sql = "SELECT username FROM user1 where username='"+username +"' and password='"+password+"'"
        print(sql)
        cursor.execute(sql)

        results = cursor.fetchall()
        count_num = 0
        for r in results:
            count_num += 1
        print(count_num)

    except pymysql.Error as err:
        print(err)

    finally:
        cursor.close()
        db.close()

    if count_num > 0:
        # messagebox.showinfo("登录", "登录成功")
        # os.system("python Tank.py")
        # root.destroy()
        root.destroy()
        app = QApplication(sys.argv)  # 创建应用程序对象
        postman = TransPorter()
        postman.Activate()  # 显示主窗口
        sys.exit(app.exec_())

    else:
        messagebox.showerror("登录", "用户名或者密码错误.")
# Add login button
login_button = Button(root, text="登录", command=login)
login_button.grid(row=2, column=1, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:39:15 2022
@author: zhuchunqiang
"""





#
# if __name__ == '__main__':

