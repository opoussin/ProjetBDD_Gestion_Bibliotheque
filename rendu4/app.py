#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname='mydb' user='me' host='localhost' password='secret'")
cur = conn.cursor()

login_user = input("Entrez votre login : ")

if login_user

sql = "SELECT login FROM Adherents" % (num, dpt, pop)
cur.execute(sql)
conn.commit()

conn.close()
