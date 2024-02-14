#!/usr/bin/node

const fs = require('node:fs');
const argv = process.argv;

if (argv.length === 5) {
  try {
    const data1 = fs.readFileSync(argv[2], 'utf8');
    const data2 = fs.readFileSync(argv[3], 'utf8');
    const allData = data1 + data2;
    fs.writeFileSync(argv[4], allData);
  } catch (err) {
    console.error(err);
  }
} else {
  console.error(`Usage: ${argv[1]} <1st src file> <2nd src file> <dest file>`);
}
