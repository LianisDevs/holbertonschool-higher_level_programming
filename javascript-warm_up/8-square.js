#!/usr/bin/node
const args = process.argv;

const num = Number(args[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < num; a++) {
    let row = '';

    for (let b = 0; b < num; b++) {
      row += 'X';
    }
    console.log(row);
  }
}
