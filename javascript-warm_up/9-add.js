#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const args = process.argv;
const num1 = Number(args[2]);
const num2 = Number(args[3]);

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
