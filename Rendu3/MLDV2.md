# MLD 1ère Version : 

## Relation entre Adherents et Compte_utilisateur:
<br>

**Rappel :** Adherents(Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ); et Compte_utilisateur( Login : int, Mot_de_passe : string):

    Adherents(#login=>Compte_utilisateur, Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str )

**Contraintes**
- Num_telephone UNIQUE
- Mail UNIQUE
- Nom, Prenom, Adresse, Date_de_naissance NOT NULL

<br>

## Relation entre Personnel et Compte_utilisateur:
<br>

**Rappel :** Personnel(Nom : char, Prenom : char ,Adresse : char ,Mail : char) et Compte_utilisateur( Login : int, Mot_de_passe : string):

    Personnel(#login=>Compte_utilisateur, Nom : char, Prenom : char ,Adresse : char ,Mail : char)

**Contraintes**
- Mail UNIQUE
- Nom, Prenom, Adresse NOT NULL

## Relation entre Adherents et Adhesions
<br>

**Rappel :** Adherents(Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ); et Adhesions(Début : Date, Fin: Date)

    Adhesions(#login=>Adherents, Début : Date, Fin: Date)

**Contraintes**
- Début NOT NULL

## Héritage par la classe mère de la relation Ressource; Film, Livre, œuvremusicale

Nous avons choisi de faire un héritage par classe mère car la classe Ressource est en association avec la classe Contributeur et les classes filles Livre, œuvremusicale et Film ne sont liées à aucune autre Classe. 

**Rappel :** Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int ) avec : Film( Synopsis: char, Langue : char , Durée_film: time  ) ; Livre( ISBN : char, Langue : char , Résumé: char ) ; œuvremusicale(Durée_oeuvre: Time)

    Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, ISBN : char, Langue : char , Résumé: char, Synopsis: char, Langue : char , Durée_film: time, Durée_oeuvre: Time, Livre : boolean, Film: Boolean, œuvremusicale= Boolean )

**Contraintes:**
- NOT (Livre AND Synopsis, Langue , Durée_film, Durée_oeuvre )
- NOT (Film AND ISBN , Langue, Résumé, Durée_oeuvre )
- NOT (œuvremusicale AND ISBN , Langue, Résumé, Synopsis, Langue , Durée_film )
- Livre AND ISBN , Langue, Résumé
- Film AND Synopsis, Langue , Durée_film
- œuvremusicale AND Durée_oeuvre
- Film OR Livre OR œuvremusicale


## Relation entre Contributeur et Ressource 
<br>

Contributeur(#Rôle :char, #Nom :char, #Prenom :char, #Date_de_naissance:Date , Nationalité: char) 

Contribue(#Rôle =>Contributeur, #Nom :char, #Prenom :char, #Date_de_naissance:Date, #Code=>Ressource ) 

## Composition entre Exemplaire et Ressource 
<br>

**Rappel :** Exemplaire(État : enum,Clé : char , Disponibilités : Boolean ,compteur : int )et Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, ISBN : char, Langue : char , Résumé: char, Synopsis: char, Langue : char , Durée_film: time, Durée_oeuvre: Time, Livre : boolean, Film: Boolean, œuvremusicale= Boolean )

    Ressource( #Code :int , Titre :char, Éditeur :char, Genre : enum, Date_appartion :Date, Nb_exemplaire : int, ISBN : char, Langue : char , Résumé: char, Synopsis: char, Langue : char , Durée_film: time, Durée_oeuvre: time, Livre : boolean, Film: boolean, œuvremusicale= boolean )

    Exemplaire(#Clé : char , #Code =>Ressource, État : enum, Disponibilité : boolean ,compteur : int )

**Contraintes**
- État, compteur NOT NULL

## Relation entre Emprunt, Reservation, Adherents, et Exemplaire 
<br>

**Rappel :** Emprunt(emprunt_enCours: Boolean, Durée_limite : date, Etat_retour : enum), Reservation(état_reservation: boolean,reserv_date : Date), Adherents(#login=>Compte_utilisateur, Nom : char, Prenom : char , Adresse : char ,Mail : char,Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ), et Exemplaire(#Clé : char , #Code =>Ressource, État : enum, Disponibilité : char ,compteur : int )


    Emprunt(#Clé=>Exemplaire, #login=>Adherents, emprunt_enCours: Boolean, Durée_limite : Date, Etat_retour : enum)
    Reservation(#Clé=>Exemplaire, #login=>Adherents,état_reservation: Boolean,reserv_date : Date)


## Héritage par la classe mère de la relation Sanction avec Retard et Degradation:   
<br>

Nous avons choisi de faire un héritage par classe mère car la classe Sanction est une classe d'association entre Emprunt et Adhérent  et les classes filles Retard et Dégradation ne sont liées à aucune autre classe. 

**Rappel :** Sanction(En_sanction :Boolean ) avec Retard(En_Retard : Boolean,Debut_retard:date) et Degradation(En_Degradation :Boolean , Debut_degradation:date ): 

    Sanction(En_sanction :Boolean, En_Retard :Boolean, Debut_retard : date, En_Degradation : Boolean, Debut_degradation : date)

**Contraintes**
- En_Retard AND Debut_Retard
- En_Degradation AND Debut_degradation
- (En_sanction AND En_Retard) OR (En_sanction AND En_Degradation)

## Relation entre Emprunt; Adherents et Sanction
<br>

**Rappel :** Emprunt(emprunt_enCours: Boolean, Durée_limite : Date, Etat_retour : enum) ; Adherents(#login=>Compte_utilisateur, Nom : char, Prenom : char, Adresse : char, Mail : char, Num_telephone : int, Date_de_naissance : Date, Nb_retard : int, Nb_degradation: int, carte : str ); et Sanction(En_sanction :Boolean, En_Retard :Boolean,Debut_retard:date, En_Degradation : Boolean, Debut_degradation : date)
    
    Sanction(#login=>Adhérents, #Clé=>Exemplaire, En_sanction :Boolean, En_Retard :Boolean, Debut_retard:date, En_Degradation :Boolean, Debut_degradation:date)

**Contraintes**
- En_Retard AND Debut_Retard
- En_Degradation AND Debut_degradation
- (En_sanction AND En_Retard) OR (En_sanction AND En_Degradation)










