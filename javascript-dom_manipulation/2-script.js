#!/usr/bin/node
document.addEventListener('DOMContentLoaded', function() {
	const clickElement = document.getElementById('red_header');
	const headerElement = document.querySelector('header');

	clickElement.addEventListener('click', function() {
		headerElement.classList.add('red');
	});
});
