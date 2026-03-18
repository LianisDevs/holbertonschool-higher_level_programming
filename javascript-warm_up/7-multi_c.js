#!/usr/bin/node
const args = process.argv;

const num = Number(args[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;

  while (i < num) {
    console.log('C is fun');
    i++;
  }
}
