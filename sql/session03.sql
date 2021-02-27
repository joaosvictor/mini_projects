-- a hackerrank problem
-- https://www.hackerrank.com/challenges/weather-observation-station-3/problem

-- return differents values
select distinct city
from station

-- mod() return the remainder of values id/2
where mod(id, 2) = 0

-- order by is used to sort the result
order by city;
