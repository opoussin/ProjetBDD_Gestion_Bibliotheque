INSERT INTO Compte_utilisateur VALUES ('apommep', 'arnaudpp');
INSERT INTO Compte_utilisateur VALUES ('pduranta', 'durantpa');
INSERT INTO Compte_utilisateur VALUES ('agatheo', 'orangecompi');
INSERT INTO Compte_utilisateur VALUES ('denised', 'dumasdenise');
INSERT INTO Compte_utilisateur VALUES ('arthurdr', 'papableu');
INSERT INTO Compte_utilisateur VALUES ('juleskin', 'gateau05');

INSERT INTO Adherents VALUES ('pduranta', 'durant', 'pierre', '7 Pl. de l Ancien Hôpital, 60200 Compiègne ', 'pierred@gmail.com', 0606065487 , '1988-06-06', 0,0, 'crap02');
INSERT INTO Adherents VALUES ('agatheo', 'orange', 'agathe', '13 Rue Winston Churchill, 60200 Compiègne ', 'agatheorange@gmail.com', 0785652544 , '2000-10-26', 0,0, 'crap01');
INSERT INTO Adherents VALUES ('arthurdr', 'drome', 'arthur', '17 Rue Winston Churchill, 60200 Compiègne ', 'dromearth@gmail.com', 0685651525 , '2001-01-17', 0,0, 'crap00');
INSERT INTO Adherents VALUES ('juleskin', 'kimp', 'jules', '12 All. des Avenues, 60200 Compiègne', 'juleskin@orange.com', 0752652530 , '1967-04-11', 0,0, 'crap03');

INSERT INTO Personnel VALUES ('apommep', 'pomme', 'arnaud', '8 Imp. de la Menardière 60200 Compiegne', 'arpomme@gmail.com');
INSERT INTO Personnel VALUES ('denised', 'dumas', 'denise', '2-4 All. des Étangs, 60350 Vieux-Moulin', 'denisedumas@gmail.com');

INSERT INTO Adhesions VALUES ('pduranta', '2020-5-4', '2022-5-16');
INSERT INTO Adhesions VALUES ('agatheo', '2021-8-13', '2023-8-17');
INSERT INTO Adhesions VALUES ('arthurdr', '2021-8-13', '2023-8-17');
INSERT INTO Adhesions VALUES ('juleskin', '2022-12-15', NULL);

INSERT INTO Ressource VALUES ('L1','Les Fleurs du Mal', 'Pierre Brunel', 'Poésie', 1868,3, '9782702182888', 'Français', 'recueil de poèmes de Charles Baudelaire reprenant la quasi-totalité de sa production en vers de 1840 jusque sa mort survenue fin août 1867',NULL,NULL,NULL,NULL, 'Livre','[{"Clé":"L1_01","Type":"Livre","Code":"L1","État":"Neuf","Disponibilité":True,"compteur":0},{"Clé":"L1_02","Type":"Livre","Code":"L1","État":"Bon","Disponibilité":True,"compteur":0},{"Clé":"L1_03","Type":"Livre","Code":"L1","État":"Bon","Disponibilité":True,"compteur":0}]');


