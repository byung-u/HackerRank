###############
# Query
###############

SELECT IF(G.Grade < 8, NULL, S.Name), G.Grade, S.Marks
FROM Students AS S
    LEFT JOIN Grades AS G ON (S.Marks >= G.Min_Mark AND S.Marks <= G.Max_Mark)
ORDER BY G.Grade DESC, S.Name ASC




###############
# TABLE setup
###############

CREATE TABLE Students (
    ID integer,
    Name text,
    Marks integer
);

INSERT INTO Students VALUES (1, "Julia", 88);
INSERT INTO Students VALUES (2, "Samantha", 68);
INSERT INTO Students VALUES (3, "Maria", 99);
INSERT INTO Students VALUES (4, "Scalet", 78);
INSERT INTO Students VALUES (5, "Ashley", 63);
INSERT INTO Students VALUES (6, "Jane", 81);

CREATE TABLE Grades (
    Grade integer,
    Min_Mark integer,
    Max_Mark integer
);

INSERT INTO Grades VALUES (1, 0, 9);
INSERT INTO Grades VALUES (2, 10, 19);
INSERT INTO Grades VALUES (3, 20, 29);
INSERT INTO Grades VALUES (4, 30, 39);
INSERT INTO Grades VALUES (5, 40, 49);
INSERT INTO Grades VALUES (6, 50, 59);
INSERT INTO Grades VALUES (7, 60, 69);
INSERT INTO Grades VALUES (8, 70, 79);
INSERT INTO Grades VALUES (9, 80, 89);
INSERT INTO Grades VALUES (10, 90, 100);
