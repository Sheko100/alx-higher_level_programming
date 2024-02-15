#!/usr/bin/node

const firstArg = process.argv[2];

let msg = 'No argument';
if (firstArg) {
  msg = firstArg;
}
console.log(msg);