INSERT INTO Ressource VALUES ('L2','L''étranger', 'Gallimard', 'Roman', 1942,2, '9782070360024', 'Français', 'Condamné à mort, Meursault. Sur une plage algérienne, il a tué un Arabe. À cause du soleil, dira-t-il, parce qu''il faisait chaud. On n''en tirera rien d''autre. Rien ne le fera plus réagir : ni l''annonce de sa condamnation, ni la mort de sa mère, ni les paroles du prêtre avant la fin. Comme si, sur cette plage, il avait soudain eu la révélation de l''universelle équivalence du tout et du rien.
La conscience de n''être sur la terre qu''en sursis, d''une mort qui, quoi qu''il arrive, arrivera, sans espoir de salut. Et comment être autre chose qu''indifférent à tout après ça ?',NULL,NULL,NULL,NULL, 'Livre', '[{"Clé":"L2_01","Type":"Livre","Code":"L2","État":"Bon","Disponibilité":True,"compteur":0},{"Clé":"L2_02","Type":"Livre","Code":"L2","État":"Bon","Disponibilité":True,"compteur":0}]');

INSERT INTO Ressource VALUES ('L3','Les Misérables', 'Ldp jeunesse', 'Roman', 1862,4, '2010008995', 'Français', 'Le destin de Jean Valjean, forçat échappé du bagne, est bouleversé par sa rencontre avec Fantine. Mourante et sans le sou, celle-ci lui demande de prendre soin de Cosette, sa fille confiée aux Thénardier. Ce couple d’aubergistes, malhonnête et sans scrupules, exploitent la fillette jusqu’à ce que Jean Valjean tienne sa promesse et l’adopte. Cosette devient alors sa raison de vivre. Mais son passé le rattrape et l’inspecteur Javert le traque…',NULL,NULL,NULL,NULL, 'Livre','[{"Clé":"L3_01","Type":"Livre","Code":"L3","État":"Bon","Disponibilité":True,"compteur":0},{"Clé":"L3_02","Type":"Livre","Code":"L3","État":"Bon","Disponibilité":True,"compteur":0},{"Clé":"L3_03","Type":"Livre","Code":"L1","État":"Bon","Disponibilité":True,"compteur":0},{"Clé":"L3_04","Type":"Livre","Code":"L3","État":"Bon","Disponibilité":True,"compteur":0}]');


INSERT INTO Ressource VALUES ('L4','Das Parfum', 'Diogenes Verlag', 'Roman', 1985,3,'3257228007','Allemand','Die spannende Geschichte - märchenhaft, witzig und zugleich fürchterlich angsteinflössend - vom finsteren Helden Grenouille. 2006 von Tom Tykwer mit Ben Whishaw, Dustin Hoffman, Alan Rickman und Rachel Hurd-Wood in den Hauptrollen verfilmt.',NULL,NULL,NULL,NULL, 'Livre','[{"Clé":"L4_01","Type":"Livre","Code":"L4","État":"Bon","Disponibilité":True,"compteur":0},{"Clé":"L4_02","Type":"Livre","Code":"L4","État":"Bon","Disponibilité":True,"compteur":0},{"Clé":"L4_03","Type":"Livre","Code":"L4","État":"Bon","Disponibilité":True,"compteur":0}]');




INSERT INTO Ressource VALUES ('F1','La haine', NULL, 'Drame', 1995,1, NULL, NULL, NULL,'Abdel Ichah, seize ans est entre la vie et la mort, passé à tabac par un inspecteur de police lors d''un interrogatoire. Une émeute oppose les jeunes d''une cité HLM aux forces de l''ordre. Pour trois d''entre eux, ces heures vont marquer un tournant dans leur vie...','Français','1:38:00',NULL, 'Film','[{"Clé":"F1_01","Type":"Film","Code":"F1","État":"Neuf","Disponibilité":True,"compteur":0}]');

INSERT INTO Ressource VALUES ('F2','Pulp Fiction', NULL, 'Thriller', 1994,1, NULL, NULL, NULL,'L''odyssée sanglante et burlesque de petits malfrats dans la jungle de Hollywood à travers trois histoires qui s''entremêlent.','Français','2:29:00',NULL, 'Film','[{"Clé":"F2_01","Type":"Film","Code":"F2","État":"Neuf","Disponibilité":True,"compteur":0}]');

INSERT INTO Ressource VALUES ('F3','La Cité de la peur', NULL, 'Comédie', 1994,3, NULL, NULL, NULL,'De nos jours, à Cannes, pendant le Festival. Pas facile pour Odile Deray, petite attachée de presse de cinéma, de faire parler de son film "Red is Dead". Il faut avouer qu''il s''agit d''un film d''horreur de série Z, un petit budget aux acteurs improbables. Pourtant un jour, la chance sourit à Odile : un tueur commet des meurtres exactement de la même manière que dans son film, l''occasion est trop belle : de vrais meurtres, comme dans son film, en plein Festival de Cannes ! Comme publicité, on ne peut pas rêver mieux..','Français','1:40:00',NULL, 'Film','[{"Clé":"F3_01","Type":"Film","Code":"F3","État":"Neuf","Disponibilité":True,"compteur":0},{"Clé":"F3_02","Type":"Film","Code":"F3","État":"Neuf","Disponibilité":True,"compteur":0},{"Clé":"F3_03","Type":"Film","Code":"F3","État":"Neuf","Disponibilité":True,"compteur":0}]');

INSERT INTO Ressource VALUES ('F4','Le Fabuleux Destin d’’Amélie Poulain', NULL, 'Comédie', 2001,2, NULL, NULL, NULL,'Amélie, une jeune serveuse dans un bar de Montmartre, passe son temps à observer les gens et à laisser son imagination divaguer. Elle s’’est fixé un but : faire le bien de ceux qui l''entourent. Elle invente alors des stratagèmes pour intervenir incognito dans leur existence. Le chemin d''Amélie est jalonné de rencontres : Georgette, la buraliste hypocondriaque ; Lucien, le commis d''épicerie ; Madeleine Wallace, la concierge portée sur le porto et les chiens empaillés ; Raymond Dufayel alias « l''homme de verre", son voisin qui ne vit qu''à travers une reproduction d''un tableau de Renoir.','Français','2:00:00',NULL, 'Film','[{"Clé":"F4_01","Type":"Film","Code":"F4","État":"Neuf","Disponibilité":True,"compteur":0},{"Clé":"F4_02","Type":"Film","Code":"F4","État":"Neuf","Disponibilité":True,"compteur":0}]');


INSERT INTO Ressource VALUES ('OM1','Requiem', NULL, 'Classique', 1793,2, NULL, NULL, NULL,NULL,NULL,NULL,'1:00:30', 'Oeuvremusicale','[{"Clé":"OM1_01","Type":"Oeuvremusicale","Code":"OM1","État":"Neuf","Disponibilité":True,"compteur":0},{"Clé":"OM1_02","Type":"Oeuvremusicale","Code":"OM1","État":"Neuf","Disponibilité":True,"compteur":0}]');




INSERT INTO Ressource VALUES ('OM2','Les 4 Saisons', NULL, 'Classique', 1725,1, NULL, NULL, NULL,NULL,NULL,NULL,'0:53:00', 'Oeuvremusicale','[{"Clé":"OM2_01","Type":"Oeuvremusicale","Code":"OM2","État":"Neuf","Disponibilité":True,"compteur":0}]');


INSERT INTO Ressource VALUES ('OM3','Marche hongroise', NULL, 'Classique', 1824,1, NULL, NULL, NULL,NULL,NULL,NULL,'0:43:00', 'Oeuvremusicale');

INSERT INTO Contributeur VALUES ('Baudelaire','Charles', '1821-04-09','français');
INSERT INTO Contributeur VALUES ('Camus','Albert', '1913-11-07','français');
INSERT INTO Contributeur VALUES ('Hugo','Victor', '1802-02-26','français');
INSERT INTO Contributeur VALUES ('Süskind','Patrick', '1949-03-26','Allemande');
INSERT INTO Contributeur VALUES ('Kassovitz','Mathieu ', '1967-08-03','français');
INSERT INTO Contributeur VALUES ('Cassel','Vincent', '1966-11-23','français');
INSERT INTO Contributeur VALUES ('Tarantino','Quentin', '1963-03-27','Américain');
INSERT INTO Contributeur VALUES ('Berberian','Alain', '1953-07-02','français');
INSERT INTO Contributeur VALUES ('Chabat','Alain', '1958-11-24','français');
INSERT INTO Contributeur VALUES ('Jeunet','Jean-Pierre', '1953-09-03','français');
INSERT INTO Contributeur VALUES ('Mozart','Wolfgang Amadeus', '1756-01-27','autrichien');
INSERT INTO Contributeur VALUES ('Vivaldi','Antonio Lucio', '1678-03-04','italien');

INSERT INTO Contribue  VALUES ('Auteur','L1','Livre','Baudelaire','Charles', '1821-04-09');
INSERT INTO Contribue  VALUES ('Auteur','L2','Livre','Camus','Albert', '1913-11-07');
INSERT INTO Contribue  VALUES ('Auteur','L3','Livre','Hugo','Victor', '1802-02-26');
INSERT INTO Contribue  VALUES ('Auteur','L4','Livre','Süskind','Patrick', '1949-03-26');
INSERT INTO Contribue  VALUES ('Réalisateur','F1','Film','Kassovitz','Mathieu ', '1967-08-03');
INSERT INTO Contribue  VALUES ('Acteur','F1','Film','Cassel','Vincent', '1966-11-23');
INSERT INTO Contribue  VALUES ('Réalisateur','F2','Film','Tarantino','Quentin', '1963-03-27');
INSERT INTO Contribue  VALUES ('Réalisateur','F3','Film','Berberian','Alain', '1953-07-02');
INSERT INTO Contribue  VALUES ('Acteur','F3','Film','Chabat','Alain', '1958-11-24');
INSERT INTO Contribue  VALUES ('Réalisateur','F4','Film','Jeunet','Jean-Pierre', '1953-09-03');
INSERT INTO Contribue  VALUES ('Compositeur','OM1','Oeuvremusicale','Mozart','Wolfgang Amadeus', '1756-01-27');
INSERT INTO Contribue  VALUES ('Compositeur','OM2','Oeuvremusicale','Vivaldi','Antonio Lucio', '1678-03-04');







