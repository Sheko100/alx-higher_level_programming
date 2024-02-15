#!/usr/bin/node

const argv = process.argv;
const argsCount = argv.length;
let big = 0;
let secBig = 0;
let num = 0;

if (argsCount > 3) {
  big = parseInt(argv[2]);

  for (let i = 3; i < argsCount; i++) {
    num = parseInt(argv[i]);
    if (big < num) {
      big = num;
    }
  }
  for (let i = 2; i < argsCount; i++) {
    num = parseInt(argv[i]);
    if (secBig < num && big !== num) {
      secBig = num;
    }
  }
  console.log(secBig);
} else {
  console.log('0');
}
