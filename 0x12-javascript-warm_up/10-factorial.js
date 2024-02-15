#!/usr/bin/node

const firstArg = process.argv[2];
const n = parseInt(firstArg);
function fac (num) {
  let res = num;

  if (num <= 0) {
    return 1;
  }
  res *= fac(num - 1);
  return res;
}

if (isNaN(n)) {
  console.log('1');
} else {
  console.log(fac(n));
}
