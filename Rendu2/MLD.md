

<b> Relation entre Adherents(Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ); et Compte_utilisateur( Login : int, Mot_de_passe : string):</b>

    Adherents(#login=>Compte_utilisateur, Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str )

<b> Relation entre Personnel(Nom : char, Prenom : char ,Adresse : char ,Mail : char) et Compte_utilisateur( Login : int, Mot_de_passe : string):</b>

    Personnel(#login=>Compte_utilisateur, Nom : char, Prenom : char ,Adresse : char ,Mail : char)

<b> Relation entre Adherents(Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ); et Adhesions(Début : Date, Fin: Date)</b>

    Adhesions(#login=>Adherents, Début : Date, Fin: Date)

<b>Héritage par la classe mère de la relation Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int ) avec : Film( Synopsis: char, Langue : char , Durée_film: time  ) ; Livre( ISBN : char, Langue : char , Résumé: char ) ; œuvremusicale(Durée_oeuvre: Time) </b>


    Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, ISBN : char, Langue : char , Résumé: char, Synopsis: char, Langue : char , Durée_film: time, Durée_oeuvre: Time, Livre : boolean, Film: Boolean, œuvremusicale= Boolean )
Contraintes:
- NOT (Livre AND Synopsis, Langue , Durée_film, Durée_oeuvre )
- NOT (Film AND ISBN , Langue, Résumé, Durée_oeuvre )
- NOT (œuvremusicale AND ISBN , Langue, Résumé, Synopsis, Langue , Durée_film )
- Livre AND ISBN , Langue, Résumé
- Film AND Synopsis, Langue , Durée_film
- œuvremusicale AND Durée_oeuvre
- Film OR Livre OR œuvremusicale


<b> Relation entre Contributeur et Ressource </b>

Contributeur( Rôle :char, Nom :char, Prenom :char, Date_de_naissance:Date , Nationalité: char) 

Contribue(#Rôle =>Contributeur, #Code=>Ressource ) 

<b> Composition entre Exemplaire(État : enum,Clé : char , Disponibilités : char ,compteur : int )et Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, ISBN : char, Langue : char , Résumé: char, Synopsis: char, Langue : char , Durée_film: time, Durée_oeuvre: Time, Livre : boolean, Film: Boolean, œuvremusicale= Boolean )</b>

    Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, ISBN : char, Langue : char , Résumé: char, Synopsis: char, Langue : char , Durée_film: time, Durée_oeuvre: Time, Livre : boolean, Film: Boolean, œuvremusicale= Boolean )

    Exemplaire(#Clé : char , #Code =>Ressource, État : enum, Disponibilité : char ,compteur : int )

<b> Relation entre Emprunt(emprunt_enCours: Boolean, Durée_limite : Date, Etat_retour : enum), Reservation(état_reservation: Boolean,reserv_date : Date), Adherents(#login=>Compte_utilisateur, Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ), et Exemplaire(#Clé : char , #Code =>Ressource, État : enum, Disponibilité : char ,compteur : int ) </b>

    Emprunt(#Clé=>Exemplaire, #login=>Adherents, emprunt_enCours: Boolean, Durée_limite : Date, Etat_retour : enum)
    Reservation(#Clé=>Exemplaire, #login=>Adherents,état_reservation: Boolean,reserv_date : Date)

Ici Emprunt et reservation sont transformées comme des classes d'associations entre Adhérents et Exemplaire. Donc Adhérents et Exemplaire restent inchangées.

<b>Héritage par la classe mère de la relation Sanction(En_sanction :Boolean ) avec Retard(En_Retard :Boolean ,Debut_retard:date) et Degradation(En_Degradation :Boolean , Debut_degradation:date ): </b>

    Sanction(En_sanction :Boolean, En_Retard :Boolean ,Debut_retard:date, En_Degradation :Boolean , Debut_degradation:date)


<b> Relation entre Emprunt(emprunt_enCours: Boolean, Durée_limite : Date, Etat_retour : enum) ; Adherents(#login=>Compte_utilisateur, Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ); et Sanction(En_sanction :Boolean, En_Retard :Boolean ,Debut_retard:date, En_Degradation :Boolean , Debut_degradation:date)</b>
    
    Sanction(#login=>Adhérents, #Clé=>Exemplaire, En_sanction :Boolean, En_Retard :Boolean ,Debut_retard:date, En_Degradation :Boolean , Debut_degradation:date)











