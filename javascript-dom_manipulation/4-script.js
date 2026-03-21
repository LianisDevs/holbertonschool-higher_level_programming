#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
	const addItemButton = document.getElementById('add_item');

	const myList = document.querySelector('.my_list');

	addItemButton.addEventListener('click', () => {
		const newList = document.createElement('li');

		newList.textContent = 'Item';

		myList.appendChild(newList);
	});
});
