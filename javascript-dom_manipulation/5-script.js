#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
	const updateHeader = document.getElementById('update_header');

	updateHeader.addEventListener('click', () => {
		updateHeader.textContent = 'New Header!!!';
	});
});
