USE JunkFood_2021;

/*a. Extraire le nombre d’employés dans le département du 64 (Colonne 1 : nombre d’employés)*/
SELECT COUNT(*) AS NbEmp64en2021 FROM History h
INNER JOIN Restaurants r ON h.resto_id = r.id
INNER JOIN Pays p ON r.pays_id = p.id
WHERE pays='France' AND code_postal LIKE '64%' AND annee = 2021;


/*b. Extraire l’ingrédient le plus utilisé dans chaque département. (Colonne 1 : département, Colonne 2 : ingrédient, Colonne 3 : Utilisation ingrédient)*/
SELECT SUBSTR(r.code_postal,1,2) AS dpt, oi.item_id, oi.quantite AS quantite_commandee, m.*, r2.*
FROM Restaurants r
INNER JOIN Orders o ON o.resto_id = r.id 
INNER JOIN Orders_items oi ON oi.order_id = o.id
LEFT JOIN Menus m ON m.id = oi.item_id
LEFT JOIN Recettes r2
ON m.plat = r2.item_id
	OR m.dessert = r2.item_id
	OR m.boisson = r2.item_id
	OR oi.item_id = r2.item_id ;


SELECT *
FROM Menus m 
LEFT JOIN Recettes r2
ON m.plat = r2.item_id OR m.dessert = r2.item_id OR m.boisson = r2.item_id;


SELECT *
FROM  Items i
LEFT JOIN Menus m
ON m.plat = i.id OR m.dessert = i.id OR m.boisson = i.id
UNION 
SELECT *
FROM  Items i
RIGHT JOIN Menus m
ON m.plat = i.id OR m.dessert = i.id OR m.boisson = i.id
JOIN Recettes r on i.id = r.item_id
JOIN Ingredients i2 on i2.id = r.ing_id;

/*c. Extraire le restaurant ayant la masse salariale la moins importante (somme des salaires) (Colonne 1 : Restaurant, Colonne 2 : masse salariale)*/

/*d. Extraire le plat le moins vendu entre 00h00 et 11h59 pour chaque restaurant. (Colonne 1 : Restaurant, colonne 2 : plat, colonne 3 : quantité)*/

/*e. Extraire les restaurants n’ayant pas encore ouvert (sans employés). (Colonne 1 : Restaurant)*/

/*f. Extraire les stocks du restaurant du 64200 avec une colonne intitulée « à commander » qui aura comme valeur (Colonne 1 : Ingredient, Colonne 2 : A commander)
  Si l’ingrédient a plus de 1000 unités en stock, le statut est « OK ».
  Si l’ingrédient a entre 750 et 999 unités en stock, le statut est « en stock ».
  Si l’ingrédient a entre 500 et 747 unités en stock, le statut est « à commander : Pas d’urgence ».
  Si l’ingrédient a entre 250 et 499 unités en stock, le statut est « à commander : urgence ».
  Si l’ingrédient a entre 1 et 249 unités en stock, le statut est « à commander : prioritaire ».
  Si l’ingrédient n’a pas de stock, le statut est : « à commander : Rupture de stock ».*/

/*g. Extraire le bénéfice moyen de chaque pays sur l’ensemble des produits vendus (bénéfice = prix de vente d’un item – prix d’achat). (Colonne 1 : Pays, Colonne 2 : Benefmoyen)*/

/*h. Extraire le top 10 des restaurants payant le mieux leurs employés ayant plus de deux ans d’expérience. (Colonne 1 : restaurant, colonne 2 : salaireMoyen)*/

/*i. Extraire le nombre moyen de ventes réalisé pour chaque heure par un employé ayant moins d’1 an d’expérience (Colonne 1 : Heure, Colonne 2 : nbventes)*/

/*j. Extraire le chiffre d’affaire moyen des restaurants ayant un espace pour enfant et celui des restaurants n’en ayant pas. (Colonne 1 : typeRestaurant, Colonne 2 : CAmoyen)*/

/*k. Extraire la moyenne des notes attribuées pour chaque manager aux employés sous leurs ordres (Colonne 1 : manager, Colonne 2 : notemoyenne).*/

/*l. Lister l’ensemble des menus pour la France et l’Espagne (Colonne 1 : Pays, Colonne 2 : Nom menu, Colonne 3 : plat, Colonne 4 : boisson, Colonne 5 : dessert)*/