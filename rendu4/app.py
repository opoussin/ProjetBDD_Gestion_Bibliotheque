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
        
        else : 
            break
else :
    /* menu adhérents






conn.commit()

conn.close()
