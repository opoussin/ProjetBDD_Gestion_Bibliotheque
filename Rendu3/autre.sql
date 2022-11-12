INSERT INTO Ressource VALUES ('L1','Les Fleurs du Mal', 'Pierre Brunel', 'Poésie', '1868','3', '9782702182888', 'Français', 'recueil de poèmes de Charles Baudelaire reprenant la quasi-totalité de sa production en vers de 1840 jusque sa mort survenue fin août 1867','NULL','NULL','NULL','NULL', 'Livre');

INSERT INTO Ressource VALUES ('L2','L''étranger', 'Gallimard', 'Roman', '1942','2', '9782070360024', 'Français', 'Condamné à mort, Meursault. Sur une plage algérienne, il a tué un Arabe. À cause du soleil, dira-t-il, parce qu''il faisait chaud. On n''en tirera rien d''autre. Rien ne le fera plus réagir : ni l''annonce de sa condamnation, ni la mort de sa mère, ni les paroles du prêtre avant la fin. Comme si, sur cette plage, il avait soudain eu la révélation de l''universelle équivalence du tout et du rien.
La conscience de n''être sur la terre qu''en sursis, d''une mort qui, quoi qu''il arrive, arrivera, sans espoir de salut. Et comment être autre chose qu''indifférent à tout après ça ?','NULL','NULL','NULL','NULL', 'Livre');

INSERT INTO Ressource VALUES ('L3','Les Misérables', 'Ldp jeunesse', 'Roman', '1862','4', '2010008995', 'Français', 'Le destin de Jean Valjean, forçat échappé du bagne, est bouleversé par sa rencontre avec Fantine. Mourante et sans le sou, celle-ci lui demande de prendre soin de Cosette, sa fille confiée aux Thénardier. Ce couple d’aubergistes, malhonnête et sans scrupules, exploitent la fillette jusqu’à ce que Jean Valjean tienne sa promesse et l’adopte. Cosette devient alors sa raison de vivre. Mais son passé le rattrape et l’inspecteur Javert le traque…','NULL','NULL','NULL','NULL', 'Livre');

INSERT INTO Ressource VALUES ('L4','Das Parfum', 'Diogenes Verlag', 'Roman', '1985','3','3257228007','Allemand','Die spannende Geschichte - märchenhaft, witzig und zugleich fürchterlich angsteinflössend - vom finsteren Helden Grenouille. 2006 von Tom Tykwer mit Ben Whishaw, Dustin Hoffman, Alan Rickman und Rachel Hurd-Wood in den Hauptrollen verfilmt.','NULL','NULL','NULL','NULL', 'Livre');

INSERT INTO Ressource VALUES ('F1','La haine', 'NULL', 'Drame', '1995','1', 'NULL', 'NULL', 'NULL','Abdel Ichah, seize ans est entre la vie et la mort, passé à tabac par un inspecteur de police lors d’'un interrogatoire. Une émeute oppose les jeunes d'une cité HLM aux forces de l''ordre. Pour trois d''entre eux, ces heures vont marquer un tournant dans leur vie...','Français','1:38:00','NULL', 'Film');

INSERT INTO Ressource VALUES ('F2','Pulp Fiction', 'NULL', 'Thriller', '1994','1', 'NULL', 'NULL', 'NULL','L''odyssée sanglante et burlesque de petits malfrats dans la jungle de Hollywood à travers trois histoires qui s''entremêlent.','Français','2:29:00','NULL', 'Film');

INSERT INTO Ressource VALUES ('F3','La Cité de la peur', 'NULL', 'Comédie', '1994','3', 'NULL', 'NULL', 'NULL','De nos jours, à Cannes, pendant le Festival. Pas facile pour Odile Deray, petite attachée de presse de cinéma, de faire parler de son film "Red is Dead". Il faut avouer qu''il s''agit d''un film d''horreur de série Z, un petit budget aux acteurs improbables. Pourtant un jour, la chance sourit à Odile : un tueur commet des meurtres exactement de la même manière que dans son film, l''occasion est trop belle : de vrais meurtres, comme dans son film, en plein Festival de Cannes ! Comme publicité, on ne peut pas rêver mieux..','Français','1:40:00','NULL', 'Film');

INSERT INTO Ressource VALUES ('F4','Le Fabuleux Destin d’’Amélie Poulain', 'NULL', 'Comédie', '2001','2', 'NULL', 'NULL', 'NULL','Amélie, une jeune serveuse dans un bar de Montmartre, passe son temps à observer les gens et à laisser son imagination divaguer. Elle s’’est fixé un but : faire le bien de ceux qui l''entourent. Elle invente alors des stratagèmes pour intervenir incognito dans leur existence. Le chemin d''Amélie est jalonné de rencontres : Georgette, la buraliste hypocondriaque ; Lucien, le commis d''épicerie ; Madeleine Wallace, la concierge portée sur le porto et les chiens empaillés ; Raymond Dufayel alias « l''homme de verre", son voisin qui ne vit qu''à travers une reproduction d''un tableau de Renoir.','Français','2:00:00','NULL', 'Film');

INSERT INTO Ressource VALUES ('OM1','Requiem', 'NULL', 'Classique', '1793','2', 'NULL', 'NULL', 'NULL','NULL','NULL','NULL','1:00:30', 'Oeuvremusicale');

INSERT INTO Ressource VALUES (‘OM1’,’Les 4 Saisons', ‘NULL', 'Classique', '1725','1', 'NULL', 'NULL', 'NULL','NULL','NULL','NULL','0:53:00', 'Oeuvremusicale');

INSERT INTO Exemplaire VALUES (Clé VARCHAR PRIMARY KEY, Type type, Code INTEGER, État etat NOT NULL,Disponibilité BOOLEAN NOT NULL , compteur INTEGER NOT NULL)

INSERT INTO Exemplaire VALUES ('L1_01', 'Livre', 'L1', 'neuf',true , 3);
INSERT INTO Exemplaire VALUES ('L1_02', 'Livre', 'L1', 'bon',true , 3);
INSERT INTO Exemplaire VALUES ('L1_03', 'Livre', 'L1', 'bon',true , 3);

INSERT INTO Exemplaire VALUES ('L2_01', 'Livre', 'L2', 'bon',true , 2);
INSERT INTO Exemplaire VALUES ('L2_02', 'Livre', 'L2', 'bon',true , 2);

INSERT INTO Exemplaire VALUES ('L3_01', 'Livre', 'L3', 'bon',true , 4);
INSERT INTO Exemplaire VALUES ('L3_02', 'Livre', 'L3', 'bon',true , 4);
INSERT INTO Exemplaire VALUES ('L3_03', 'Livre', 'L3', 'bon',true , 4);
INSERT INTO Exemplaire VALUES ('L3_04', 'Livre', 'L3', 'bon',true , 4);

INSERT INTO Exemplaire VALUES ('L4_01', 'Livre', 'L4', 'bon',true , 3);
INSERT INTO Exemplaire VALUES ('L4_02', 'Livre', 'L4', 'bon',true , 3);
INSERT INTO Exemplaire VALUES ('L4_03', 'Livre', 'L4', 'bon',true , 3);

INSERT INTO Exemplaire VALUES ('F1_01', 'Film', 'F1', 'neuf',true , 1);

INSERT INTO Exemplaire VALUES ('F2_01', 'Film', 'F2', 'neuf',true , 1);

INSERT INTO Exemplaire VALUES ('F3_01', 'Film', 'F3', 'neuf',true , 3);
INSERT INTO Exemplaire VALUES ('F3_02', 'Film', 'F3', 'neuf',true , 3);
INSERT INTO Exemplaire VALUES ('F3_03', 'Film', 'F3', 'neuf',true , 3);


INSERT INTO Exemplaire VALUES ('F4_01', 'Film', 'F4', 'neuf',true , 2);
INSERT INTO Exemplaire VALUES ('F4_02', 'Film', 'F4', 'neuf',true , 2);

INSERT INTO Exemplaire VALUES ('OM1_01', 'Oeuvremusicale', 'OM1', 'neuf',true , 2);
INSERT INTO Exemplaire VALUES ('OM1_02', 'Oeuvremusicale', 'OM1', 'neuf',true , 2);

INSERT INTO Exemplaire VALUES ('OM2_01', 'Oeuvremusicale', 'OM2', 'neuf',true , 1);


