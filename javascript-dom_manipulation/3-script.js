#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function() {
	const clickElement = document.getElementById('toggle_header');
	const headerElement = document.querySelector('header');

	clickElement.addEventListener('click', function() {
		if (headerElement.classList.contains('green')) {
			headerElement.classList.remove('green');
			headerElement.classList.add('red');
		} else {
			headerElement.classList.remove('red');
			headerElement.classList.add('green');
		}
	});
});
