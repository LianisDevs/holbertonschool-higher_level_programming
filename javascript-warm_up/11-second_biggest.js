#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

let max = -Infinity;
let secondMax = -Infinity;

if (args.length < 2) {
  console.log(0);
} else {
  for (const num of args) {
    if (num > max) {
      console.log('num is', num);
      secondMax = max;
      console.log('secondMax is now ', secondMax);
      max = num;
      console.log('max is now', max);
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }
  console.log(secondMax);
}
