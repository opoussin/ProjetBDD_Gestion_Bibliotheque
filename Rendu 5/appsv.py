#!/usr/bin/python3

import psycopg2

conn=psycopg2.connect("dbname='dbnf18a054' user='nf18a054'host='tuxa.sme.utc' password='L6FRUpdm'")
cur=conn.cursor()

login_user = input("Entrez votre login : \n")
sql = "SELECT login FROM Adherents WHERE login='%s' UNION SELECT login FROM Personnel WHERE login='%s'" %(login_user,login_user)
cur.execute(sql)
row = cur.fetchone()

#login faux :
while not row :
    print("le login n'est pas bon \n")
    login_user = input("Entrez votre login : \n")
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
        choix = int(input(" Que voulez-vous faire : \n 1. Gestion des ressources \n 2. Gestion des adhérents \n 3. Gestion des Emprunts, Reservations et Sanctions\n 0. Sortir \n"))
        #menu des actions sur les ressources
        if (choix == 1) :
            choix_2 = int(input(" Que voulez-vous faire : \n 1. Ajouter une ressource \n  2. Ajouter un exemplaire d'une ressource \n 3. Modifier un exemplaire \n 4. Visualiser une ressource \n 5. Nombre d'exemplaire disponible d'une ressource \n"))
            #ajouter une ressource
            if (choix_2==1) :
                Type=input("Entrez le type de ressource : Film, Livre ou Oeuvremusicale \n")
                Code=input("Entrez le code de la ressource :\n")
                Titre=input("Entrez le titre de la ressource : \n")
                Genre=input("Entrez le genre de la ressource : \n")
                Date_appartion=int(input("Entrez l'année de date d'apparition de la ressource : \n"))
                Nb_exemplaire=int(input("Entrez le nombre d'exemplaire de la ressource : \n"))

                #on exprime différentes possibilités car la requête n'est pas la même en fonction du type ( livre, oeuvre, film)  de la ressource
                if (Type=='Livre'):
                    ISBN=input("Entrez l'ISBN du livre :\n")
                    Langue_livre=input("Entrez la langue du livre : \n")
                    Résumé=input("Entrez le résumé du livre :\n")
                    Éditeur= input("Entrez l'éditeur de la ressource : \n")
                    sql_ajout_livre="INSERT INTO Ressource VALUES ('%s','%s','%s','%s','%d','%d','%s','%s','%s',NULL,NULL,NULL,NULL,'%s')" % (Code, Titre, Éditeur, Genre, Date_appartion, Nb_exemplaire,ISBN,Langue_livre,Résumé, Type)
                    cur.execute(sql_ajout_livre)
                    print("La ressource ", Titre,  "a bien été ajoutée")
                elif(Type=='Film'):
                    Synopsis=input("Entrez le synopsis du film : \n")
                    Langue_film=input("Entrez la langue du film : \n")
                    Durée_film=input("Entrez la durée du film sous le format HH:MM:SS : \n")
                    sql_ajout_film="INSERT INTO Ressource VALUES ('%s','%s',NULL,'%s','%d','%d',NULL,NULL,NULL,'%s','%s','%s',NULL,'%s')" % (Code, Titre, Genre, Date_appartion, Nb_exemplaire,Synopsis,Langue_film,Durée_film, Type)
                    cur.execute(sql_ajout_film)
                    print("La ressource ", Titre,  "a bien été ajoutée")
                elif(Type=='Oeuvremusicale'):
                    Durée_oeuvre=input("Entrez la durée de l'oeuvre sous le format HH:MM:SS :\n")
                    sql_ajout_OM="INSERT INTO Ressource VALUES ('%s','%s',NULL,'%s','%d','%d',NULL,NULL,NULL,NULL,NULL,NULL,'%s','%s')" % (Code, Titre, Genre, Date_appartion, Nb_exemplaire,Durée_oeuvre, Type)
                    cur.execute(sql_ajout_OM)
                    print("La ressource ", Titre,  "a bien été ajoutée")

            #ajout d'un exemplaire : ajout dans la table exemplaire et modification du nombre de 'exemplaire de la table ressource
            elif (choix_2==2):
                Clé= input("Entrez la clé de l'exemplaire :\n")
                Code_E= input("Entrez le code de la ressource :\n")
                sql_type="SELECT Type FROM Ressource WHERE Ressource.Code = '%s'" %Code_E
                cur.execute(sql_type)
                row = cur.fetchone()
                État= input("Entrez l'état de l'exemplaire : \n")
                sql_type="SELECT Type FROM Ressource WHERE Ressource.Code = '%s'" %Code_E
                cur.execute(sql_type)
                row = cur.fetchone()
                sql_ajout_exemplaire="INSERT INTO Exemplaire VALUES ('%s','%s','%s','%s',true,'%d')"%(Clé,row[0], Code_E, État,0)
                sql_titre="SELECT Titre FROM Ressource WHERE Ressource.Code = '%s'" %Code_E
                cur.execute(sql_titre)
                row = cur.fetchone()
                print("L'exemplaire ",Clé," de la ressource ",row[0]," a bien été ajouté\n")
                sql_recuperation_nbexemplaire="SELECT Nb_exemplaire FROM Ressource WHERE Ressource.Code = '%s'" %Code_E
                cur.execute(sql_recuperation_nbexemplaire)
                row = cur.fetchone()
                sql_nb_exemplaire="UPDATE Ressource SET Nb_exemplaire= '%d' WHERE Code='%s' " %(row[0]+1,Code_E)
                cur.execute(sql_nb_exemplaire)

            #modification d'un exemplaire : on ne veut pas changer le code de la ressource, donc le type non plus, et la clé non plus: juste l'état et la Disponibilité
            elif (choix_2==3):
                #affichage des titres et de la clé de tous les exemplaires
                sql_consult_exemplaire="SELECT Ressource.Titre, Exemplaire.Clé FROM Ressource INNER JOIN Exemplaire ON Ressource.Code=Exemplaire.Code"
                cur.execute(sql_consult_exemplaire)
                result = cur.fetchall()
                for row in result:
                    print(row)
                    print("\n")

                Clé= input("Entrez la clé de l'exemplaire à modifier: \n")
                sql_lecture="SELECT * FROM Exemplaire WHERE Clé='%s'" %Clé
                cur.execute(sql_lecture)
                row = cur.fetchone()
                while not row :
                    print("Cet exemplaire n'existe pas \n")
                    Clé= input("Entrez la clé de l'exemplaire à modifier: \n")
                    sql_lecture="SELECT * FROM Exemplaire WHERE Clé='%s'" %Clé
                    cur.execute(sql_lecture)
                    row = cur.fetchall()
                print("Type: ",row[1]," Code: ",row[2],", État: ",row[3],", Disponibilité: ",row[4],", compteur: ",row[5],"\n")
                État= input("Entrez le nouvel état de l'exemplaire : \n")
                disp=int(input("est-ce que l'exemplaire est encore disponible? 1 oui, 0 Non \n"))
                if(disp==1) :
                        sql_nb_exemplaire="UPDATE Exemplaire SET État='%s', Disponibilité='true' WHERE Clé= '%s' " %(État,Clé)
                        cur.execute(sql_nb_exemplaire)
                elif(disp==0) :
                        sql_nb_exemplaire="UPDATE Exemplaire SET État='%s', Disponibilité='false' WHERE Clé= '%s' " %(État,Clé)
                        cur.execute(sql_nb_exemplaire)
                print("L'exemplaire a été modifié \n")

            elif (choix_2==4):
                #affichage des titres de toutes les ressouprintrces
                sql_consult="SELECT Titre FROM Ressource"
                cur.execute(sql_consult)
                result = cur.fetchall()
                for row in result:
                    print(row, "\n")
                Titre= input("Entrez le Titre de la ressource à consulter: \n")
                sql_lecture="SELECT * FROM Ressource WHERE Titre='%s'" %Titre
                cur.execute(sql_lecture)
                row = cur.fetchone()

                #test si la ressource existe, sinon on redemande
                while not row :
                    print(" Cette ressource n'existe pas \n")
                    Titre= input("Entrez le Titre de la ressource à consulter: \n")
                    sql_lecture="SELECT * FROM Ressource WHERE Titre='%s'" %Titre
                    cur.execute(sql_lecture)
                    row = cur.fetchone()

                if (row[13]=='Livre'):
                    print("Titre: ",row[1],", Éditeur: ",row[2],", Genre: ",row[3],", Date_apparition: ",row[4],", Nb_exemplaire: ",row[5],", ISBN: ",row[6],", Langue_livre: ",row[7],", Résumé: ",row[8],"\n")
                elif (row[13]=='Film'):
                    print("Titre: ",row[1],", Éditeur: ",row[2],", Genre: ",row[3],", Date_apparition: ",row[4],", Nb_exemplaire: ",row[5],",  Synopsis: ",row[9],", Langue_film: ",row[10],", Durée_film: ",row[11],"\n")
                else:
                    print("Titre: ",row[1],", Éditeur: ",row[2],", Genre: ",row[3],", Date_apparition: ",row[4],", Nb_exemplaire: ",row[5],",  Durée_oeuvre:",row[12],"\n")

            elif(choix_2==5):
                ressource_disp=input("Titre de la ressource dont vous souhaitez vérifier la disponibilité : \n")
                sql_disponibilité = "SELECT COUNT(Exemplaire.Disponibilité) FROM Ressource INNER JOIN Exemplaire ON Ressource.Code=Exemplaire.Code WHERE (Ressource.Titre='%s' AND Exemplaire.Disponibilité='true' ) "%(ressource_disp)
                cur.execute(sql_disponibilité)
                row = cur.fetchone()
                print(" La ressource ",ressource_disp," est disponible en ",row[0]," exemplaires \n")

        #menu des actions sur les adhérents
        elif (choix == 2) :
            choix_2 = int(input(" Que voulez-vous faire : \n 1. Ajouter un adhérent \n 2. Modifier les informations personnelles d'un adhérent \n 3. Modifier l'adhésion d'un adhérent \n 4. Accéder aux informations d'un adhérent \n 5. Afficher la liste des adhérents \n"))
            if (choix_2==1) :
                login=input("Entrez le login de l'adhérent : \n")
                mdp=input("Entrez le mot de passe de l'adhérent : \n")
                Nom=input("Entrez le nom de l'adhérent : \n")
                Prenom=input("Entrez le prénom de l'adhérent : \n")
                Adresse= input("Entrez l'adresse de l'adhérent : \n")
                Mail=input("Entrez son mail : \n")
                Num_tele=input("Entrez le numero de téléphone : \n")
                Date_naissance=input("Entrez la date de naissance de l'adhérent sous la forme YYYY-MM-DD: \n")
                Num_carte =input("Entrez le numéro de la carte : \n")
                sqlajout="INSERT INTO Compte_utilisateur VALUES ('%s', '%s')"%(login, mdp)
                cur.execute(sqlajout)
                sql_ajout_adherent="INSERT INTO Adherents VALUES ('%s','%s','%s','%s','%s','%s','%s','%d','%d','%s')" % (login, Nom, Prenom, Adresse, Mail, Num_tele,Date_naissance,0,0, Num_carte)
                cur.execute(sql_ajout_adherent)
                print("L'adérent ",Nom," ",Prenom," a bien été ajouté \n")

            elif (choix_2==2) :
                login2 = input("Entrez le login de l'adhérent : \n")
                #vérifier si l'adhérent est déjà dans la liste des adhérents
                sql22="SELECT login FROM Adherents WHERE login='%s'" %login2
                cur.execute(sql22)
                row = cur.fetchone()
                while not row :
                    print( "le login n'est pas bon \n")
                    login2 = input("Entrez le login : \n")
                    sql22 = "SELECT login FROM Adherents WHERE login='%s'" %(login2)
                    cur.execute(sql22)
                    row = cur.fetchone()

                # menu des informations que le personnel pourrait modifier
                information=int(input("Veuillez choisir l'information que vous voulez modifier : 1.Nom 2.Prenom 3.Adresse 4.Mail 5.Numéro de téléphone 6.Date de naissance 7.nombre de retard 8.nombre de dégradation 9.Numéro de carte 0.quitter \n"))

                while information != 0 : #modifier plusieurs informations d'un adhérent
                    if (information==1):
                        Nom_n=input("Entrez le nom : \n")
                        sql_nom="UPDATE Adherents SET Nom = '%s' WHERE login = '%s' " % (Nom_n,login2)
                        cur.execute(sql_nom)
                        print("Le nom ", Nom_n, " a bien été enregistré \n")
                        information=int(input("Veuillez choisir l'information que vous voulez modifier : 1.Nom 2.Prenom 3.Adresse 4.Mail 5.Numéro de téléphone 6.Date de naissance 7.nombre de retard 8.nombre de dégradation 9.Numéro de carte 0.quitter \n"))

                    elif(information==2):
                        Prenom_n=input("Entrez le prenom : \n")
                        sql_prenom="UPDATE Adherents SET Prenom = '%s' WHERE login = '%s' " % (Prenom_n,login2)
                        cur.execute(sql_prenom)
                        print("Le prénom ",Prenom_n , " a bien été enregistré \n")
                        information=int(input("Veuillez choisir l'information que vous voulez modifier : 1.Nom 2.Prenom 3.Adresse 4.Mail 5.Numéro de téléphone 6.Date de naissance 7.nombre de retard 8.nombre de dégradation 9.Numéro de carte 0.quitter \n"))

                    elif(information==3):
                        Adresse_n= input("Entrez l'adresse de l'adhérent : \n")
                        sql_adr="UPDATE Adherents SET Adresse = '%s' WHERE login = '%s' " % (Adresse_n,login2)
                        cur.execute(sql_adr)
                        print("L'adresse ", Adresse_n, " a bien été enregistré \n")
                        information=int(input("Veuillez choisir l'information que vous voulez modifier : 1.Nom 2.Prenom 3.Adresse 4.Mail 5.Numéro de téléphone 6.Date de naissance 7.nombre de retard 8.nombre de dégradation 9.Numéro de carte 0.quitter \n"))


                    elif(information==4):
                        Mail_n=input("Entrez son mail : \n")
                        sql_mail="UPDATE Adherents SET Mail = '%s' WHERE login = '%s' " % (Mail_n,login2)
                        cur.execute(sql_mail)
                        print("Le mail ",Mail_n ," a bien été enregistré \n")
                        information=int(input("Veuillez choisir l'information que vous voulez modifier : 1.Nom 2.Prenom 3.Adresse 4.Mail 5.Numéro de téléphone 6.Date de naissance 7.nombre de retard 8.nombre de dégradation 9.Numéro de carte 0.quitter \n"))


                    elif(information==5):
                        Num_tele_n=int(input("Entrez le nombre de téléphone : \n"))
                        sql_numtele="UPDATE Adherents SET Num_telephone = '%d' WHERE login = '%s' " % (Num_tele_n,login2)
                        cur.execute(sql_numtele)
                        print("Le numéro de téléphone ",Num_tele_n," a bien été enregistré \n")
                        information=int(input("Veuillez choisir l'information que vous voulez modifier : 1.Nom 2.Prenom 3.Adresse 4.Mail 5.Numéro de téléphone 6.Date de naissance 7.nombre de retard 8.nombre de dégradation 9.Numéro de carte 0.quitter \n"))


                    elif(information==6):
                        Date_naissance_n=input("Entrez la date de naissance de l'adhérent sous la forme YYYY-MM-DD: \n")
                        sql_date="UPDATE Adherents SET Date_de_naissance = '%s' WHERE login = '%s' " % (Date_naissance_n,login2)
                        cur.execute(sql_date)
                        print("La date de naissance ",Date_naissance_n," a bien été enregistré \n")
                        information=int(input("Veuillez choisir l'information que vous voulez modifier : 1.Nom 2.Prenom 3.Adresse 4.Mail 5.Numéro de téléphone 6.Date de naissance 7.nombre de retard 8.nombre de dégradation 9.Numéro de carte 0.quitter \n"))


                    elif(information==7):
                        Nb_retard_n =int(input("Entrez le nombre de retard pour retourner une ressource : \n"))
                        sql_retard="UPDATE Adherents SET Nb_retard = '%s' WHERE login = '%s' " % (Nb_retard_n,login2)
                        cur.execute(sql_retard)
                        print("Le nombre de retard ",Nb_retard_n," a bien été enregistré \n")
                        information=int(input("Veuillez choisir l'information que vous voulez modifier : 1.Nom 2.Prenom 3.Adresse 4.Mail 5.Numéro de téléphone 6.Date de naissance 7.nombre de retard 8.nombre de dégradation 9.Numéro de carte 0.quitter \n"))


                    elif(information==8):
                        Nb_degradation_n =int(input("Entrez le nombre de dégradation de la ressource : \n"))
                        sql_degradation="UPDATE Adherents SET Nb_degradation = '%s' WHERE login = '%s' " % (Nb_degradation_n,login2)
                        cur.execute(sql_degradation)
                        print("Le nombre de degradation ",Nb_degradation_n," a bien été enregistré \n")
                        information=int(input("Veuillez choisir l'information que vous voulez modifier : 1.Nom 2.Prenom 3.Adresse 4.Mail 5.Numéro de téléphone 6.Date de naissance 7.nombre de retard 8.nombre de dégradation 9.Numéro de carte 0.quitter \n"))


                    elif(information==9):
                        Num_carte_n =input("Entrez le numéro de la carte : \n")
                        sql_carte="UPDATE Adherents SET carte = '%s' WHERE login = '%s' " % (Num_carte_n,login2)
                        cur.execute(sql_carte)
                        print("Le numéro de la carte ",Num_carte_n," a bien été enregistré \n")
                        information=int(input("Veuillez choisir l'information que vous voulez modifier : 1.Nom 2.Prenom 3.Adresse 4.Mail 5.Numéro de téléphone 6.Date de naissance 7.nombre de retard 8.nombre de dégradation 9.Numéro de carte 0.quitter \n"))



            elif (choix_2==3) :
                login_modif=input("Entrez le login de l'adhérent dont vous voulez modifier l'adhésion : \n")
                date_fin=input("Entrez la nouvelle date de fin de l'adhésion : \n")
                sql_adhesion="UPDATE Adhesions SET FIN = '%s' WHERE login = '%s' " % (date_fin,login_modif)
                cur.execute(sql_adhesion)
                print("L'adhésion de l'adhérent ",login_modif, " a bien été enregistrée\n")


            elif (choix_2==4) :
                login_info=input("Entrez le login de l'adhérent dont vous voulez consulter les informations : \n")
                sql_info= "SELECT * FROM Adherents WHERE login = '%s' " %login_info
                cur.execute(sql_info)
                raw = cur.fetchone()
                print(raw)
                while(not raw):
                    login_info=input("Mauvais login, Entrez le login de l'adhérent dont vous voulez consulter les informations : \n")
                    sql_info= "SELECT Adherents.login,Adherents.Nom ,Adherents.Prenom ,Adherents.Adresse ,Adherents.Mail,Adherents.Num_telephone,Adherents.Date_de_naissance ,Adherents.Nb_retard ,Adherents.Nb_degradation,Adherents.carte,Adhesions.Debut,Adhesions.FIN, EMPRUNT.emprunt_enCours, Reservation.état_reservation, Sanction.En_sanction FROM (((Adherents INNER JOIN Adhesions ON Adherents.login= Adhesions.login)INNER JOIN EMPRUNT ON EMPRUNT.login=Adhesions.login)INNER JOIN Reservation ON Reservation.login=Adhesions.login)INNER JOIN Sanction ON Sanction.login=Adhesions.login" %login_info
                    cur.execute(sql_info)
                    raw = cur.fetchone()
                print(" login : ", raw[0] ,"\nNom : ",raw[1],"\nPrenom : ",raw[2],"\nAdresse: ",raw[3],"\nMail: ",raw[4],"\nNuméro de telephone: ",raw[5],"\nDate de naissance: ",raw[6],"\nNombre de retard: ",raw[7],"\nNombre de degradation: ",raw[8],"\ncarte: ",raw[9],"\nDebut d'adhésion: ",raw[10],"\nFin d'adhésions: ",raw[11],"\n Emprunt en Cours: ",raw[12],"\n reservation en cours: ",raw[13],"\nEn sanction: ",raw[14]," \n")

            elif (choix_2==5) :
                sql="SELECT * FROM Adherents"
                cur.execute(sql)
                result = cur.fetchall()
                for row in result:
                    print(row,"\n")



        #menu des actions sur emprunts, réservation et sanction
        elif (choix == 3) :
            choix_2 = int(input(" Que voulez-vous faire : \n 1. Ajouter un emprunt \n 2. Modifier (retour, et autres modifications) un emprunt \n 3. Ajouter une réservation \n 4. Modifier une réservation \n 5. Afficher la liste des emprunts en cours \n 6. Sanctionner \n"))
            if choix_2 == 1:
                duré = input("Entrez la date limite de l'emprunt sous la forme YYYY-MM-DD : \n")
                login = input("Entrez le login de la personne qui emprunte la ressource : \n")
                cle = input("Entrez la clé de l'exemplaire : \n")
                sql_empr = "INSERT INTO EMPRUNT VALUES ('%s', '%s',true, '%s')" % (cle , login, duré)
                cur.execute(sql_empr)
                sql00 = "UPDATE Exemplaire SET Disponibilité =false WHERE Clé='%s'" % (cle)
                cur.execute(sql00)
                sql = "SELECT compteur FROM Exemplaire WHERE Clé='%s'" % (cle)
                cur.execute(sql)
                row = cur.fetchone()
                cpt=row[0]+1
                sql01 = "UPDATE Exemplaire SET compteur ='%s' WHERE Clé='%s'" % (cpt, cle)
                cur.execute(sql01)
                conn.commit()
            elif choix_2 == 2:
                date_retour = input("Entrez la date du retour de l'emprunt sous la forme YYYY-MM-DD : \n")
                login = input("Entrez le login de la personne qui emprunte la ressource : \n")
                cle = input("Entrez la clé de l'exemplaire : \n")
                sql = "SELECT Durée_limite FROM EMPRUNT WHERE login='%s' AND Clé='%s'" % (login,cle)
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
                    sql_sanction = "INSERT INTO Sanction VALUES ('%s', '%s',true,true,'%s', false,'%s')" % (cle , login, date_retour, None)
                    cur.execute(sql_sanction)
                    conn.commit()
            elif choix_2 == 3:
                cle = input("Entrez la clé de l'exemplaire : \n")
                login = input("Entrez le login de la personne qui réserve la ressource : \n")
                date_effective = input("Entrez la date effective de la réservation sous la forme YYYY-MM-DD : \n")
                sql01 = "UPDATE Exemplaire SET  Disponibilité ='false' WHERE Clé='%s'" % (cle)
                cur.execute(sql01)
                conn.commit()
                Sql_reserv = "INSERT INTO Reservation VALUES ('%s', '%s',true, '%s')" % (cle , login, date_effective)
                cur.execute(Sql_reserv)
                conn.commit()
            elif choix_2 == 4:
                choix_3= int(input("Que voulez-vous faire 1. Modifier la date de la réservation 2. Modifié la ressource de la réservation \n"))
                if choix_3 ==1 :
                    cle = input("Entrez la clé de l'exemplaire : \n")
                    login = input("Entrez le login de la personne qui réserve la ressource : \n")
                    date_effective = input("Entrez la nouvelle date effective de la réservation sous la forme YYYY-MM-DD : \n")
                    sql01 = "UPDATE Reservation SET  reserv_date ='%s' WHERE Clé='%s' AND login='%s'" % ( date_effective, cle, login)
                    cur.execute(sql01)
                    conn.commit()
                elif choix_3 ==2 :
                    cle = input("Entrez la l'ancienne clé de l'exemplaire : \n")
                    cle2 = input("Entrez la nouvelle clé de l'exemplaire : \n")
                    login = input("Entrez le login de la personne qui réserve la ressource : \n")
                    sql01 = "UPDATE Reservation SET  Clé ='%s' WHERE Clé='%s' AND login='%s'" % ( cle2, cle, login)
                    cur.execute(sql01)
                    conn.commit()
                    sql01 = "UPDATE Exemplaire SET Disponibilité ='true' WHERE Clé='%s'" % (cle)
                    cur.execute(sql01)
                    conn.commit()
            elif choix_2 == 5:
                sql = "SELECT Clé, login FROM EMPRUNT WHERE emprunt_enCours ='true'"
                cur.execute(sql)
                raw = cur.fetchone()
                for i in range(len(raw)):
                    Cle = raw[i][0]
                    login = raw[i][1]
                    print("Les emprunt en cours sont ",Cle, login,"\n")
            elif choix_2 == 6:
                date_effective = input("Entrez la date du retour effective de la sanction sous la forme YYYY-MM-DD : \n")
                login = input("Entrez le login de la personne qui sanctionner: \n")
                cle = input("Entrez la clé de l'exemplaire : \n")
                sanction=int(input("Entrez 1 si la sanction est une degradation et 0 si c'est un retard \n"))
                if sanction==0:
                    sql_sanction = "INSERT INTO Sanction VALUES ('%s', '%s',true,false,'%s', true,'%s')" % (cle , login, None, date_effective)
                    cur.execute(sql_sanction)
                    conn.commit()
                elif sanction==1:
                    sql_sanction = "INSERT INTO Sanction VALUES ('%s', '%s',true,true,'%s', false,'%s')" % (cle , login, date_effective, None)
                    cur.execute(sql_sanction)
                    conn.commit()

        else :
            break
