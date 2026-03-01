--  lists all the cities of California that can be found in the database

SELECT c.id, c.name
FROM hbtn_0d_usa.cities AS c
WHERE c.state_id = (
	SELECT s.id
	FROM hbtn_0d_usa.states as s
	WHERE s.name = "California"
)

ORDER BY c.id;
