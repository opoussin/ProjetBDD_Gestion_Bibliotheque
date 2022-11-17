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
                    Type=raw_input("Entrez le type de ressource : Film, Livre ou Oeuvremusicale ")
                    Code=raw_input("Entrez le code de la ressource : ")
                    Titre=raw_input("Entrez le titre de la ressource : ")
                    Éditeur= =raw_input("Entrez l'éditeur de la ressource : ")
                    Genre=raw_input("Entrez le genre de la ressource : ")
                    Date_appartion=raw_input("Entrez la date d'apparition de la ressource : ")
                    Nb_exemplaire=int(input("Entrez le nombre d'exemplaire de la ressource : "))
                    if (Type=='Livre'):
                        ISBN=raw_input("Entrez l'ISBN du livre : ")
                        Langue_livre=raw_input("Entrez la langue du livre : ")
                        Résumé=raw_input("Entrez le résumé du livre : "),
                    elif(Type=='Film'):
                        Synopsis=raw_input("Entrez le synopsis du film : ")
                        Langue_film=raw_input("Entrez la langue du film : ")
                        Durée_film=raw_input("Entrez la durée du film sous le format HH:MM:SS : ")
                    elif(Type=='Oeuvremusicale'):
                        Durée_oeuvre=raw_input("Entrez la durée dde l'oeuvre sous le format HH:MM:SS : ")
                
                    
                    
                    


            #menu des actions sur les adhérents
             if (choix == 2) :
                choix_2 = int(input(" Que voulez-vous faire : \n 1. Ajouter un adhérent \n 2. Modifier les informations personnelles d'un adhérent \n 3. Modifier l'adhésion d'un adhérent \n 4. Accéder aux informations d'un adhérent \n 5. Afficher la liste des adhérents"))
            #menu des actions sur emprunts, réservation et sanction
            if (choix == 3) :
                choix_2 = int(input(" Que voulez-vous faire : \n 1. Ajouter un emprunt \n 2. Modifier (retour, et autres modifications) un emprunt \n 3. Ajouter une réservation \n 4. Modifier une réservation \n 5. Afficher la liste des emprunts en cours \n 6. Sanctionner "))
    else :
        /* menu adhérents






conn.commit()

conn.close()

