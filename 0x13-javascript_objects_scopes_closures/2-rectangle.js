#!/usr/bin/node
// Rectangle that defines a rectangle
class Rectangle {
  constructor(w, h) {
    this.width = w;
    this.height = h;
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object
      this.width = undefined;
      this.height = undefined;
    }
  }
}

module.exports = Rectangle;
