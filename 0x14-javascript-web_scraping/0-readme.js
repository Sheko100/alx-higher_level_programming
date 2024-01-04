#!/usr/bin/node

const { argv } = require('node:process');

const argsCount = argv.length - 2;

if (argsCount > 0) {
  const fs = require('fs');

  fs.readFile(argv[2], 'utf-8', function (err, data) {
    if (err) throw err;
    console.log(data);
  });
}
