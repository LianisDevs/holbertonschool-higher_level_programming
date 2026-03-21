#!/usr/bin/node
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json').then(response => {
	return response.json()
}).then(jsonData => {
	const targetElement = document.getElementById('character');

	if (targetElement) {
		targetElement.textContent = jsonData.name;
	}
});
