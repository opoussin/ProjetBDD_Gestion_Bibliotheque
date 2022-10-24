Adhesions(Encours : booléen ,Début : Date, Fin: Date)

Adherents(Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str )

Personnel(Nom : char, Prenom : char ,Adresse : char ,Mail : char)

Exemplaire(État : enum,Clé : char , Disponibilités : char ,compteur : int )


Ressource(#Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int)


Compte_utilisateur( Login : int, Mot_de_passe : string)

Sanction(  , En_sanction :Boolean , Durée_sanction )

Sanction(En_sanction :Boolean )


Retard(En_Retard :Boolean ,Debut_retard:date)

Degradation(En_Degradation :Boolean , Debut_degradation:date )

Emprunt(emprunt_enCours: Boolean, Durée_limite : Date, Etat_retour : enum)

Reservation(emprunt_enCours: Boolean,reserv_date : Date)



<b>Héritage par la classee mère de la relation Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int ) avec :
- Film( Synopsis: char, Langue : char , Durée_film: time  )
- Livre( ISBN : char, Langue : char , Résumé: char )
- œuvremusicale(Durée_oeuvre: Time) </b>


Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, ISBN : char, Langue : char , Résumé: char, Synopsis: char, Langue : char , Durée_film: time, Durée_oeuvre: Time, Livre : boolean, Film: Boolean, œuvremusicale= Boolean )
Contraintes:
- NOT (Livre AND Synopsis, Langue , Durée_film, Durée_oeuvre )
- NOT (Film AND ISBN , Langue, Résumé, Durée_oeuvre )
- NOT (œuvremusicale AND ISBN , Langue, Résumé, Synopsis, Langue , Durée_film )
- Livre AND ISBN , Langue, Résumé
- Film AND Synopsis, Langue , Durée_film
- œuvremusicale AND Durée_oeuvre
- Film OR Livre OR œuvremusicale


Contraintes : on devra vérifier que les nullités et non nullités de c, d, e et f en fonction du type t (cela peut se faire grâce à un CHECK en SQL)



<b> Relation entre Contributeur et Ressource </b>

Contributeur( Rôle :char, Nom :char, Prenom :char, Date_de_naissance:Date , Nationalité: char) 
Contribue_livre(#Rôle =>Contributeur, #Code=>Livre ) 
Contribue_film(#Rôle =>Contributeur, #Code=>Film ) 
Contribue_musique(#Rôle =>Contributeur, #Code=>œuvremusicale ) 
