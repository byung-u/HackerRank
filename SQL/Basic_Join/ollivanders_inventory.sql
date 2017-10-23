###############
# Query
###############

SELECT W.id, WP.age, W.coins_needed, W.power
FROM Wands AS W
    INNER JOIN Wands_Property AS WP ON (W.code = WP.code)
WHERE WP.is_evil = 0 AND W.coins_needed = (
    SELECT MIN(coins_needed)
    FROM Wands AS W2
    INNER JOIN Wands_Property AS WP2 ON (W2.code = WP2.code)
    WHERE WP.age = WP2.age AND W.power = W2.power
    )
ORDER BY W.power DESC, WP.age DESC
;


#####
# 1
#####
SELECT W.id, W.code, W.coins_needed, W.power, WP.age
FROM Wands AS W 
    JOIN Wands_Property AS WP ON (W.code = WP.code)
ORDER BY W.power DESC, WP.age DESC

#####
# 2
#####
SELECT W.id, W.code, W.coins_needed, W.power, WP.age
FROM Wands AS W 
    JOIN Wands_Property AS WP ON (W.code = WP.code)
WHERE WP.is_evil = 0 
ORDER BY W.power DESC, WP.age DESC


#####
# 3 (temp)
#####
SELECT W.id, W.code, W.coins_needed, W.power, WP.age
FROM Wands AS W 
    JOIN Wands_Property AS WP ON (W.code = WP.code)
WHERE WP.is_evil = 0 AND W.coins_needed = "--?-- Minimum coins_needed --?--"
ORDER BY W.power DESC, WP.age DESC


#####
# 3 
#####
SELECT W.id, WP.age, W.coins_needed, W.power
FROM Wands AS W 
    JOIN Wands_Property AS WP ON (W.code = WP.code)
WHERE WP.is_evil = 0 AND W.coins_needed = (
    SELECT MIN(coins_needed)
    FROM Wands AS W_nested
        INNER JOIN Wands_Property AS WP_nested ON (W_nested.code = WP_nested.code)
    WHERE W_nested.power = W.power AND WP_nested.age = WP.age
    )
    ORDER BY W.power DESC, WP.age DESC;


# TEST
SELECT W.id, W.code, W.coins_needed, W.power
FROM Wands AS W
    INNER JOIN Wands_Property AS WP ON (W.code = WP.code)
WHERE WP.is_evil = 0 AND W.coins_needed =
        (SELECT MIN(coins_needed)
         FROM Wands AS W2
            INNER JOIN Wands_Property AS WP2 ON (W2.code = WP2.code)
         WHERE W2.power = W.power AND WP2.age = WP.age
        )
ORDER BY W.power DESC, WP.age DESC


###############
# TABLE setup
###############

CREATE TABLE Wands (
    id integer,
    code integer,
    coins_needed integer,
    power integer
);

CREATE TABLE Wands_Property (
    code integer,
    age integer,
    is_evil integer
);


INSERT INTO Wands VALUES (1,4,3688,8);
INSERT INTO Wands VALUES (2,3,9365,3);
INSERT INTO Wands VALUES (3,3,7187,10);
INSERT INTO Wands VALUES (4,3,734,8);
INSERT INTO Wands VALUES (5,1,6020,2);
INSERT INTO Wands VALUES (6,2,6773,7);
INSERT INTO Wands VALUES (7,3,9873,9);
INSERT INTO Wands VALUES (8,3,7721,7);
INSERT INTO Wands VALUES (9,1,1647,10);
INSERT INTO Wands VALUES (10,4,504,5);
INSERT INTO Wands VALUES (11,2,7587,5);
INSERT INTO Wands VALUES (12,5,9897,10);
INSERT INTO Wands VALUES (13,3,4651,8);
INSERT INTO Wands VALUES (14,2,5408,1);
INSERT INTO Wands VALUES (15,2,6018,7);
INSERT INTO Wands VALUES (16,4,7710,5);
INSERT INTO Wands VALUES (17,2,8798,7);
INSERT INTO Wands VALUES (18,2,3312,3);
INSERT INTO Wands VALUES (19,4,7651,6);
INSERT INTO Wands VALUES (20,5,5689,3);

INSERT INTO Wands_Property VALUES (1, 45, 0);
INSERT INTO Wands_Property VALUES (2, 40, 0);
INSERT INTO Wands_Property VALUES (3, 4, 1);
INSERT INTO Wands_Property VALUES (4, 20, 0);
INSERT INTO Wands_Property VALUES (5, 17, 0);
