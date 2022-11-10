CREATE TABLE Compte_utilisateur (
  PRIMARY KEY login,
  Mot_de_passe VARCHAR
);



CREATE TYPE genre AS ENUM ('Roman', 'Nouvelle', 'Fantastique','Science-fiction', 'Fantasy', 'Polar','Thriller', 'Roman noir', 'Biographie','Conte', 'Légende', 'Essai','Poésie', 'Manga', 'Théâtre','Aventure', 'Guerre', 'Histoire','Action', 'Comédie', 'Drame','Comédie dramatique', 'Fiction', 'Western', 'Documentaires', 'Classique','Jazz', 'Variété française', 'Variété internationale','Musiques du monde', 'Rap', 'Musique électronique','Bande dessinée','Famille','Musique de film');


CREATE TYPE etat AS ENUM ('Neuf', 'Bon', 'Abîmé','Perdu');

CREATE TABLE Adherents(
  FOREIGN KEY login REFERENCES Compte_utilisateur(login),
  Nom VARCHAR NOT NULL,
  Prenom VARCHAR NOT NULL,
  Adresse VARCHAR NOT NULL,
  Mail VARCHAR UNIQUE,
  Num_telephone INTEGER UNIQUE,
  Date_de_naissance DATE,
  Nb_retard INTEGER,
  Nb_degradation INTEGER,
  carte VARCHAR
);

CREATE TABLE Personnel(
  FOREIGN KEY login REFERENCES Compte_utilisateur(login),
  Nom VARCHAR NOT NULL,
  Prenom VARCHAR NOT NULL,
  Adresse VARCHAR NOT NULL,
  Mail VARCHAR UNIQUE
);

CREATE TABLE Adhesions(
  FOREIGN KEY login REFERENCES Adherents(login),
  Debut DATE NOT NULL,
  FIN DATE
);

CREATE TABLE Ressource(
  PRIMARY KEY Code INTEGER,
  Titre VARCHAR,
  Éditeur VARCHAR,
  Genre genre,
  Date_appartion DATE,
  Nb_exemplaire INTEGER,
  ISBN VARCHAR,
  Langue_livre VARCHAR,
  Résumé VARCHAR,
  Synopsis VARCHAR,
  Langue_film VARCHAR,
  Durée_film TIME,
  Durée_oeuvre TIME,
  Livre BOOLEAN,
  Film BOOLEAN,
  Oeuvremusicale BOOLEAN
  CHECK ((Livre NOT NULL AND ISBN NOT NULL AND Langue_livre NOT NULL AND Résumé NOT NULL AND Oeuvremusicale IS NULL AND Durée_oeuvre IS NULL AND Film IS NULL AND Synopsis IS NULL AND Langue_film IS NULL AND Durée_film IS NULL)
        OR (Oeuvremusicale NOT NULL AND Durée_oeuvre NOT NULL AND Livre IS NULL AND ISBN IS NULL AND Langue_livre IS NULL AND Résumé IS NULL AND Film IS NULL AND Synopsis IS NULL AND Langue_film IS NULL AND Durée_film IS NULL )
        OR (Film NOT NULL AND Synopsis NOT NULL AND Langue_film NOT NULL AND Durée_film NOT NULL AND Livre IS NULL AND ISBN IS NULL AND Langue_livre IS NULL AND Résumé IS NULL AND Oeuvremusicale IS NULL AND Durée_oeuvre IS NULL )),
);

CREATE TABLE Contributeur (
  Nom VARCHAR,
  Prenom VARCHAR,
  Date_de_naissance DATE,
  PRIMARY KEY (Rôle, Nom, Prenom, Date_de_naissance),
  Nationalité VARCHAR
);

CREATE TABLE Contribue (
  Rôle role,
  FOREIGN KEY Code REFERENCES Ressource(code),
  FOREIGN KEY Nom REFERENCES Contributeur(Nom),
  FOREIGN KEY Prenom REFERENCES Contributeur(Prenom),
  FOREIGN KEY Date_de_naissance REFERENCES Contributeur(Date_de_naissance),
);

CREATE TABLE Exemplaire(
  PRIMARY KEY Clé VARCHAR,
  FOREIGN KEY Code REFERENCES Ressource(Code),
  État etat NOT NULL,
  Disponibilité BOOLEAN ,
  compteur INTEGER NOT NULL
);

CREATE TABLE EMPRUNT (
  FOREIGN KEY Clé REFERENCES Exemplaire(Clé),
  FOREIGN KEY login REFERENCES Adherents(login),
  emprunt_enCours BOOLEAN,
   Durée_limite DATE,
  Etat_retour etat
);

CREATE TABLE Reservation (
  FOREIGN KEY Clé REFERENCES Exemplaire(Clé),
  FOREIGN KEY login REFERENCES Adherents(login),
  état_reservation BOOLEAN,
  reserv_date DATE
);

CREATE TABLE Sanction(
  FOREIGN KEY login REFERENCES Adhérents(login),
  FOREIGN KEY Clé REFERENCES Exemplaire(Clé),
  En_sanction BOOLEAN,
  En_Retard BOOLEAN,
  Debut_retard DATE,
  En_Degradation BOOLEAN,
  Debut_degradation DATE
  CHECK (En_Retard NOT NULL AND Debut_retard NOT NULL),
  CHECK(En_Degradation NOT NULL AND Debut_degradation NOT NULL),
  CHECK((En_sanction NOT NULL AND En_Retard NOT NULL) OR (En_sanction NOT NULL AND En_Degradation NOT NULL))
);

