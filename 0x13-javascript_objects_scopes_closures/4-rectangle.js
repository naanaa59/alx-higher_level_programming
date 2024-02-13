#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && h !== undefined && w !== undefined) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row = row + 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    if (this.isValid()) {
      const tmp = this.width;
      this.width = this.height;
      this.height = tmp;
    }
  }

  double () {
    if (this.isValid()) {
      this.width *= 2;
      this.height *= 2;
    }
  }

  isValid () {
    return typeof this.width === 'number' && this.width > 0 &&
           typeof this.height === 'number' && this.height > 0;
  }
}
module.exports = Rectangle;
