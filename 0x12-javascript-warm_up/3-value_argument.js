#!/usr/bin/node

const firstArg = process.argv[2];

let msg = 'No arguemnt';
if (firstArg) {
  msg = firstArg;
}
console.log(msg);
