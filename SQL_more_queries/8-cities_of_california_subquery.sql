--  lists all the cities of California that can be found in the database
SET @db = SELECT DATABASE();

SELECT c.id, c.name
FROM @db.cities AS c
WHERE c.state_id = (
	SELECT s.id
	FROM @db.states as s
	WHERE s.name = "California"
)
ORDER BY c.id;
