# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:51:16 2021

@author: user
"""

#0507作業1
#101_AI_林建名

import os
from prettytable import PrettyTable
import pymysql

def print_fun():
    print("(0) 離開程式\n"
          "(1) 顯示會員列表\n"
          "(2) 新增會員資料\n"
          "(3) 更新會員資料\n"
          "(4) 刪除會員資料\n"
          "(5) 新增會員的電話\n"
          "(6) 刪除會員的電話")
    
def print_member():
    os.system('cls' if os.name == 'nt' else 'clear')
    connect = pymysql.connect(host = 'localhost',
                              user = "root",
                              passwd = passwd,
                              db = "python_ai",
                              charset = "utf8",
                              port = port)
    cursor = connect.cursor()
    cursor.execute("select m.*, t.tel from `member` m left join `tel` t on m.id=t.member_id")
    all_datas = cursor.fetchall()
    table = PrettyTable(["編號", "姓名", "生日", "地址", "電話"], encoding='utf8')
    table.align = 'l'
    
    temp = ["" for i in range(4)]
    for data in all_datas:
        if data[0] == temp[0]:
            table.add_row(["", "", "", "", data[4]])
        else:
            temp = data 
            table.add_row(temp)
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
        
        elif inp == '5':
            print_member()
            param = {
                "a":input("請選擇要添加電話的會員編號："),
                "b":input("請輸入電話：")
                }
            cursor.execute("insert into `tel`(`member_id`, `tel`) values(%(a)s, %(b)s)", param)
            connect.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
        
        elif inp == '6':
            print_member()
            inp = input("請選擇要刪除電話的會員編號：")
            cursor.execute(f"select id, tel from tel where member_id={inp}")
            datas = cursor.fetchall()
            table = PrettyTable(["編號", "電話"], encoding='utf8')
            table.align = 'l'
            for data in datas:
                table.add_row([data[0], data[1]])
            print(table)
            inp = input("請輸入要刪除的電話編號：")
            cursor.execute(f"delete from tel where id={inp}")
            connect.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
                    
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        continue