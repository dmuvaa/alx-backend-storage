-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT
    band_name,
    CASE
        WHEN split IS NULL OR split = 0 THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM
    metal_bands
WHERE
    LOWER(style) = 'glam rock'
ORDER BY
    lifespan DESC;
