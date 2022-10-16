OBJETS:
 
Pour commencer, nous voulons représenter les tables explicites du sujet : 

    - Adherents ( Nom : char, Prenom : char , Adresse : char , Mail : char, Num_telephone : int, Date_de_naissance : Date, carte : str ). Pour relier la carte d’adhérent à l’adhérent, nous 	avons rajouté un attribut carte directement dans la table Adherents.

    - Personel( Nom : char, Prenom : char, Adresse : char, Mail : char)
    
    - compte_utilisateur( Login : {KEY} , Mot_de_passe : Unique not null )

    - contributeur( Rôle :char, Nom :char, Prenom :char, Date_de_naissance:Date, Nationalité: char)
   
    - Ressource ( Code :int, Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int )


Puisque les différentes ressources ‘livre’, ‘film’ et ‘oeuvre musicale’ possèdent des attributs communs mais également propres à eux mêmes, nous avons décidés de les représenter en tant que classes filles de la classe mère Ressource:

	- livre ( ISBN : char, Langue : char , Résumé: char )

	- film ( Synopsis: char, Langue : char , Duré: time) 

	- œuvremusicale ( Durée: Time)
	
Pour répondre au besoin d’avoir un historique des adhésions de la bibliothèque, nous avons créé une table Adhesions : 

	- Adhesions ( Encours : booléen, Début : Date, Fin: Date)

Nous voulons gérer les emprunts de ressources par les adhérents( exemplaire emprunté, durée d’emprunt, l’état de la ressource à son retour), et nous souhaitons également en garder un historique en cas de dégradation des ressource empruntées. nous avons donc créé une table emprunt en cours:   

    - Emprun_en_cours( Durée_limite: date  , Etat_retour: varchar, Encour? : bool)

De plus, puisqu’une ressource peut être présente en plusieurs exemplaires, et qu’il faut contrôler l’état et la disponibilité d’un exemplaire pour le louer, nous proposons une table exemplaire, avec un attribut clé qu’il faudrait rajouter pour distinguer tous les exemplaires d’une même ressource: 

    - Exemplaire ( Clé : char, État : enum, Disponibilités : char, compteur : int)

Pour gérer les possibles sanctions envers un adhérent, nous avons créé une table sanction.

	- Sanction ( Nb_retard : int, Nb_degradation : int, En_sanction :Boolean, Durée_sanction: )

