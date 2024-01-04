#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

fs.readFile(argv[2], 'utf-8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
