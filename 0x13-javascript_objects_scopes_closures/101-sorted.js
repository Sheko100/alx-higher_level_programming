#!/usr/bin/node

const dict = require('./101-data').dict;

const occDict = {};

for (const [key, value] of Object.entries(dict)) {
  if (value in occDict === false) {
    occDict[value] = [];
  }
  occDict[value].push(key);
}
console.log(occDict);
