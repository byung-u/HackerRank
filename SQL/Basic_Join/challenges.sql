###############
# Query
###############

# TEST 1
SELECT H.hacker_id, H.name, COUNT(C.challenge_id)
FROM Hackers AS H
    INNER JOIN Challenges AS C ON (H.hacker_id = C.hacker_id)
GROUP BY H.hacker_id, H.name


# Solution
# https://www.hackerrank.com/challenges/challenges/forum/comments/279709

/* these ar the columns we want to output */
SELECT H.hacker_id, H.name, COUNT(C.challenge_id) AS C_COUNT
FROM Hackers AS H
    /* this is the join we want to output them from */
    INNER JOIN Challenges AS C ON (H.hacker_id = C.hacker_id)
/* after they have been grouped by hacer_id, name */
GROUP BY H.hacker_id, H.name

/* but we want to be selective about which hackers we output */
/* having is required (instead of where) for filtering on groups */
HAVING
        /* output anyone with a count that is equal to... */
        C_COUNT = (
                    /* the max count that anyone has */
                    SELECT MAX(check1.cnt)
                    FROM (
                            SELECT COUNT(hacker_id) AS CNT
                            FROM Challenges
                            GROUP BY hacker_id
                            ORDER BY hacker_id) check1
                   )
        OR 
        /* or anyone who's count is in ... */
        C_COUNT IN (
                    /* the set of counts */
                    SELECT check2.cnt
                    FROM (
                            SELECT COUNT(*) AS CNT
                            FROM Challenges
                            GROUP BY hacker_id) check2
                    /* whos's group of counts... */
                    GROUP BY check2.cnt
                    /* has only 1 element */
                    HAVING COUNT(check2.cnt) = 1
                   )
/* the order the rows should be output */
ORDER BY C_COUNT DESC, C.hacker_id
;


###############
# TABLE setup
###############

CREATE TABLE Hackers (
    hacker_id integer,
    name text
);

CREATE TABLE Challenges (
    challenge_id integer,
    hacker_id integer
);


INSERT INTO Hackers VALUES (5077, "Rose");
INSERT INTO Hackers VALUES (21283, "Angela");
INSERT INTO Hackers VALUES (62743, "Frank");
INSERT INTO Hackers VALUES (88255, "Patrick");
INSERT INTO Hackers VALUES (96196, "Lisa");


INSERT INTO Challenges VALUES (61654, 5077);
INSERT INTO Challenges VALUES (58302, 21283);
INSERT INTO Challenges VALUES (40587, 88255);
INSERT INTO Challenges VALUES (29477, 5077);
INSERT INTO Challenges VALUES (1220, 21283);
INSERT INTO Challenges VALUES (69514, 21283);
INSERT INTO Challenges VALUES (46561, 62743);
INSERT INTO Challenges VALUES (58077, 62743);
INSERT INTO Challenges VALUES (18483, 88255);
INSERT INTO Challenges VALUES (33625, 96196);
INSERT INTO Challenges VALUES (61656, 5077);
INSERT INTO Challenges VALUES (61659, 5077);
