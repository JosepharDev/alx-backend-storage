-- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans
WITH fan_counts AS (
    SELECT 
        origin,
        COUNT(*) AS nb_fans
    FROM 
        metal_bands
    GROUP BY 
        origin
)

SELECT 
    origin,
    nb_fans
FROM 
    fan_counts
ORDER BY 
    nb_fans DESC;
