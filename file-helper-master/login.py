from tkinter import *
from tkinter import messagebox
import os
import pymysql
# import Tank






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

        sql = "SELECT username FROM tank_user where username='"+username +"' and password='"+password+"'"
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
        os.system("python Tank.py")
        root.destroy()
    else:
        messagebox.showerror("登录", "用户名或者密码错误.")

# Create a Tkinter window
root = Tk()
root.title("登录")
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



