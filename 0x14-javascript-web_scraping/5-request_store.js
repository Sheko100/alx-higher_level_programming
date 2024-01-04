#!/usr/bin/node

const argsCount = process.argv.length - 2;

if (argsCount > 1) {
  const fs = require('fs');
  const req = require('request');
  const url = process.argv[2];
  const filePath = process.argv[3];
  req(url, function (err, res, body) {
    if (err) throw err;
    else {
      fs.writeFile(filePath, body, 'utf-8', function (err) {
        if (err) console.error(err);
      });
    }
  });
}