else :
#Vérifier d'abord si l'adhérent est en sanction
    sql3="SELECT S.En_sanction FROM Sanction S JOIN Adherents A ON S.login = A.login WHERE S.login='%s'" %login_user
    cur.execute(sql3)
    row3 = cur.fetchone()
    if (row3 == "True") :
        print("Désolé, vous êtes en sanction\n")
    #Si l'adhérent n'est pas en sanction : entrer dans le menu adhérents
    else :
        #menu adhérents
        choix = -1
        while choix!=0 :
            choix = int(input(" Que voulez-vous faire : \n 1.Consulter votre l'historique d'emprunt\n 2.Voir notre recommandation selon vos intérêts\n 3.rechercher un exemplaire \n 0. Sortir \n"))
            if (choix == 1) :
                sql5="SELECT * FROM Emprunt E Join Adherents A ON E.login = A.login WHERE E.login='%s'" %login_user
                cur.execute(sql5)
                row5 = cur.fetchall()
                print("Votre historique est : \n")
                for i in range(len(row5)):
                    print(row5[:][i], "\n")
            elif (choix == 2) :
                #recommandations par genre
                sql_a="SELECT * FROM Genre4 WHERE login='%s'" %login_user
                cur.execute(sql_a)
                row5 = cur.fetchone()
                sql0="SELECT Code,Titre FROM Ressource WHERE Genre='%s'" %row5[1]
                cur.execute(sql0)
                row = cur.fetchall()
                print("Nous vous recommandons les ressourses suivantes: \n")
                for i in range(2):
                    # on affiche 3 Ressource pour pas surcharger
                    print(row[i][0],row[i][1]," \n")
                #recommandations par langue
                #sql_a="SELECT * FROM LangueFilm2 WHERE login='%s'" %login_user
                #cur.execute(sql_a)
                #row5 = cur.fetchone()
                #sql0="SELECT Code,Titre FROM Ressource WHERE Langue_film='%s'" %row5[1]
                #cur.execute(sql0)
                #row = cur.fetchall()
                #print("Nous vous recommandons les ressourses suivantes: \n")
                #for i in range(1):
                    # on affiche 3 Ressource pour pas surcharger
                #        print(row[i][0],row[i][1]," \n")
            elif (choix == 3) :
                type_recherche=int(input("quel type de recherche voulez-vous faire ? \n 1. par titre \n 2. par Type (Livre, Film , Oeuvremusicale ) \n 3. par genre ? \n"))
                if type_recherche == 1:
                    titre = input("Entrez la titre de la resource voulu : \n")
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
                    sql = "SELECT Titre FROM Ressource WHERE Type ='%s'" %(type)
                    cur.execute(sql)
                    raw = cur.fetchall()
                    print("Les ressource corespondant à ",type," sont \n")
                    print(raw,"\n")
                elif type_recherche == 3:
                    genre = input("Entrez le genre de la resource voulu : \n")
                    sql = "SELECT Titre FROM Ressource WHERE Genre ='%s'" %(genre)
                    cur.execute(sql)
                    raw = cur.fetchall()
                    print("Les ressource corespondant à ",genre," sont \n")
                    print(raw, "\n")
conn.commit()
conn.close()
