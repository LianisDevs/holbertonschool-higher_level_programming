#!/usr/bin/node
fetch('https://swapi-api.hbtn.io/api/films/?format=json').then(response => {
	return response.json()
}).then(jsonData => {
	const targetElement = document.getElementById('list_movies');

	if (targetElement) {

		movieList = jsonData.results.map(element => element.title);

		for (const movie of movieList) {
			var newList = document.createElement('li');
			newList.textContent = movie;
			targetElement.appendChild(newList);
		}
	}
});
