#!/usr/bin/node

const argsCount = process.argv.length;
let msg = 'No arguemnt';

if (argsCount === 3) {
  msg = 'Argument found';
} else if (argsCount > 3) {
  msg = 'Arguments found';
}

console.log(msg);
