#!/usr/bin/node

const firstArg = process.argv[2];

const size = parseInt(firstArg);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < size; row++) {
    for (let col = 0; col < size; col++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
