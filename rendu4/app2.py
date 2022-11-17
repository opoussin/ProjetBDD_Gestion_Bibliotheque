#!/usr/bin/python3


        else : 
        #menu adhérents
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
                cur.execute(sql4)
                row4 = cur.fetchone()
                print(row4)
                
            #Recommandation selon les intérêts
            elif (choix == 3) :
                
            else : 
                break




conn.commit()

conn.close()