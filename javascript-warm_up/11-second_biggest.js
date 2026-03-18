#!/usr/bin/node

const args = process.argv;

let max = 0;
let secondMax = 0;

if (args[2] === undefined || args[3] === undefined) {
  console.log(0);
} else {
  for (const num of args) {
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax) {
      secondMax = num;
    }
  }
  console.log(secondMax);
}
