
SELECT SUM(city.POPULATION)
FROM CITY AS city
    LEFT JOIN COUNTRY AS country ON (CITY.COUNTRYCODE = COUNTRY.CODE)
    WHERE country.CONTINENT = 'Asia';
