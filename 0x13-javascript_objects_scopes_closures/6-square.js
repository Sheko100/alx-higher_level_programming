#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
