#!/usr/bin/env python
# coding:cp936
# Author: Simon Lau 
# Created: 2013-8-5
# Power By Python

import MySQLdb,configparser
from pip.backwardcompat import raw_input


# ��ȡ�����ļ�
config = configparser.ConfigParser()
config.read(r"D:\mysql.ini")
s_ip = config.get("server", "ip")
s_name = config.get("server", "name")
s_passwd = config.get("server", "passwd")
s_db = config.get("server", "db")

# ������
conn = MySQLdb.connect(host = s_ip, user = s_name, passwd = s_passwd, db = s_db)

# ѭ������,����������ȷ
while True :
    try :
        cursor = conn.cursor()
        print("#" * 15 + " Mysql DB " + "#" * 15)
        cursor.execute("SHOW TABLES")

        # ��ʾ���е����ݱ�����
        for tn in cursor.fetchall() :
            # ��ʽ�����,����ĸ��д
            print("{0:-<39}".format(str(tn).split("'")[1]).capitalize() + "#")

        # ����һ������
        tabname = raw_input("Please input table name : ")
        sqlone = "SELECT DISTINCT t1 FROM " + tabname
        cursor.execute(sqlone)

        # ͳ�ƿ�ʼ
        print("#" * 16 + " Result " + "#" * 16)
        for row in cursor.fetchall() :
            key = "SELECT COUNT(*) t1 FROM " + tabname + " WHERE t1="
            sql = key + "\"" + str(row).split("'")[1] + "\""
            cursor.execute(sql)
            for s in cursor.fetchall() :
                print("{0:-<37}{1:0}".format(str(row).split("'")[1], s[0]))
        print("#" * 17 + " End " + "#" * 17)
        break
    except :
        print("�������,����������!")
        continue