SELECT
    (CASE
    WHEN A + B <= C THEN 'Not A Triangle'
    WHEN B + C <= A THEN 'Not A Triangle'
    WHEN C + A <= B THEN 'Not A Triangle'
    WHEN A = B AND B = C THEN 'Equilateral'
    WHEN A = B AND B != C AND C != A THEN 'Isosceles'
    WHEN A != B AND B = C AND C != A THEN 'Isosceles'
    WHEN A != B AND B != C AND C = A THEN 'Isosceles'
    ELSE 'Scalene'
    END)
FROM TRIANGLES;



# SHORTER
SELECT 
    (CASE
       WHEN A + B <= C  OR B + C <= A OR C + A <= B THEN 'Not A Triangle'
       WHEN A = B AND B = C THEN 'Equilateral'
       WHEN A = B OR B = C OR C = A THEN 'Isosceles'
       ELSE 'Scalene'
    END)
FROM TRIANGLES;