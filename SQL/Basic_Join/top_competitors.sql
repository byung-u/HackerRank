###############
# Query
###############

SELECT H.hacker_id, H.name
FROM Submissions AS S    
    INNER JOIN Challenges AS C ON (S.challenge_id = C.challenge_id)
    INNER JOIN Difficulty AS D ON (C.difficulty_level = D.difficulty_level)
    INNER JOIN Hackers AS H ON (S.hacker_id = H.hacker_id)
WHERE D.difficulty_level = C.difficulty_level AND D.score = S.score
GROUP BY H.hacker_id, H.name
HAVING COUNT(S.hacker_id) > 1
ORDER BY COUNT(S.hacker_id) DESC, S.hacker_id ASC
;





###############
# TABLE setup
###############

CREATE TABLE Hackers (
    hacker_id integer,
    name text
);

CREATE TABLE Difficulty (
    difficulty_level integer,
    score integer
);

CREATE TABLE Challenges (
    challenge_id integer,
    hacker_id integer,
    difficulty_level integer
);

CREATE TABLE Submissions (
    submission_id integer,
    hacker_id integer,
    challenge_id integer,
    score integer
);

INSERT INTO Hackers VALUES (5580, "Rose");
INSERT INTO Hackers VALUES (8439, "Angela");
INSERT INTO Hackers VALUES (27205, "Frank");
INSERT INTO Hackers VALUES (52243, "Patrick");
INSERT INTO Hackers VALUES (52348, "Lisa");
INSERT INTO Hackers VALUES (77726, "Bonnie");
INSERT INTO Hackers VALUES (83082, "Michael");
INSERT INTO Hackers VALUES (86870, "Todd");
INSERT INTO Hackers VALUES (90411, "Joe");

INSERT INTO Difficulty VALUES (1, 20);
INSERT INTO Difficulty VALUES (2, 30);
INSERT INTO Difficulty VALUES (3, 40);
INSERT INTO Difficulty VALUES (4, 60);
INSERT INTO Difficulty VALUES (5, 80);
INSERT INTO Difficulty VALUES (6, 100);
INSERT INTO Difficulty VALUES (7, 120);


INSERT INTO Challenges VALUES (4810, 77726, 4);
INSERT INTO Challenges VALUES (21089, 27205, 1);
INSERT INTO Challenges VALUES (36566, 5580, 7);
INSERT INTO Challenges VALUES (66730, 52243, 6);
INSERT INTO Challenges VALUES (71055, 52243, 2);

INSERT INTO Submissions VALUES (68628,77726,36566,30);
INSERT INTO Submissions VALUES (65300,77726,21089,10);
INSERT INTO Submissions VALUES (40326,52243,36566,77);
INSERT INTO Submissions VALUES (97397,90411,66730,100);
INSERT INTO Submissions VALUES (97431,90411,71055,30);

