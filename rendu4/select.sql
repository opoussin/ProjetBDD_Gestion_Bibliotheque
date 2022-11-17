// Qui a contribué au film La haine ?

SELECT Contribue.nom, Contribue.prenom, Contribue.rôle
FROM Contribue INNER JOIN Ressource ON Contribue.code = Ressource.code
WHERE Ressource.titre='La haine'

// Quels sont les adhérents qui ont adhéré apres le 12 novembre 2022 ?

SELECT Adherents.nom, Adherents.prenom
FROM Adhesions INNER JOIN Adherents ON Adhesions.login = Adherents.login
WHERE Adhesions.debut > '2022-11-12'

// Quels sont les personnes qui ont publié une oeuvre en même 1994 ?

SELECT C.Nom, C.Prenom
FROM Contribue C JOIN Ressource R ON C.Code = R.Code
WHERE R.Date_appartion = '1994'