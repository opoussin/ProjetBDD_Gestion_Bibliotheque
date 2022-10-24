<h1>MLD 1ère Version : </h1>

<h2> Relation entre Adherents et Compte_utilisateur:</h2>

<b>Rappel : </b> Adherents(Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ); et Compte_utilisateur( Login : int, Mot_de_passe : string):

    Adherents(#login=>Compte_utilisateur, Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str )

<b>Contraintes</b>
- Num_telephone UNIQUE
- Mail UNIQUE
- Nom, Prenom, Adresse, Date_de_naissance NOT NULL

<h2> Relation entre Personnel et Compte_utilisateur:</h2>

<b>Rappel : </b>Personnel(Nom : char, Prenom : char ,Adresse : char ,Mail : char) et Compte_utilisateur( Login : int, Mot_de_passe : string):

    Personnel(#login=>Compte_utilisateur, Nom : char, Prenom : char ,Adresse : char ,Mail : char)

<b>Contraintes</b>
- Mail UNIQUE
- Nom, Prenom, Adresse NOT NULL

<h2> Relation entre Adherents et Adhesions</h2>

<b>Rappel : </b>Adherents(Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ); et Adhesions(Début : Date, Fin: Date)

    Adhesions(#login=>Adherents, Début : Date, Fin: Date)

<b>Contraintes</b>
- Début NOT NULL

<h2>Héritage par la classe mère de la relation Ressource; Film, Livre, œuvremusicale</h2>

<b>Rappel : </b>Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int ) avec : Film( Synopsis: char, Langue : char , Durée_film: time  ) ; Livre( ISBN : char, Langue : char , Résumé: char ) ; œuvremusicale(Durée_oeuvre: Time)

    Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, ISBN : char, Langue : char , Résumé: char, Synopsis: char, Langue : char , Durée_film: time, Durée_oeuvre: Time, Livre : boolean, Film: Boolean, œuvremusicale= Boolean )

<b>Contraintes:</b>
- NOT (Livre AND Synopsis, Langue , Durée_film, Durée_oeuvre )
- NOT (Film AND ISBN , Langue, Résumé, Durée_oeuvre )
- NOT (œuvremusicale AND ISBN , Langue, Résumé, Synopsis, Langue , Durée_film )
- Livre AND ISBN , Langue, Résumé
- Film AND Synopsis, Langue , Durée_film
- œuvremusicale AND Durée_oeuvre
- Film OR Livre OR œuvremusicale


<h2> Relation entre Contributeur et Ressource </h2>

Contributeur(#Rôle :char, #Nom :char, #Prenom :char, #Date_de_naissance:Date , Nationalité: char) 

Contribue(#Rôle =>Contributeur, #Code=>Ressource ) 

<h2>Composition entre Exemplaire et Ressource </h2>

<b>Rappel : </b>Exemplaire(État : enum,Clé : char , Disponibilités : Boolean ,compteur : int )et Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, ISBN : char, Langue : char , Résumé: char, Synopsis: char, Langue : char , Durée_film: time, Durée_oeuvre: Time, Livre : boolean, Film: Boolean, œuvremusicale= Boolean )

    Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, ISBN : char, Langue : char , Résumé: char, Synopsis: char, Langue : char , Durée_film: time, Durée_oeuvre: Time, Livre : boolean, Film: Boolean, œuvremusicale= Boolean )

    Exemplaire(#Clé : char , #Code =>Ressource, État : enum, Disponibilité : boolean ,compteur : int )

<b>Contraintes</b>
- État, compteur NOT NULL

<h2> Relation entre Emprunt, Reservation, Adherents, et Exemplaire </h2>

<b>Rappel : </b>Emprunt(emprunt_enCours: Boolean, Durée_limite : Date, Etat_retour : enum), Reservation(état_reservation: Boolean,reserv_date : Date), Adherents(#login=>Compte_utilisateur, Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ), et Exemplaire(#Clé : char , #Code =>Ressource, État : enum, Disponibilité : char ,compteur : int )


    Emprunt(#Clé=>Exemplaire, #login=>Adherents, emprunt_enCours: Boolean, Durée_limite : Date, Etat_retour : enum)
    Reservation(#Clé=>Exemplaire, #login=>Adherents,état_reservation: Boolean,reserv_date : Date)


<h2>Héritage par la classe mère de la relation Sanction avec Retard et Degradation: </h2>

<b>Rappel : </b> Sanction(En_sanction :Boolean ) avec Retard(En_Retard :Boolean ,Debut_retard:date) et Degradation(En_Degradation :Boolean , Debut_degradation:date ): 

    Sanction(En_sanction :Boolean, En_Retard :Boolean ,Debut_retard:date, En_Degradation :Boolean , Debut_degradation:date)

<b>Contraintes</b>
- En_Retard AND Debut_Retard
- En_Degradation AND Debut_degradation
- (En_sanction AND En_Retard) OR (En_sanction AND En_Degradation)

<h2> Relation entre Emprunt; Adherents et Sanction</h2>

<b>Rappel : </b>Emprunt(emprunt_enCours: Boolean, Durée_limite : Date, Etat_retour : enum) ; Adherents(#login=>Compte_utilisateur, Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ); et Sanction(En_sanction :Boolean, En_Retard :Boolean ,Debut_retard:date, En_Degradation :Boolean , Debut_degradation:date)
    
    Sanction(#login=>Adhérents, #Clé=>Exemplaire, En_sanction :Boolean, En_Retard :Boolean ,Debut_retard:date, En_Degradation :Boolean , Debut_degradation:date)

<b>Contraintes</b>
- En_Retard AND Debut_Retard
- En_Degradation AND Debut_degradation
- (En_sanction AND En_Retard) OR (En_sanction AND En_Degradation)









