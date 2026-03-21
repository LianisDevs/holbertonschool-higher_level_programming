#!/usr/bin/node
const headerElement = document.getElementById('red_header');

const redHeaderElement = document.querySelector('header');

redHeaderElement.addEventListener('click', () => {
	headerElement.style.color = '#FF0000';
});
