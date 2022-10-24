Adhesions(Encours : booléen ,Début : Date, Fin: Date)

Adherents(Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, carte : str )

Personnel(Nom : char, Prenom : char ,Adresse : char ,Mail : char)

Exemplaire(État : enum,Clé : char , Disponibilités : char ,compteur : int )


Ressource(#Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int)


Compte_utilisateur( Login : int, Mot_de_passe : string)

Sanction( Nb_retard, Nb_degradation , En_sanction :Boolean , Durée_sanction )

Emprunt_en_cours(Durée_limite : Date, Etat_retour : enum)

Contributeurs( Rôle :char, Nom :char, Prenom :char, Date_de_naissance:Date , Nationalité: char) 


<b>Héritage par les classes filles de la relation Ressource - Film,Livre,OeuvreMusicale : </b>

Livre( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, ISBN : char, Langue : char , Résumé: char )

Film( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, Synopsis: char, Langue : char , Durée_film: time  ) avec 

œuvremusicale( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int ,Durée_oeuvre: Time)

Contrainte : INTERSECTION (PROJECTION(Livre,Code), PROJECTION(Film,Code), PROJECTION(œuvremusicale,Code)) = {}

<b> Relation entre Contributeur et Film, Livre, œuvremusicale </b>

Contributeur( Rôle :char, Nom :char, Prenom :char, Date_de_naissance:Date , Nationalité: char) 
Contribue_livre(#Rôle =>Contributeur, #Code=>Livre ) 
Contribue_film(#Rôle =>Contributeur, #Code=>Film ) 
Contribue_musique(#Rôle =>Contributeur, #Code=>œuvremusicale ) 
