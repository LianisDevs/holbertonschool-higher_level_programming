--  lists all the cities of California that can be found in the database

SELECT c.id, c.name
FROM cities AS c
WHERE c.state_id = (
	SELECT s.id
	FROM states as s
	WHERE s.name = "California"
)

ORDER BY c.id;
