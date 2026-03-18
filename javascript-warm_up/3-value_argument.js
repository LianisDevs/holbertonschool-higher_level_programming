#!/usr/bin/node
const args = process.argv;

if (args[2] === undefined) {
  console.log('No aruments');
} else {
  let i = 2;

  while (args[i] !== undefined) {
    console.log(args[i]);
    i++;
  }
}
