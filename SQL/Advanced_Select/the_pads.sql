SELECT
    CONCAT(Name, '(', SUBSTR(Occupation, 1, 1), ')')
FROM OCCUPATIONS
    ORDER BY Name ASC;

SELECT
    CONCAT('There are a total of ', COUNT(Occupation), ' ', LOWER(Occupation),'s.')
FROM OCCUPATIONS
    GROUP BY Occupation
    ORDER BY COUNT(Occupation), Occupation ASC;

# CREATE sample
CREATE TABLE contacts (
 contact_id integer PRIMARY KEY,
 first_name text NOT NULL,
 last_name text NOT NULL,
 email text NOT NULL UNIQUE,
 phone text NOT NULL UNIQUE
);
