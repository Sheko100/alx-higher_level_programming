#!/usr/bin/node

const firstArg = process.argv[2];
const integer = parseInt(firstArg);
let msg = 'Not a number';

if (!isNaN(integer)) {
  msg = `My number: ${integer}`;
}

console.log(msg);
