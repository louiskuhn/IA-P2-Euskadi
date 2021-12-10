USE JunkFood_2021;

/*a. Extraire le nombre d’employés dans le département du 64 (Colonne 1 : nombre d’employés)*/
SELECT COUNT(*) AS NbEmp64en2021 FROM History h
INNER JOIN Restaurants r ON h.resto_id = r.id
INNER JOIN Pays p ON r.pays_id = p.id
WHERE pays='France' AND code_postal LIKE '64%' AND annee = 2021;


/*b. Extraire l’ingrédient le plus utilisé dans chaque département. (Colonne 1 : département, Colonne 2 : ingrédient, Colonne 3 : Utilisation ingrédient)*/
SELECT DISTINCT * FROM
(SELECT SUBSTR(r.code_postal,1,2) AS dpt, i.nom, SUM(oi.quantite * r2.unites) AS quantite_tot_ing
FROM Restaurants r
INNER JOIN Orders o ON o.resto_id = r.id 
INNER JOIN Orders_items oi ON oi.order_id = o.id
LEFT JOIN Menus m ON m.id = oi.item_id
LEFT JOIN Recettes r2 ON m.plat = r2.item_id
	OR m.dessert = r2.item_id
	OR m.boisson = r2.item_id
	OR oi.item_id = r2.item_id
LEFT JOIN Ingredients i ON i.id = r2.ing_id 
GROUP BY dpt, r2.ing_id
ORDER BY dpt, quantite_tot_ing DESC) AS tmp
GROUP BY dpt;

/*c. Extraire le restaurant ayant la masse salariale la moins importante (somme des salaires) (Colonne 1 : Restaurant, Colonne 2 : masse salariale)*/
SELECT r.code_postal, SUM(h.salaire) AS masse_salariale
FROM Restaurants r
INNER JOIN History h ON r.id = h.resto_id
WHERE h.annee = 2021
GROUP BY r.code_postal
ORDER BY masse_salariale;

/*d. Extraire le plat le moins vendu entre 00h00 et 11h59 pour chaque restaurant. (Colonne 1 : Restaurant, colonne 2 : plat, colonne 3 : quantité)*/
SELECT DISTINCT * FROM
(SELECT tmp.code_postal, tmp.nom, SUM(tmp.quantite) AS QuantiteCommandeeMinuitMidi FROM
(SELECT r.code_postal, EXTRACT(HOUR FROM o.date_heure) as heure, i.id, i.nom, oi.quantite 
FROM Restaurants r
INNER JOIN Orders o ON o.resto_id = r.id 
INNER JOIN Orders_items oi ON oi.order_id = o.id
LEFT JOIN Menus m ON m.id = oi.item_id
LEFT JOIN Items i ON m.plat = i.id OR oi.item_id = i.id
WHERE i.type_item = 'plat') AS tmp
WHERE heure < 12
GROUP BY tmp.code_postal, tmp.id
ORDER BY tmp.code_postal, QuantiteCommandeeMinuitMidi DESC) AS tmp2
GROUP BY code_postal;

/*e. Extraire les restaurants n’ayant pas encore ouvert (sans employés). (Colonne 1 : Restaurant)*/
/*Y en a pas, on se contente donc de sortir le nombre d'employés par restaurant en 2021*/
SELECT r.code_postal, COUNT(*) AS NbEmployes
FROM History h
INNER JOIN Restaurants r ON h.resto_id = r.id
WHERE h.annee = 2021
GROUP BY r.code_postal;

/*f. Extraire les stocks du restaurant du 64200 avec une colonne intitulée « à commander » qui aura comme valeur : (Colonne 1 : Ingredient, Colonne 2 : A commander)
Si l’ingrédient a plus de 1000 unités en stock, le statut est « OK ».
Si l’ingrédient a entre 750 et 999 unités en stock, le statut est « en stock ».
Si l’ingrédient a entre 500 et 747 unités en stock, le statut est « à commander : Pas d’urgence ».
Si l’ingrédient a entre 250 et 499 unités en stock, le statut est « à commander : urgence ».
Si l’ingrédient a entre 1 et 249 unités en stock, le statut est « à commander : prioritaire ».
Si l’ingrédient n’a pas de stock, le statut est : « à commander : Rupture de stock ».*/

ALTER TABLE Stocks ADD COLUMN IF NOT EXISTS statut VARCHAR(30);
UPDATE Stocks SET statut = CASE
		WHEN unites>=1000 THEN 'OK'
		WHEN unites BETWEEN 750 AND 999 THEN 'En stock'
		WHEN unites BETWEEN 500 AND 749 THEN 'À commander : pas d urgence'
		WHEN unites BETWEEN 250 AND 499 THEN 'À commander : urgence'
		WHEN unites BETWEEN 1 AND 249 THEN 'À commander : prioritaire'
		WHEN unites =0 THEN 'À commander : rupture de stock'
	END;

SELECT i.nom, s.statut
FROM Stocks s
JOIN Restaurants r on s.resto_id = r.id 
JOIN Ingredients i on s.ing_id = i.id
WHERE r.code_postal ='64200';

/*g. Extraire le bénéfice moyen de chaque pays sur l’ensemble des produits vendus (bénéfice = prix de vente d’un item – prix d’achat). (Colonne 1 : Pays, Colonne 2 : Benefmoyen)*/
/* DEUX OPTIONS : */
/* 1. le bénéfice moyen sur les produits proposés dans un pays*/
SELECT pays, AVG(marge) AS MargeMoyenneCarte FROM
	(SELECT p.pays, i.nom, i.prix - SUM(r.unites * i2.prix) as marge
	FROM Pays p
	INNER JOIN Cartes c ON p.id = c.pays_id
	INNER JOIN Items i ON c.item_id = i.id
	LEFT JOIN Menus m ON m.id = i.id 
	LEFT JOIN Recettes r ON m.plat = r.item_id
		OR m.dessert = r.item_id
		OR m.boisson = r.item_id
		OR i.id = r.item_id
	LEFT JOIN Ingredients i2 ON i2.id = r.ing_id
	GROUP BY p.pays, i.nom) AS Marge
