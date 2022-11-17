#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname='mydb' user='me' host='localhost' password='secret'")
cur = conn.cursor()

login_user = input("Entrez votre login : ")
sql = "SELECT login FROM Adherents, Personnel WHERE login=%s" %login_user
cur.execute(sql)

//login faux : 
while(sql='NULL')
    print( "le login n'est pas bon")
    login_user = input("Entrez votre login : ")
    sql = "SELECT login FROM Adherents, Personnel WHERE login=%s" %login_user
    cur.execute(sql)



sql2="SELECT login FROM Adherents WHERE login=%s" %login_user
cur.execute(sql2)
    if sql2='NULL'
        sql2 = "SELECT login FROM Personnel WHERE login=%s" %login_user
        cur.execute(sql2)
        /*MENU Personnel
    else 
        /* menu adhérents



sql = "SELECT login FROM Adherents WHERE login=%s" %login_user
cur.execute(sql)
    if sql='NULL'
        sql2 = "SELECT login FROM Personnel WHERE login=%s" %login_user
        if sql2=NULL
            login_user = input("Le login donné n'existe pas dans la base de données, entrez votre login : ")





conn.commit()

conn.close()
