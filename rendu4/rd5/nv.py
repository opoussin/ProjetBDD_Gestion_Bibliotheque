#!/usr/bin/python3

import psycopg2

conn=psycopg2.connect("dbname='dbnf18a054' user='nf18a054'host='tuxa.sme.utc' password='L6FRUpdm'")
cur=conn.cursor()

login_user = input("Entrez votre login : ")
sql = "SELECT login FROM Adherents WHERE login='%s' UNION SELECT login FROM Personnel WHERE login='%s'" %(login_user,login_user)
cur.execute(sql)
row = cur.fetchone()

#login faux :
while not row :
    print( "le login n'est pas bon")
    login_user = input("Entrez votre login : ")
    sql = "SELECT login FROM Adherents WHERE login='%s' UNION SELECT login FROM Personnel WHERE login='%s'" %(login_user,login_user)
    cur.execute(sql)
    row = cur.fetchone()


#on cherche si c'est un adhérent ou un personnel
sql2="SELECT login FROM Adherents WHERE login='%s'" %login_user
cur.execute(sql2)
row = cur.fetchone()
if (not row) :
    choix = -1
    while(choix!=0) :
        choix = int(input(" Que voulez-vous faire : \n 1. Gestion des ressources \n 2. Gestion des adhérents \n 3. Gestion des Emprunts, Reservations et Sanctions\n 0. Sortir\n"))
        #menu des actions sur les ressources
        if (choix == 1) :
            choix_2 = int(input(" Que voulez-vous faire : \n 1. Ajouter une ressource \n  2. Ajouter un exemplaire d'une ressource \n 3. Modifier un exemplaire \n 4. Visualiser une ressource \n 5. Nombre d'exemplaire disponible d'une ressource \n "))
            #ajouter une ressource
            if (choix_2==1) :
                Type=raw_input("Entrez le type de ressource : Film, Livre ou Oeuvremusicale ")
                Code=raw_input("Entrez le code de la ressource : ")
                Titre=raw_input("Entrez le titre de la ressource : ")
                Éditeur= raw_input("Entrez l'éditeur de la ressource : ")
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
                while not row :
                    print("Cet exemplaire n'existe pas ")
                    Clé= raw_input("Entrez la clé de l'exemplaire à modifier: ")
                    sql_lecture="SELECT * FROM Exemplaire WHERE Clé=%s" %Clé
                    cur.execute(sql_lecture)
                    row = cur.fetchone()
                print("Type: %s, Code: %s, État: %s, Disponibilité: %b, compteur: %d \n " %(row[1],row[2],row[3],row[4],row[5]))
                État= raw_input("Entrez le nouvel état de l'exemplaire : ")
                disp=int(input("est-ce que l'exemplaire est encore disponible? 1 oui, 0 Non"))
                if(disp==1) :
                        sql_nb_exemplaire="UPDATE Exemplaire WHERE Clé= %s SET État=%s, Disponibilité=%b" %(Clé,true)
                        cur.execute(sql_nb_exemplaire)
                elif(disp==0) :
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
                while not row :
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
            if (choix_2==1) :
                login=input("Entrez le login de l'adhérent : ")
                Nom=input("Entrez le nom de l'adhérent : ")
                Prenom=input("Entrez le prénom de l'adhérent : ")
                Adresse= input("Entrez l'adresse de l'adhérent : ")
                Mail=input("Entrez son mail : ")
                Num_tele=input("Entrez le nombre de téléphone : ")
                Date_naissance=input("Entrez la date de naissance de l'adhérent : ")
                Nb_retard =int(input("Entrez le nombre de retard pour retourner une ressource : "))
                Nb_degradation =int(input("Entrez le nombre de dégradation de la ressource : "))
                Num_carte =input("Entrez le numéro de la carte : ")
                sql_ajout_adherent="INSERT INTO Adherents VALUES (%s,%s,%s,%s,%s,%s,%s,%d,%d,%s)" % (login, Nom, Prenom, Adresse, Mail, Num_tele,Date_naissance,Nb_retard,Nb_dagradation, Num_carte)
                cur.execute(sql_ajout_adherent)
                print("L'adérent '%s''%s' a bien été ajouté") %(Nom,Prenom)

            elif (choix_2==2) :
                login2 = input("Entrez le login de l'adhérent : ")
                #vérifier si l'adhérent est déjà dans la liste des adhérents
                sql22="SELECT login FROM Adherents WHERE login='%s'" %login2
                cur.execute(sql22)
                row = cur.fetchone()
                while not row :
                    print( "le login n'est pas bon")
                    login_user = input("Entrez le login : ")
                    sql22 = "SELECT login FROM Adherents WHERE login='%s'" %(login2,login2)
                    cur.execute(sql22)
                    row = cur.fetchone()

                # menu des informations que le personnel pourrait modifier
                information=input("Veuillez choisir l'information que vous voulez modifier : 1.Nom 2.Prenom 3.Adresse 4.Mail 5.Numéro de téléphone 6.Date de naissance 7.nombre de retard 8.nombre de dégradation 9.Numéro de carte 0.quitter \n")

                while information != 0 : #modifier plusieurs informations d'un adhérent
                    if (information==1):
                        Nom_n=input("Entrez le nom : ")
                        sql_nom="UPDATE Adherents SET Nom = '%s' WHERE login = '%s' " % (Nom_n,login2)
                        cur.execute(sql_nom)
                        print("Le nom '%s' a bien été enregistré") %Nom_n
                    elif(information==2):
                        Prenom_n=input("Entrez le prenom : ")
                        sql_prenom="UPDATE Adherents SET Prenom = '%s' WHERE login = '%s' " % (Prenom_n,login2)
                        cur.execute(sql_prenom)
                        print("Le prénom '%s' a bien été enregistré") %Prenom_n
                    elif(information==3):
                        Adresse_n= input("Entrez l'adresse de l'adhérent : ")
                        sql_adr="UPDATE Adherents SET Adresse = '%s' WHERE login = '%s' " % (Adresse_n,login2)
                        cur.execute(sql_adr)
                        print("L'adresse '%s' a bien été enregistré") %Adresse_n

                    elif(information==4):
                        Mail=input("Entrez son mail : ")
                        sql_mail="UPDATE Adherents SET Adresse = '%s' WHERE login = '%s' " % (Mail_n,login2)
                        cur.execute(sql_mail)
                        print("Le mail '%s' a bien été enregistré") %Mail_n

                    elif(information==5):
                        Num_tele_n=input("Entrez le nombre de téléphone : ")
                        sql_numtele="UPDATE Adherents SET Num_telephone = '%s' WHERE login = '%s' " % (Num_tele_n,login2)
                        cur.execute(sql_numtele)
                        print("Le numéro de téléphone '%s' a bien été enregistré") %Num_tele_n

                    elif(information==6):
                        Date_naissance_n=input("Entrez la date de naissance de l'adhérent : ")
                        sql_date="UPDATE Adherents SET Date_de_naissance = '%s' WHERE login = '%s' " % (Date_naissance_n,login2)
                        cur.execute(sql_date)
                        print("La date de naissance '%s' a bien été enregistré") %Date_naissance_n

                    elif(information==7):
                        Nb_retard_n =int(input("Entrez le nombre de retard pour retourner une ressource : "))
                        sql_retard="UPDATE Adherents SET Nb_retard = '%s' WHERE login = '%s' " % (Nb_retard_n,login2)
                        cur.execute(sql_retard)
                        print("Le nombre de retard '%s' a bien été enregistré") %Nb_retard_n

                    elif(information==8):
                        Nb_degradation_n =int(input("Entrez le nombre de dégradation de la ressource : "))
                        sql_degradation="UPDATE Adherents SET Nb_degradation = '%s' WHERE login = '%s' " % (Nb_degradation_n,login2)
                        cur.execute(sql_degradation)
                        print("Le nombre de degradation '%s' a bien été enregistré") %Nb_degradation_n

                    elif(information==9):
                        Num_carte_n =input("Entrez le numéro de la carte : ")
                        sql_carte="UPDATE Adherents SET Adresse = '%s' WHERE login = '%s' " % (Num_carte_n,login2)
                        cur.execute(sql_carte)
                        print("Le numéro de la carte '%s' a bien été enregistré") %Num_carte_n


            elif (choix_2==3) :
                login_modif=input("Entrez le login de l'adhérent dont vous voulez modifier l'adhésion : ")
                date_fin=input("Entrez la nouvelle date de fin de l'adhésion : ")
                sql_adhesion="UPDATE Adhesions SET FIN = '%s' WHERE login = '%s' " % (date_fin,login_modif)
                cur.execute(sql_adhesion)
                print("L'adhésion de l'adhérent '%s' a bien été enregistrée") %login_modif


            elif (choix_2==4) :
                login_info=input("Entrez le login de l'adhérent dont vous voulez consulter les informations : ")
                sql_info= "SELECT Adherents.login,Adherents.Nom ,Adherents.Prenom ,Adherents.Adresse ,Adherents.Mail,Adherents.Num_telephone,Adherents.Date_de_naissance ,Adherents.Nb_retard ,Adherents.Nb_degradation,Adherents.carte,Adhesions.Debut,Adhesions.FIN, EMPRUNT.emprunt_enCours, Reservation.état_reservation, Sanction.En_sanction FROM (((Adherents INNER JOIN Adhesions ON Adherents.login= Adhesions.login)INNER JOIN EMPRUNT ON EMPRUNT.login=Adhesions.login)INNER JOIN Reservation ON Reservation.login=Adhesions.login)INNER JOIN Sanction ON Sanction.login=Adhesions.login" %login_info
                cur.execute(sql_info)
                raw = cur.fetchone()
                while(not raw):
                    login_info=input("Mauvais login, Entrez le login de l'adhérent dont vous voulez consulter les informations : ")
                    sql_info= "SELECT Adherents.login,Adherents.Nom ,Adherents.Prenom ,Adherents.Adresse ,Adherents.Mail,Adherents.Num_telephone,Adherents.Date_de_naissance ,Adherents.Nb_retard ,Adherents.Nb_degradation,Adherents.carte,Adhesions.Debut,Adhesions.FIN, EMPRUNT.emprunt_enCours, Reservation.état_reservation, Sanction.En_sanction FROM (((Adherents INNER JOIN Adhesions ON Adherents.login= Adhesions.login)INNER JOIN EMPRUNT ON EMPRUNT.login=Adhesions.login)INNER JOIN Reservation ON Reservation.login=Adhesions.login)INNER JOIN Sanction ON Sanction.login=Adhesions.login" %login_info
                    cur.execute(sql_info)
                    raw = cur.fetchone()
                print("login : %s \n Nom : %s \n Prenom : %s \n Adresse: : %s \n Mail: %s \n Numéro de telephone:  %s \n Date de naissance: %s \n Nombre de retard: %d \n Nombre de degradation: %d \n carte: %s \n Debut d'adhésion: %s \nFin d'adhésions: % \n Emprunt en Cours: %b \n reservation en cours: %b \n En sanction: %b \n") % (raw[0],raw[1],raw[2], raw[3],raw[4],raw[5],raw[6],raw[7],raw[8],raw[9],raw[10],raw[11],raw[12],raw[13],raw[14])

            elif (choix_2==5) :
                sql="SELECT * FROM Adherents"
                cur.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    print(row)
                    print("\n")





        #menu des actions sur emprunts, réservation et sanction
        elif (choix == 3) :
            choix_2 = int(input(" Que voulez-vous faire : \n 1. Ajouter un emprunt \n 2. Modifier (retour, et autres modifications) un emprunt \n 3. Ajouter une réservation \n 4. Modifier une réservation \n 5. Afficher la liste des emprunts en cours \n 6. Sanctionner "))
            if choix_2 == 1:
                duré = input("Entrez la date limite de l'emprunt sous la forme YYYY-MM-DD : ")
                login = input("Entrez le login de la personne qui emprunte la ressource : ")
                cle = input("Entrez la clé de l'exemplaire : ")
                encours = True
                sql_empr = "INSERT INTO EMPRUNT VALUES (%s, %s,%b, %s)" % (cle , login, True, duré)
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
                choix_3= int(input("Que voulez-vous faire 1. Modifier la date de la réservation 2. Modifié la ressource de la réservation"))
                if choix_3 ==1 :
                    cle = input("Entrez la clé de l'exemplaire : ")
                    login = input("Entrez le login de la personne qui réserve la ressource : ")
                    date_effective = input("Entrez la nouvelle date effective de la réservation sous la forme YYYY-MM-DD : ")
                    sql01 = "UPDATE Reservation SET  reserv_date =%s WHERE Clé='%s' AND login='%s'" % ( date_effective, cle, login)
                    cur.execute(sql01)
                    conn.commit()
                elif choix_3 ==2 :
                    cle = input("Entrez la l'ancienne clé de l'exemplaire : ")
                    cle2 = input("Entrez la nouvelle clé de l'exemplaire : ")
                    login = input("Entrez le login de la personne qui réserve la ressource : ")
                    sql01 = "UPDATE Reservation SET  Clé =%s WHERE Clé='%s' AND login='%s'" % ( cle2, cle, login)
                    cur.execute(sql01)
                    conn.commit()
                    sql01 = "UPDATE Exemplaire SET Disponibilité =%b WHERE Clé='%s'" % (True, cle)
                    cur.execute(sql01)
                    conn.commit()
            elif choix_2 == 5:
                sql = "SELECT Clé, login FROM EMPRUNT WHERE emprunt_enCours ='%b'" %(True)
                cur.execute(sql)
                raw = cur.fetchone()
                for i in range(len(raw)):
                    Cle = raw[i][0]
                    login = raw[i][1]
                    print("Les emprunt en cours sont %s %s" % (Cle, login))
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
#Vérifier d'abord si l'adhérent est en sanction
    sql3="SELECT S.En_sanction FROM Sanction S JOIN Adherents A ON S.login = A.login WHERE S.login='%s'" %login_user
    cur.execute(sql3)
    row3 = cur.fetchone()
    if (row3 == "TRUE") :
        print("Désolé, vous êtes en sanction\n")
    #Si l'adhérent n'est pas en sanction : entrer dans le menu adhérents
    else :
        #menu adhérents
        choix = -1
        while choix!=0 :
            choix = int(input(" Que voulez-vous faire : \n 1.Consulter votre l'historique d'emprunt\n 2.Voir notre recommandation selon vos intérêts\n 3.rechercher un exemplaire \n 0. Sortir\n"))
            if (choix == 1) :
                sql5="SELECT * FROM Emprunt E Join Adherents A ON E.login = A.login WHERE E.login='%s'" %login_user
                cur.execute(sql5)
                row5 = cur.fetchone()
                print("Votre historique est : \n")
                print(row5)
                print("\n")
            elif (choix == 2) :
                sql_a="SELECT Clé FROM Emprunt E Join Adherents A ON E.login = A.login WHERE E.login='%s'" %login_user
                cur.execute(sql_a)
                row5 = cur.fetchall()
                for i in row5:
                    sql0="SELECT Code FROM Exemplaire WHERE Clé='%s'" %i
                    cur.execute(sql0)
                    row1 = cur.fetchone()
                sql_a="SELECT Genre FROM Ressource R Join Exemplaire E ON R.Code = '%s' GROUP BY Genre" %row1[0]
                cur.execute(sql_a)
                row4 = cur.fetchone()
                print("Nous vous recomandon les ressourses suivantes: \n")
                sqlaff="SELECT Titre FROM Ressource WHERE Type='%s'" %row4
                cur.execute(sqlaff)
                row7 = cur.fetchone()
                print(row7)
            elif (choix == 3) :
                type_recherche=int(input("quel type de recherche voulez-vous faire ? \n 1. par titre \n 2. par Type (Livre, Film , Oeuvremusicale ) \n 3. par genre ?"))
                if type_recherche == 1:
                    titre = input("Entrez la titre de la resource voulu : ")
                    sql = "SELECT Code FROM Ressource WHERE Titre ='%s'" %(titre)
                    cur.execute(sql)
                    raw = cur.fetchone()
                    sql_aff = "SELECT Disponibilité FROM Exemplaire WHERE code ='%s'" %(raw[0])
                    cur.execute(sql_aff)
                    raw1 = cur.fetchone()
                    if raw1[0] == False :
                        print("La resource n'est pas disponible \n")
                    elif raw1[0] == True :
                        print("La resource est disponible \n")
                elif type_recherche ==2:
                    type = input("Entrez le type de la resource voulu : \n")
                    sql = "SELECT * FROM Ressource WHERE Type ='%s'" %(type)
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Les ressource corespondant à %s sont \n" %(type))
                    print(raw)
                elif type_recherche ==3:
                    genre = input("Entrez le genre de la resource voulu : \n")
                    sql = "SELECT * FROM Ressource WHERE Genre ='%s'" %(genre)
                    cur.execute(sql)
                    raw = cur.fetchone()
                    print("Les ressource corespondant à %s sont \n" %(genre))
                    print(raw)
                    print("\n")

conn.commit()
conn.close()
