#!/usr/bin/node

const firstArg = process.argv[2];

const times = parseInt(firstArg);

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
