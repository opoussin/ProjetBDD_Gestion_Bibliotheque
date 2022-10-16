<h1>Note de clarification</h1>

<h2> Objets </h2>
 
Pour commencer, nous voulons représenter les tables explicites du sujet : 

     Adherents ( Nom : char, Prenom : char , Adresse : char , Mail : char, Num_telephone : int, Date_de_naissance : Date, carte : str ). Pour relier la carte d’adhérent à l’adhérent, nous 	avons rajouté un attribut carte directement dans la table Adherents.

     Personnel( Nom : char, Prenom : char, Adresse : char, Mail : char)
    
     Compte_utilisateur( Login : {KEY} , Mot_de_passe : Unique not null )

     Contributeur( Rôle :char, Nom :char, Prenom :char, Date_de_naissance:Date, Nationalité: char)
   
     Ressource ( Code :int, Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int )

Puisque les différentes ressources ‘livre’, ‘film’ et ‘oeuvre musicale’ possèdent des attributs communs mais également propres à eux mêmes, nous avons décidés de les représenter en tant que classes filles de la classe mère Ressource:

	 Livre ( ISBN : char, Langue : char , Résumé: char )

	 Film ( Synopsis: char, Langue : char , Durée_film: time) 

	 œuvremusicale ( Durée_oeuvre: Time)

Pour répondre au besoin d’avoir un historique des adhésions de la bibliothèque, nous avons créé une table Adhesions : 

	 Adhesions ( Encours : booléen, Début : Date, Fin: Date)

Nous voulons gérer les emprunts de ressources par les adhérents( exemplaire emprunté, durée d’emprunt, l’état de la ressource à son retour), et nous souhaitons également en garder un historique en cas de dégradation des ressource empruntées. nous avons donc créé une table emprunt en cours:   

     Emprunt_en_cours( Durée_limite: date  , Etat_retour: varchar, En_cours : bool)

De plus, puisqu’une ressource peut être présente en plusieurs exemplaires, et qu’il faut contrôler l’état et la disponibilité d’un exemplaire pour le louer, nous proposons une table exemplaire, avec un attribut clé qu’il faudrait rajouter pour distinguer tous les exemplaires d’une même ressource: 

     Exemplaire ( Clé : char, État : enum, Disponibilités : char, compteur : int)

Pour gérer les possibles sanctions envers un adhérent, nous avons créé une table sanction.

	 Sanction ( Nb_retard : int, Nb_degradation : int, En_sanction :Boolean, Durée_sanction: )


<h2>Cardinalités </h2>

- Un adhérent peut faire 0 ou NMAX emprunts avec NMAX le nombre maximum d'emprunts simultanés. Un emprunt correspond à un seul adhérent.
- <i> !!!!! Un emprunt correspond à un seul exemplaire. Un exemplaire peut appartenir à aucun ou un seul emprunt en cours. !!!!!!!!!!</i>
- Un adhérent a un seul compte utilisateur. Un compte utilisateur correspond à un seul adhérent.
- Un compte utilisateur correspond à un seul membre de la bibliothèque (Personnel). Un membre de la bibliothèque (Personnel) possède un seul compte utilisateur. 
- Un exemplaire correspond à une seule ressource. Une ressource peut avoir 1 ou plusieurs exemplaires.
- Un contributeur contribue à au moins une ressource. Une ressource a au moins un contributeur

 

    - Adherent --> Emprunt : 1 adhérent peut faire 0 ou n emprunts (Nmax nombre maximum)
    - Emprunt -> adherent: un emprunt correspond à un seul adhérent
    - Emprunt -> Exemplaire : un emprunt correspond à un seul exemplaire
    - Exemplaire -> Emprunt: un exemplaire peut appartenir à aucun ou un seul emprunt  
    - Adherent -> Compte utilisateur : un adhérent a un seul compte utilisateur
    - COmpte utilisateur -> Adhérent: un compte correspond à un seul adhérent (utilisateur)
    - Compte -> Personnel: un compte pour un seul Personnel
    - Personnel -> Compte: un personnel a un seul compte
    - Exemplaire - Ressource: un exemplaire correspond à une seule ressource
    - Ressource -> Exemplaire: Un ressource peut avoir 1 ou plusieurs exemplaires
    - Contributeur -> Ressource : un contributeur contribue à au moins une ressource 
    - Ressource -> Contributeur: une ressource a au moins un contributeur






<h2>Notes:</h2>

- Pour établir la liste des documents populaires, un compteur du nombre d'emprunts est ajouté à la table Exemplaire, ce compteur servira à calculer les statistiques dans la partie python.  
- L'historique des emprunts est gardé dans la table Emprunt_en_cours.
- Les sanctions sont définies dans la table Sanction, tant que le booleen indique que la sanction est en cours (mise à jour en fonction de la date de fin), le droit d'emprunt de l'utilisateur est suspendu 
- Un membre du personnel de la bibliothèque n'est pas adhérent. 
- Exemplaire perdu ..? (je sais plus si on a dit que le compteur diminue ou non en attendant que le livre soit remboursé)


