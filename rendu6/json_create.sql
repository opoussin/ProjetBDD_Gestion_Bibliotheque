CREATE TABLE Compte_utilisateur (
  login VARCHAR  PRIMARY KEY ,
  Mot_de_passe VARCHAR
);

CREATE TYPE genre AS ENUM ('Roman', 'Nouvelle', 'Fantastique','Science-fiction', 'Fantasy', 'Polar','Thriller', 'Roman noir', 'Biographie','Conte', 'Légende', 'Essai','Poésie', 'Manga', 'Théâtre','Aventure', 'Guerre', 'Histoire','Action', 'Comédie', 'Drame','Comédie dramatique', 'Fiction', 'Western', 'Documentaires', 'Classique','Jazz', 'Variété française', 'Variété internationale','Musiques du monde', 'Rap', 'Musique électronique','Bande dessinée','Famille','Musique de film');

CREATE TYPE role AS ENUM ('Auteur', 'Compositeur', 'Interprète','Acteur','Réalisateur');

CREATE TYPE etat AS ENUM ('Neuf', 'Bon', 'Abîmé','Perdu');

CREATE TYPE type AS ENUM ('Oeuvremusicale', 'Film', 'Livre');

CREATE TABLE Adherents(
  login VARCHAR PRIMARY KEY,
  FOREIGN KEY ( login ) REFERENCES Compte_utilisateur(login),
  Nom VARCHAR NOT NULL,
  Prenom VARCHAR NOT NULL,
  Adresse VARCHAR NOT NULL,
  Mail VARCHAR UNIQUE,
  Num_telephone INTEGER UNIQUE,
  Date_de_naissance DATE,
  Nb_retard INTEGER,
  Nb_degradation INTEGER,
  carte VARCHAR UNIQUE
);

CREATE TABLE Personnel(
  login VARCHAR,
  FOREIGN KEY ( login ) REFERENCES Compte_utilisateur(login),
  Nom VARCHAR NOT NULL,
  Prenom VARCHAR NOT NULL,
  Adresse VARCHAR NOT NULL,
  Mail VARCHAR UNIQUE
);

CREATE TABLE Adhesions(
  login VARCHAR,
  FOREIGN KEY ( login ) REFERENCES Adherents(login),
  Debut DATE NOT NULL,
  FIN DATE
);

CREATE TABLE Ressource(
  Code VARCHAR,
  Titre VARCHAR,
  Éditeur VARCHAR,
  Genre genre,
  Date_appartion INTEGER,
  Nb_exemplaire INTEGER,
  ISBN VARCHAR,
  Langue_livre VARCHAR,
  Résumé VARCHAR,
  Synopsis VARCHAR,
  Langue_film VARCHAR,
  Durée_film TIME,
  Durée_oeuvre TIME,
  Type type,
  PRIMARY KEY (Type, Code),
CHECK ((Type = 'Livre' AND ISBN is NOT NULL AND Langue_livre is NOT NULL AND Résumé is NOT NULL AND Durée_oeuvre IS NULL AND Synopsis IS NULL AND Langue_film IS NULL AND Durée_film IS NULL)
        OR (Type = 'Oeuvremusicale' AND Durée_oeuvre is NOT NULL AND ISBN IS NULL AND Langue_livre IS NULL AND Résumé IS NULL AND Synopsis IS NULL AND Langue_film IS NULL AND Durée_film IS NULL )
        OR (Type = 'Film' AND Synopsis is NOT NULL AND Langue_film is NOT NULL AND Durée_film is NOT NULL AND ISBN IS NULL AND Langue_livre IS NULL AND Résumé IS NULL AND Durée_oeuvre IS NULL ))

);

CREATE TABLE Contributeur (
  Nom VARCHAR,
  Prenom VARCHAR,
  Date_de_naissance DATE,
  PRIMARY KEY (Nom, Prenom, Date_de_naissance),
  Nationalité VARCHAR
);

CREATE TABLE Contribue (
  Rôle role,
  Code VARCHAR,
  Type type,
  Nom VARCHAR,
  Prenom VARCHAR,
  Date_de_naissance DATE,
  FOREIGN KEY ( Code, Type) REFERENCES Ressource(Code, Type),
  FOREIGN KEY ( Nom, Prenom, Date_de_naissance ) REFERENCES Contributeur(Nom,Prenom, Date_de_naissance),
  PRIMARY KEY (Rôle,Type, Code, Nom, Prenom, Date_de_naissance),
  CHECK ((Type='Livre' AND Rôle='Auteur') OR (Type='Film' AND (Rôle='Acteur' OR Rôle='Réalisateur')) OR (Type='Oeuvremusicale' AND (Rôle='Compositeur' OR Rôle='Interprète')))
);

CREATE TABLE Exemplaire(
  Clé VARCHAR PRIMARY KEY,
  Type type,
  Code VARCHAR,
  FOREIGN KEY ( Code, Type ) REFERENCES Ressource(Code, Type),
  État etat NOT NULL,
  Disponibilité BOOLEAN NOT NULL,
  compteur INTEGER NOT NULL
);

CREATE TABLE EMPRUNT (
  Clé VARCHAR,
  login VARCHAR,
  FOREIGN KEY ( Clé ) REFERENCES Exemplaire(Clé),
  FOREIGN KEY ( login ) REFERENCES Adherents(login),
  emprunt_enCours BOOLEAN NOT NULL,
  Durée_limite DATE,
  Etat_retour etat
);

CREATE TABLE Reservation (
  Clé VARCHAR,
  login VARCHAR,
  FOREIGN KEY ( Clé ) REFERENCES Exemplaire(Clé),
  FOREIGN KEY ( login ) REFERENCES Adherents(login),
  état_reservation BOOLEAN NOT NULL,
  reserv_date DATE
);

CREATE TABLE Sanction(
  Clé VARCHAR,
  login VARCHAR,
  PRIMARY KEY (Clé, login),
  FOREIGN KEY ( login ) REFERENCES Adherents(login),
  FOREIGN KEY ( Clé ) REFERENCES Exemplaire(Clé),
  En_sanction BOOLEAN NOT NULL,
  En_Retard BOOLEAN NOT NULL,
  Debut_retard DATE,
  En_Degradation BOOLEAN NOT NULL,
  Debut_degradation DATE,
CHECK ((En_Retard is true AND (Debut_retard is NOT NULL)) OR (En_Degradation is true AND (Debut_degradation is NOT NULL))),
  CHECK((En_sanction is true AND En_Retard is true) OR (En_sanction is true AND En_Degradation is true))
);


