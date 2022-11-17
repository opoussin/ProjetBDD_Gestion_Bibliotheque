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
            choix_2 = int(input(" Que voulez-vous faire : \n 1. Ajouter une ressource \n  2. Ajouter un exemplaire d'une ressource \n 3. Modifier un exemplaire \n 4. Visualiser une ressource \n 5. Nombre d'exemplaire disponible d'une ressource"))

                #ajouter une ressource
                if (choix_2==1) :
                    Type=raw_input("Entrez le type de ressource : Film, Livre ou Oeuvremusicale ")
                    Code=raw_input("Entrez le code de la ressource : ")
                    Titre=raw_input("Entrez le titre de la ressource : ")
                    Éditeur= =raw_input("Entrez l'éditeur de la ressource : ")
                    Genre=raw_input("Entrez le genre de la ressource : ")
                    Date_appartion=int(input("Entrez l'année de date d'apparition de la ressource : "))
                    Nb_exemplaire=int(input("Entrez le nombre d'exemplaire de la ressource : "))

                    #on exprime différentes possibilités car la requête n'est pas la même en fonction du type ( livre, oeuvre, film)  de la ressource
                    if (Type=='Livre'):
                        ISBN=raw_input("Entrez l'ISBN du livre : ")
                        Langue_livre=raw_input("Entrez la langue du livre : ")
                        Résumé=raw_input("Entrez le résumé du livre : "),
                        sql_ajout_livre="INSERT INTO Ressource VALUES (%s,%s,%s,%s,%d,%d,%s,%s,%s,NULL,NULL,NULL,NULL,%s)" % (Code, Titre, Éditeur, Genre, Date_appartion, Nb_exemplaire,ISBN,Langue_livre,Résumé, Type)
                        cur.execute(sql_ajout_livre)
                        print("La ressource '%s' a bien été ajoutée") %Titre
                    elif(Type=='Film'):
                        Synopsis=raw_input("Entrez le synopsis du film : ")
                        Langue_film=raw_input("Entrez la langue du film : ")
                        Durée_film=raw_input("Entrez la durée du film sous le format HH:MM:SS : ")
                        sql_ajout_film="INSERT INTO Ressource VALUES (%s,%s,%s,%s,%d,%d,NULL,NULL,NULL,%s,%s,%s,NULL,%s)" % (Code, Titre, Éditeur, Genre, Date_appartion, Nb_exemplaire,Synopsis,Langue_film,Durée_film, Type)
                        cur.execute(sql_ajout_film)
                        print("La ressource '%s' a bien été ajoutée") %Titre
                    elif(Type=='Oeuvremusicale'):
                        Durée_oeuvre=raw_input("Entrez la durée de l'oeuvre sous le format HH:MM:SS : ")
                        sql_ajout_OM="INSERT INTO Ressource VALUES (%s,%s,%s,%s,%d,%d,NULL,NULL,NULL,NULL,NULL,NULL,%s,%s)" % (Code, Titre, Éditeur, Genre, Date_appartion, Nb_exemplaire,Durée_oeuvre, Type)
                        cur.execute(sql_ajout_OM)
                        print("La ressource '%s' a bien été ajoutée") %Titre

                #ajout d'un exemplaire : ajout dans la table exemplaire et modification du nombre de 'exemplaire de la table ressource
                elif (choix_2==2):
                    Clé= raw_input("Entrez la clé de l'exemplaire : ")
                    Code_E= raw_input("Entrez le code de la ressource : ")
                    sql_type="SELECT Type FROM Ressource WHERE Ressource.Code = %s" %Code_E
                    cur.execute(sql_type)
                    row = cur.fetchone()
                    État= raw_input("Entrez l'état de l'exemplaire : ")
                    sql_type="SELECT Type FROM Ressource WHERE Ressource.Code = %s" %Code_E
                    cur.execute(sql_type)
                    row = cur.fetchone()
                    sql_ajout_exemplaire="INSERT INTO Exemplaire VALUES (%s,%s,%s,%s,%b,%d)"%(Clé,row[0], Code_E, État, true,0)
                    sql_titre="SELECT Titre FROM Ressource WHERE Ressource.Code = %s" %Code_E
                    cur.execute(sql_titre)
                    row = cur.fetchone()
                    print("L'exemplaire %s de la ressource '%s' a bien été ajouté") %(Clé, row[0])
                    sql_recuperation_nbexemplaire="SELECT Nb_exemplaire FROM Ressource WHERE Ressource.Code = %s" %Code_E
                    cur.execute(sql_recuperation_nbexemplaire)
                    row = cur.fetchone()
                    sql_nb_exemplaire="UPDATE Ressource WHERE Code=%s SET Nb_exemplaire= %d +1" %(Code_E, row[0])
                    cur.execute(sql_nb_exemplaire)

                #modification d'un exemplaire : on ne veut pas changer le code de la ressource, donc le type non plus, et la clé non plus: juste l'état et la Disponibilité
                elif (choix_2==3):

                     #affichage des titres et de la clé de tous les exemplaires
                    sql_consult_exemplaire="SELECT Ressource.Titre, Exemplaire.Clé FROM Ressource INNER JOIN Exemplaire ON Ressource.Code=Exemplaire.Code"
                    cur.execute(sql_consult_exemplaire)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                        print("\n")

                    Clé= raw_input("Entrez la clé de l'exemplaire à modifier: ")
                    sql_lecture="SELECT * FROM Exemplaire WHERE Clé=%s" %Clé
                    cur.execute(sql_lecture)
                    row = cur.fetchone()
                    while(!row):
                        print("Cet exemplaire n'existe pas ")
                        Clé= raw_input("Entrez la clé de l'exemplaire à modifier: ")
                        sql_lecture="SELECT * FROM Exemplaire WHERE Clé=%s" %Clé
                        cur.execute(sql_lecture)
                        row = cur.fetchone()
                    print( "Type: %s, Code: %s, État: %s, Disponibilité: %b, compteur: %d \n" %(row[1],row[2],row[3],row[4],row[5]))
                    État= raw_input("Entrez le nouvel état de l'exemplaire : ")
                    disp=int(input("est-ce que l'exemplaire est encore disponible? 1 oui, 0 Non")
                        if(disp==1)
                            sql_nb_exemplaire="UPDATE Exemplaire WHERE Clé= %s SET État=%s, Disponibilité=%b" %(Clé,true)
                            cur.execute(sql_nb_exemplaire)
                        elif(disp==0)
                            sql_nb_exemplaire="UPDATE Exemplaire WHERE Clé= %s SET État=%s, Disponibilité=%b" %(Clé,false)
                            cur.execute(sql_nb_exemplaire)
                    print("L'exemplaire a été modifié")

                 elif (choix_2==4):
                    #affichage des titres de toutes les ressources
                    sql_consult="SELECT Titre FROM Ressource"
                    cur.execute(sql_consult)
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                        print("\n")
                    Titre= raw_input("Entrez le Titre de la ressource à consulter: ")
                    sql_lecture="SELECT * FROM Ressource WHERE Titre=%s" %Titre
                    cur.execute(sql_lecture)
                    row = cur.fetchone()

                    #test si la ressource existe, sinon on redemande 
                    while (!row)
                        print(" Cette ressource n'existe pas ")
                        Titre= raw_input("Entrez le Titre de la ressource à consulter: ")
                        sql_lecture="SELECT * FROM Ressource WHERE Titre=%s" %Titre
                        cur.execute(sql_lecture)
                        row = cur.fetchone()

                    if (row[13]=='Livre'):
                        print( "Titre: %s, Éditeur: %s, Genre: %s, Date_apparition: %d, Nb_exemplaire: %d, ISBN: %s, Langue_livre: %s, Résumé: %s  \n" %(row[1],row[2],row[3],row[4],row[5], row[6],row[7],row[8]))
                    elif (row[13]=='Film'):
                        print( "Titre: %s, Éditeur: %s, Genre: %s, Date_apparition: %d, Nb_exemplaire: %d,  Synopsis: %s, Langue_film: %s, Durée_film: %s  \n" %(row[1],row[2],row[3],row[4],row[5], row[9],row[10],row[11]))
                    else:
                        print( "Titre: %s, Éditeur: %s, Genre: %s, Date_apparition: %d, Nb_exemplaire: %d,  Durée_oeuvre:%s  \n" %(row[1],row[2],row[3],row[4],row[5], row[12]))
                
                elif(choix_2==5):
                    ressource_disp=raw_input("Titre de la ressource dont vous souhaitez vérifier la disponibilité")
                    sql_disponibilité = "SELECT COUNT(Exemplaire.Disponibilité) FROM Ressource INNER JOIN Exemplaire ON Ressource.Code=Exemplaire.Code WHERE (Ressource.Titre=%s AND Exemplaire.Disponibilité=%b  "%(ressource_disp,true)
                    cur.execute(sql_disponibilité)
                    row = cur.fetchone()
                    print(" La ressource '%s' est disponible en %d exemplaires " %(ressource_disp, row[0]))
                    
                


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
                login = input("Entrez le login de la personne qui réserve la ressource : ")
                date_effective = input("Entrez la date effective de la réservation sous la forme YYYY-MM-DD : ")
                sql01 = "UPDATE Exemplaire SET  Disponibilité =%b WHERE Clé='%s'" % (False, cle)
                cur.execute(sql01)
                conn.commit()
                Sql_reserv = "INSERT INTO Reservation VALUES (%s, %s,%b, %s)" % (cle , login, True, date_effective)
                cur.execute(Sql_reserv)
                conn.commit()

            elif choix_2 == 4:
                choix_3= int(input("Que voulez-vous faire 1. Ajouter une réservation 2. Modifié une réservation"))
                if choix_3 ==1 : 
                    cle = input("Entrez la clé de l'exemplaire : ")
                    login = input("Entrez le login de la personne qui réserve la ressource : ")
                    date_effective = input("Entrez la date effective de la réservation sous la forme YYYY-MM-DD : ")
                    sql01 = "UPDATE Reservation SET  reserv_date =%d WHERE Clé='%s' AND login='%s'" % ( date_effective, cle, login)
                    cur.execute(sql01)
                    conn.commit()
                elif choix_3 ==2 : 
                   choix_4=int(input("Que voulez-vous faire 1. Modifier la date de la réservation 2. Modifié le livre de la réservation))
                   if choix_4 ==1 :
                        login = input("Entrez le login de la personne qui réserve la ressource : ")
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
