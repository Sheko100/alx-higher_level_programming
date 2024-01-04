#!/usr/bin/node

const { argv } = require('node:process');

const argsCount = argv.length - 2;

if (argsCount > 0) {
  const fs = require('fs');

  fs.readFile(argv[2], 'utf8', function (err, data) {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
