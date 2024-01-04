#!/usr/bin/node

const argsCount = process.argv.length - 2;

if (argsCount > 1) {
  const fs = require('fs');
  const filePath = process.argv[2];
  const data = process.argv[3];

  fs.writeFile(filePath, data, 'utf-8', function (err) {
    if (err) console.error(err);
  });
}
