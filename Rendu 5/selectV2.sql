/*Qui a contribué au film La haine ?*/

SELECT Contribue.nom, Contribue.prenom, Contribue.rôle
FROM Contribue INNER JOIN Ressource ON Contribue.code = Ressource.code
WHERE Ressource.titre='La haine';

/*Quels sont les adhérents qui ont adhéré apres le 12 novembre 2022 */

SELECT Adherents.nom, Adherents.prenom
FROM Adhesions INNER JOIN Adherents ON Adhesions.login = Adherents.login
WHERE Adhesions.debut > '2022-11-12';

/* Quels sont les personnes qui ont publié une oeuvre en même 1994 ?*/

SELECT C.Nom, C.Prenom
FROM Contribue C JOIN Ressource R ON C.Code = R.Code
WHERE R.Date_appartion = '1994';

/*VUES POUR BD*/

/* View pour vérification que le login existe dans la base de donnée */
CREATE VIEW ExistenceLogin AS
SELECT login 
FROM Adherents  UNION SELECT login FROM Personnel ;

/* View pour vérification que le login existe dans la table Adherents */
CREATE VIEW LoginAdherent AS
SELECT login 
FROM Adherents;

/* jointure ressource _ Exemplaire */
CREATE VIEW RessourceExemplaire AS
SELECT Ressource.Titre, Exemplaire.Clé 
FROM Ressource INNER JOIN Exemplaire ON Ressource.Code=Exemplaire.Code ;

/* Compte le nombre d'exemplaire disponible  */
CREATE VIEW CompteExemplaire AS
SELECT Ressource.Titre, COUNT(Exemplaire.Disponibilité) 
FROM Ressource INNER JOIN Exemplaire ON Ressource.Code=Exemplaire.Code 
WHERE Exemplaire.Disponibilité=true 
GROUP BY Ressource.Titre;

/* View pour consulter un adhérent */
CREATE VIEW ConsultationAdherent AS
SELECT Adherents.login,Adherents.Nom ,Adherents.Prenom ,Adherents.Adresse ,Adherents.Mail,Adherents.Num_telephone,Adherents.Date_de_naissance ,Adherents.Nb_retard ,Adherents.Nb_degradation,Adherents.carte,Adhesions.Debut,Adhesions.FIN, EMPRUNT.emprunt_enCours, Reservation.état_reservation, Sanction.En_sanction 
FROM (((Adherents INNER JOIN Adhesions ON Adherents.login= Adhesions.login)INNER JOIN EMPRUNT ON EMPRUNT.login=Adhesions.login)INNER JOIN Reservation ON Reservation.login=Adhesions.login)INNER JOIN Sanction ON Sanction.login=Adhesions.login ;

/* Afficher la liste des emprunts en cours */
CREATE VIEW EmpruntEnCours AS
SELECT Clé, login 
FROM EMPRUNT 
WHERE emprunt_enCours = true;

/*Views pour avoir les personnes en cours de sanction*/
CREATE VIEW PersonneSanction AS
SELECT S.En_sanction 
FROM Sanction S JOIN Adherents A ON S.login = A.login ;

/*Views pour avoir les personnes en cours de sanction*/
CREATE VIEW HistoriqueEmprunt AS
SELECT * 
FROM Emprunt E Join Adherents A ON E.login = A.login ;

/*Views pour les statistiques, recommendations*/
CREATE VIEW statistiques AS
SELECT MAX(COUNT(Genre)) 
FROM Ressource R Join Exemplaire E ON R.Code = A.Code 
GROUP BY Genre;

CREATE VIEW statistiques2 AS
SELECT MAX(COUNT(Genre)) 
FROM Ressource R Join Exemplaire E ON R.Code = A.Code 
GROUP BY Genre;
/*now, à chaque fois on rejoute le login pour rajouter une condition WHERE dans le code python et pouvoir sélectionner à partir du login ce que l'on recherche*/

CREATE VIEW Genre1 AS 
SELECT Code, Clé, login
FROM Emprunt JOIN Exemplaire ON Emprunt.Clé = Exemplaire.Clé


CREATE VIEW Genre2 AS 
SELECT Genre, Clé, login
FROM Genre1 Join Ressource ON Genre1.Code = Ressource.Code

/* On compte le nombre d'exemplaire emprunté avec le même genre*/
CREATE VIEW Genre3 AS 
SELECT login, Genre, COUNT(Clé) 
FROM Genre2
GROUP BY Genre 

/*On cherche le Max de la tables ensuite dans le python*/
CREATE VIEW Genre4 AS
SELECT login, MAX(COUNT(Clé))
FROM Genre3

/* Stats par auteurs ? */





/*
CREATE VIEW statistiques3 AS
SELECT AVG() 
FROM Ressource R Join Exemplaire E ON R.Code = A.Code 
GROUP BY Genre;*/

