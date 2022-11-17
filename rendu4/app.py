#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname='mydb' user='me' host='localhost' password='secret'")
cur = conn.cursor()

login_user = input("Entrez votre login : ")
sql = "SELECT login FROM Adherents, Personnel WHERE login=%s" %login_user
cur.execute(sql)
row = cur.fetchone()

#login faux : 
while(!row) :
    print( "le login n'est pas bon")
    login_user = input("Entrez votre login : ")
    sql = "SELECT login FROM Adherents, Personnel WHERE login=%s" %login_user
    cur.execute(sql)
    row = cur.fetchone()


#on cherche si c''est un adhérent ou un personnel
sql2="SELECT login FROM Adherents WHERE login=%s" %login_user
cur.execute(sql2)
row = cur.fetchone()
if (!row) :
    choix = -1
    while(choix!=0) :
        choix = int(input(" Que voulez-vous faire : \n 1. Gestion des ressources \n 2. Gestion des adhérents \n 3. Gestion des Emprunts, Reservations et Sanctions\n 0. Sortir"))
        #menu des actions sur les ressources
        if (choix == 1) :
            choix_2 = int(input(" Que voulez-vous faire : \n 1. Ajouter une ressource \n 2. Modifier une ressource \n 3. Supprimer une ressource\n 4. Ajouter un exemplaire d'une ressource \n 5. Modifier un exemplaire"))




            #ajouter une ressource
            if (choix_2==1) :
                


        #menu des actions sur les adhérents
            elif (choix == 2) :
            choix_2 = int(input(" Que voulez-vous faire : \n 1. Ajouter un adhérent \n 2. Modifier les informations personnelles d'un adhérent \n 3. Modifier l'adhésion d'un adhérent \n 4. Accéder aux informations d'un adhérent \n 5. Afficher la liste des adhérents"))
        #menu des actions sur emprunts, réservation et sanction
        elif (choix == 3) :
            choix_2 = int(input(" Que voulez-vous faire : \n 1. Ajouter un emprunt \n 2. Modifier (retour, et autres modifications) un emprunt \n 3. Ajouter une réservation \n 4. Modifier une réservation \n 5. Afficher la liste des emprunts en cours \n 6. Sanctionner "))
            if choix_2 == 1: 
                duré = input("Entrez la date limite de l'emprunt sous la forme YYYY-MM-DD : ")
                login = input("Entrez le login de la personne qui emprunte la ressource : ")
                cle = input("Entrez la clé de l'exemplaire : ")
                encours = True 
                sql_empr = "INSERT INTO EMPRUNT VALUES (%s, %s,%b, %s)" % (cle , login, encours, duré)
                cur.execute(sql_empr)
                sql00 = "UPDATE Exemplaire SET Disponibilité =%b WHERE Clé='%s'" % (False, cle)
                cur.execute(sql00)
                sql = "SELECT compteur FROM Exemplaire WHERE Clé='%s'" % (clé)
                cur.execute(sql)
                row = cur.fetchone()
                row=row+1
                sql01 = "UPDATE Exemplaire SET compteur =%s WHERE Clé='%s'" % (row, cle)
                cur.execute(sql01)
                conn.commit()
            elif choix_2 == 2: 
                date_retour = input("Entrez la date du retour de l'emprunt sous la forme YYYY-MM-DD : ")
                login = input("Entrez le login de la personne qui emprunte la ressource : ")
                cle = input("Entrez la clé de l'exemplaire : ")
                sql = "SELECT Durée_limite FROM EMPRUNT WHERE login='%s' AND Clé='%s'" % (login,clé)
                cur.execute(sql)
                row = cur.fetchone()
                sanction=0
                for i in range(4):
                    if row[i] < date_retour[i]:
                        sanction=1
                if row[6] < date_retour[6]:
                        sanction=1
                elif row[7] < date_retour[7]:
                        sanction=1
                for i in range(8,10):
                    if row[i] < date_retour[i]:
                        sanction=1
                if sanction == 1:
                    sql_sanction = "INSERT INTO Sanction VALUES (%s, %s,%b,%b,%s, %b,%s)" % (cle , login, True,True, date_retour, False, None)
                    cur.execute(sql_sanction)
                    conn.commit()
            elif choix_2 == 3:
                cle = input("Entrez la clé de l'exemplaire : ")
            elif choix_2 == 4:
                cle = input("Entrez la clé de l'exemplaire : ")
            elif choix_2 == 5:
                sql = "SELECT Clé, login FROM EMPRUNT WHERE emprunt_enCours ='%b'" % True
                cur.execute(sql)
                raw = cur.fetchone()
                for i in range(len(raw)):
                    Cle = raw[i][0]
                    login = raw[i][1]
                    print ("Les emprunt en cours sont %s %s" % (Cle, login))
            elif choix_2 == 6:
                date_effective = input("Entrez la date du retour effective de la sanction sous la forme YYYY-MM-DD : ")
                login = input("Entrez le login de la personne qui sanctionner: ")
                cle = input("Entrez la clé de l'exemplaire : ")
                sanction=int(input("Entrez 1 si la sanction est une degradation et 0 si c'est un retard"))
                if sanction==0:
                    sql_sanction = "INSERT INTO Sanction VALUES (%s, %s,%b,%b,%s, %b,%s)" % (cle , login, True,False, None, True, date_effective)
                    cur.execute(sql_sanction)
                    conn.commit()
                elif sanction==1:
                    sql_sanction = "INSERT INTO Sanction VALUES (%s, %s,%b,%b,%s, %b,%s)" % (cle , login, True,True, date_effective, False, None)
                    cur.execute(sql_sanction)
                    conn.commit()
        
        else : 
            break
else :
    /* menu adhérents






conn.commit()

conn.close()
