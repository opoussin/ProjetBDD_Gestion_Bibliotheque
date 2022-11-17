#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname='mydb' user='me' host='localhost' password='secret'")
cur = conn.cursor()

login_user = input("Entrez votre login : ")
sql = "SELECT login FROM Adherents, Personnel WHERE login=%s" %login_user
cur.execute(sql)
row = cur.fetchone()

#login faux : 
while(!row)
    print( "le login n'est pas bon")
    login_user = input("Entrez votre login : ")
    sql = "SELECT login FROM Adherents, Personnel WHERE login=%s" %login_user
    cur.execute(sql)
    row = cur.fetchone()


#on cherche si c''est un adhérent ou un personnel
sql2="SELECT login FROM Adherents WHERE login=%s" %login_user
cur.execute(sql2)
row = cur.fetchone()
    if (!row)
        /*MENU Personnel
    else 
        /* menu adhérents






conn.commit()

conn.close()
