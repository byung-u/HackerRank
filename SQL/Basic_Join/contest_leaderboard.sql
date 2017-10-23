###############
# Query
###############

# TEST 1
SELECT H.hacker_id, H.name, SUM(S.score) 
FROM Hackers AS H
    INNER JOIN Submissions AS S ON (H.hacker_id = S.hacker_id)
GROUP BY H.hacker_id, H.name


# Solutinon 1
SELECT H.hacker_id, H.name, SUM(SUB_SCORE) AS SUM_SCORE
FROM Hackers AS H
    INNER JOIN (
                    /* find max_score*/
                    SELECT S.hacker_id, MAX(S.score) AS SUB_SCORE
                    FROM Submissions AS S
                    GROUP BY S.challenge_id, S.hacker_id
               ) MAX_SCORE
    ON H.hacker_id = MAX_SCORE.hacker_id
GROUP BY H.hacker_id, H.name
/* don't accept hackers with total_score=0 */
HAVING SUM_SCORE > 0
/* finally order as required */
ORDER BY SUM_SCORE DESC, H.hacker_id
;

# Solutinon 2
SELECT H.hacker_id, H.name, SUM(SUB_SUM) AS SUM_SCORE
FROM Hackers AS H
    JOIN (
            SELECT S.hacker_id, S.challenge_id, MAX(S.score) AS SUB_SUM
            FROM Submissions AS S
                GROUP BY S.hacker_id, S.challenge_id
                HAVING SUB_SUM > 0
         ) AS check1
    ON ( H.hacker_id = check1.hacker_id)
GROUP BY H.hacker_id
ORDER BY SUM_SCORE DESC, H.hacker_id
;



###############
# TABLE setup
###############

CREATE TABLE Hackers (
    hacker_id integer,
    name text
);

CREATE TABLE Submissions (
    submission_id integer,
    hacker_id integer,
    challenge_id integer,
    score integer
);


INSERT INTO Hackers VALUES (4071, "Rose");
INSERT INTO Hackers VALUES (4806, "Angela");
INSERT INTO Hackers VALUES (26071, "Frank");
INSERT INTO Hackers VALUES (49438, "Patrick");
INSERT INTO Hackers VALUES (74842, "Lisa");
INSERT INTO Hackers VALUES (80305, "Kimberly");
INSERT INTO Hackers VALUES (84072, "Bonnie");
INSERT INTO Hackers VALUES (87668, "Michael");
INSERT INTO Hackers VALUES (92118, "Todd");
INSERT INTO Hackers VALUES (95895, "Joe");


INSERT INTO Submissions VALUES (67194, 74842, 63132, 76);
INSERT INTO Submissions VALUES (64479, 74842, 19797, 98);
INSERT INTO Submissions VALUES (40742, 26071, 49593, 20);
INSERT INTO Submissions VALUES (17513,  4806, 49593, 32);
INSERT INTO Submissions VALUES (69846, 80305, 19797, 19);
INSERT INTO Submissions VALUES (41002, 26071, 89343, 36);
INSERT INTO Submissions VALUES ( 6943,  4071, 19797, 95);
INSERT INTO Submissions VALUES ( 9951,  4071, 49593, 43);
INSERT INTO Submissions VALUES (10063,  4071, 49593, 96);
