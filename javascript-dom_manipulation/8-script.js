#!/usr/bin/node

fetch('https://hellosalut.stefanbohacek.com/?lang=fr').then(response => {
	return response.json()
}).then(jsonData => {
	const targetElement = document.getElementById('hello');

	if (targetElement) {
		targetElement.textContent = jsonData.hello;
	};
});
