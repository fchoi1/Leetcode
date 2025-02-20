WITH 
res AS (
    SELECT 
        id, 
        LAG(temperature) OVER (ORDER BY recordDate ASC) AS prev, 
        LAG(recordDate)  OVER (ORDER BY recordDate ASC) AS prevDate, 
        temperature AS curr,
        recordDate as currDate
    FROM Weather
)
SELECT id
FROM res 
WHERE curr > prev and DATEDIFF(currDate, prevDate) = 1