GROUP BY Marge.pays;

/* 2. le bénéfice moyen sur les produits qui ont été effectivement vendus dans un pays*/
SELECT Vente.pays, SUM(QuantiteVendue * marge)/SUM(QuantiteVendue) AS MargeMoyenneVendue FROM
(SELECT p.pays, i.nom, SUM(oi.quantite) AS QuantiteVendue
	FROM Restaurants r
	INNER JOIN Pays p ON r.pays_id = p.id
	INNER JOIN Orders o ON r.id = o.resto_id 
	INNER JOIN Orders_items oi ON o.id = oi.order_id
	INNER JOIN Items i ON oi.item_id = i.id
	GROUP BY p.pays, i.nom) AS Vente
INNER JOIN
(SELECT p.pays, i.nom, i.prix - SUM(r.unites * i2.prix) as marge
	FROM Pays p
	INNER JOIN Cartes c ON p.id = c.pays_id
	INNER JOIN Items i ON c.item_id = i.id
	LEFT JOIN Menus m ON m.id = i.id 
	LEFT JOIN Recettes r ON m.plat = r.item_id
		OR m.dessert = r.item_id
		OR m.boisson = r.item_id
		OR i.id = r.item_id
	LEFT JOIN Ingredients i2 ON i2.id = r.ing_id
	GROUP BY p.pays, i.nom) AS Marge
ON Marge.pays = Vente.pays AND Marge.nom = Vente.nom
GROUP BY Vente.pays;
		
/*h. Extraire le top 10 des restaurants payant le mieux leurs employés ayant plus de deux ans d’expérience. (Colonne 1 : restaurant, colonne 2 : salaireMoyen)*/
SELECT r.code_postal, r.ville, AVG(h.salaire) AS SalaireMoy2ans
FROM History h 
JOIN Restaurants r on h.resto_id = r.id
JOIN Personnel p on h.ind_id = p.id
WHERE p.experience > 2
GROUP BY r.code_postal
ORDER BY AVG(h.salaire) DESC
LIMIT 10;

/*i. Extraire le nombre moyen de ventes réalisé pour chaque heure par un employé ayant moins d’1 an d’expérience (Colonne 1 : Heure, Colonne 2 : nbventes)*/
SELECT tmp.hh, AVG(tmp.NbVentes) FROM
	(SELECT p.id, EXTRACT(HOUR FROM o.date_heure) AS hh, COUNT(*) AS NbVentes
	FROM Orders o
	INNER JOIN Personnel p ON o.vendeur_id = p.id
	WHERE p.experience = 1
	GROUP BY p.id, hh) AS tmp
GROUP BY hh;

/* Sur tous les vendeurs */
SELECT hh, AVG(NbVentes) FROM
	(SELECT p.id, EXTRACT(HOUR FROM o.date_heure) AS hh, COUNT(*) AS NbVentes
	FROM Orders o
	INNER JOIN Personnel p ON o.vendeur_id = p.id
	GROUP BY p.id, hh) AS tmp
GROUP BY hh;

/*j. Extraire le chiffre d’affaire moyen des restaurants ayant un espace pour enfant et celui des restaurants n’en ayant pas. (Colonne 1 : typeRestaurant, Colonne 2 : CAmoyen)*/
SELECT tmp.espace_enfant, AVG(tmp.CA) FROM
(SELECT r.espace_enfant, SUM(o.somme) AS CA
FROM Restaurants r
INNER JOIN Orders o ON r.id = o.resto_id
GROUP BY r.id) AS tmp
GROUP BY tmp.espace_enfant;


/*k. Extraire la moyenne des notes attribuées pour chaque manager aux employés sous leurs ordres (Colonne 1 : manager, Colonne 2 : notemoyenne).*/
SELECT h.superieur, p.prenom, p.nom, AVG(h.note) AS NoteMoyenne
FROM History h, Personnel p
WHERE h.superieur = p.id
GROUP BY h.superieur;

SELECT h.superieur, p.prenom, p.nom, AVG(h.note) AS NoteMoyenne
FROM History h
INNER JOIN Personnel p
ON p.id = h.superieur
GROUP BY h.superieur;

/* En ne conservant que les managers */
SELECT h.superieur, p.prenom, p.nom, AVG(h.note) AS NoteMoyenne
FROM History h
INNER JOIN History h2 ON h2.ind_id = h.superieur
INNER JOIN Personnel p ON p.id = h.superieur
WHERE h2.poste = 'manager'
GROUP BY h.superieur;

/*l. Lister l’ensemble des menus pour la France et l’Espagne (Colonne 1 : Pays, Colonne 2 : Nom menu, Colonne 3 : plat, Colonne 4 : boisson, Colonne 5 : dessert)*/
SELECT p.pays, i.nom as menu, i2.nom as Plat, i3.nom as Boisson, i4.nom as Dessert FROM
Pays p INNER JOIN Cartes c ON p.id = c.pays_id
INNER JOIN Items i ON c.item_id = i.id
INNER JOIN Menus m ON i.id = m.id
INNER JOIN Items i2 ON m.plat = i2.id
INNER JOIN Items i3 ON m.boisson = i3.id
INNER JOIN Items i4 ON m.dessert = i4.id
WHERE p.pays IN ('France', 'Espagne') AND i.type_item = 'menu'
ORDER BY p.pays;


