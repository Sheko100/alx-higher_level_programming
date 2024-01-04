#!/usr/bin/node

const req = require('request');
const argsCount = process.argv.length - 2;

if (argsCount > 0) {
  const url = process.argv[2];

  req(url, function (err, res, body) {
    if (err) throw err;
    else console.log('code:', res.statusCode);
  });
}
