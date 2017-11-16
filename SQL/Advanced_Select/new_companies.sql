" Solution "

SELECT company_code, founder, (
                                SELECT COUNT(DISTINCT lead_manager_code)
                                FROM Lead_Manager
                                WHERE company_code = C.company_code)
                                    , (
                                        SELECT COUNT(DISTINCT senior_manager_code)
                                        FROM Senior_Manager
                                        WHERE company_code = C.company_code)
                                        , (
                                            SELECT COUNT(DISTINCT manager_code)
                                            FROM Manager
                                            WHERE company_code = C.company_code)
                                            , (
                                                SELECT COUNT(DISTINCT employee_code)
                                                FROM Employee
                                                WHERE company_code = C.company_code)
FROM Company AS C                                
ORDER BY company_code
;



" Table "
CREATE TABLE Company (
    company_code text,
    founder text
);

CREATE TABLE Lead_Manager (
    lead_manager_code text,
    company_code text
);

CREATE TABLE Senior_Manager (
    senior_manager_code text,
    lead_manager_code text,
    company_code text
);

CREATE TABLE Manager (
    manager_code text,
    senior_manager_code text,
    lead_manager_code text,
    company_code text
);

CREATE TABLE Employee (
    employee_code text,
    manager_code text,
    senior_manager_code text,
    lead_manager_code text,
    company_code text
);

INSERT INTO Company VALUES ("C1", "Monika");
INSERT INTO Company VALUES ("C2", "Samantha");

INSERT INTO Lead_Manager VALUES ("LM1", "C1");
INSERT INTO Lead_Manager VALUES ("LM2", "C2");

INSERT INTO Senior_Manager VALUES ("SM1", "LM1", "C1");
INSERT INTO Senior_Manager VALUES ("SM2", "LM1", "C1");
INSERT INTO Senior_Manager VALUES ("SM3", "LM2", "C2");

INSERT INTO Manager VALUES ("M1", "SM1", "LM1", "C1");
INSERT INTO Manager VALUES ("M2", "SM3", "LM2", "C2");
INSERT INTO Manager VALUES ("M3", "SM3", "LM2", "C2");

INSERT INTO Employee VALUES ("E1", "M1", "SM1", "LM1", "C1");
INSERT INTO Employee VALUES ("E2", "M1", "SM1", "LM1", "C1");
INSERT INTO Employee VALUES ("E3", "M2", "SM3", "LM2", "C2");
INSERT INTO Employee VALUES ("E4", "M3", "SM3", "LM2", "C2");
