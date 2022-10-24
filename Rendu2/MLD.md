Adhesions(Encours : booléen ,Début : Date, Fin: Date)

Adherents(Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, carte : str )

Personnel(Nom : char, Prenom : char ,Adresse : char ,Mail : char)

Exemplaire(État : enum,Clé : char , Disponibilités : char ,compteur : int )


Ressource(#Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int)


Compte_utilisateur( Login : int, Mot_de_passe : string)

Sanction( Nb_retard, Nb_degradation , En_sanction :Boolean , Durée_sanction )

Emprunt_en_cours(Durée_limite : Date, Etat_retour : enum)

Contributeurs( Rôle :char, Nom :char, Prenom :char, Date_de_naissance:Date , Nationalité: char) 
Ressource( Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int)

Livre( ISBN : char, Langue : char , Résumé: char )

Film( Synopsis: char, Langue : char , Durée_film: time  )

œuvremusicale(Durée_oeuvre: Time)