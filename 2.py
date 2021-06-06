# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:51:16 2021

@author: user
"""

#0506作業2
#101_AI_林建名

import os
from prettytable import PrettyTable
import pymysql

def print_fun():
    print("(0) 離開程式\n"
          "(1) 顯示會員列表\n"
          "(2) 新增會員資料\n"
          "(3) 更新會員資料\n"
          "(4) 刪除會員資料")
    
def print_member():
    os.system('cls' if os.name == 'nt' else 'clear')
    cursor.execute("select * from `member`")
    datas = cursor.fetchall()
    table = PrettyTable(["編號", "姓名", "生日", "地址"], encoding='utf8')
    table.align = 'l'
    for data in datas:
        table.add_row([data[0], data[1] ,data[2] ,data[3]])
    print(table)

passwd = input("請輸入資料庫root密碼：")
port = int(input("請輸入資料庫的Port："))
os.system('cls' if os.name == 'nt' else 'clear')
connect = pymysql.connect(host = 'localhost',
                          user = "root",
                          passwd = passwd,
                          db = "python_ai",
                          charset = "utf8",
                          port = port)
cursor = connect.cursor()
while True:    
    print_fun()
    inp = input("指令：")
    try:
        if inp == '0':
            connect.close()
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        elif inp == '1':
            print_member()

        elif inp == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            param = {
                "a":input("請輸入會員姓名："),
                "b":input("請輸入會員生日："),
                "c":input("請輸入會員地址：")
                }
            cursor.execute("INSERT INTO `member`(`name`, `birthday`, `address`) VALUES(%(a)s, %(b)s, %(c)s)", param)
            connect.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif inp == '3':
            print_member()
            param = {
                "a":input("請選擇你要修改的資料編號："),
                "b":input("請輸入會員姓名："),
                "c":input("請輸入會員生日："),
                "d":input("請輸入會員地址：")
                }
            cursor.execute("UPDATE `member` SET `name`=%(b)s, `birthday`=%(c)s, `address`=%(d)s WHERE `id`=%(a)s", param)
            connect.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif inp == '4':
            print_member()
            inp = input("請選擇你要刪除的資料編號：")
            cursor.execute(f"DELETE FROM `member` WHERE `id`='{inp}'")
            connect.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        continue