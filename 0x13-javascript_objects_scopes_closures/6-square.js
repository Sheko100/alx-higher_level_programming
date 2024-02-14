#!/usr/bin/node

const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    const ch = c === undefined ? 'X' : c;

    for (let row = 0; row < this.height; row++) {
      for (let col = 0; col < this.width; col++) {
        process.stdout.write(ch);
      }
      console.log('');
    }
  }
}

module.exports = Square;
