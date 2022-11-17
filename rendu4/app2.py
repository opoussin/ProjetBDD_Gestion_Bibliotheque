#!/usr/bin/python3

    #Si login n'est pas dans la liste personnels
    else : 
            #Vérifier d'abord si l'adhérent est en sanction
            sql3="SELECT S.En_sanction FROM Sanction S JOIN Adherents A ON S.login = A.login WHERE S.login=%s" %login_user
            cur.execute(sql3)
            row3 = cur.fetchone()
            if (row3 == "TRUE") :
                print("Désolé, vous êtes en sanction\n")
                break
            #Si l'adhérent n'est pas en sanction : entrer dans le menu adhérents
            else : 
        #menu adhérents
        choix = -1
        while(choix!=0) :
            choix = int(input(" Que voulez-vous faire : \n 1.Réserver une ressource \n 2.Consulter votre l'histoirique d'emprunt\n 3.Voir notre recommandation selon vos intérêts\n 0. Sortir\n"))
            #Des actions pour réserver un exemplaire d'une ressource
           
            if (choix == 1) :
                choix_1 = int(input("Veuillez entrer le code de la ressource que vous souhaitez réserver\n"))
                #vérifier s'il reste encore des exemplaires à réserver
                sql4="SELECT * FROM Exemplaire E Join Ressource R ON E.Code = R.Code WHERE E.Code=%s" %choix_1
                cur.execute(sql4)
                row4 = cur.fetchone()
                if(row4) : 


            #Consultation de l'histoirique
            elif (choix == 2) :
                sql5="SELECT * FROM Emprunt E Join Adherents A ON E.login = A.login WHERE E.login=%s" %user_login
                cur.execute(sql5)
                row5 = cur.fetchone()
                print(row5)
                print("\n")
                
            #Recommandation selon les intérêts
            elif (choix == 3) :
                
            elif (choix == 0) :
                break

            #remarque : pour les autres nombres, on ne va pas entrer dans les 'if', et on va donc tomber dans la boucle while






conn.commit()

conn.close()
