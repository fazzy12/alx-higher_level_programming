#!/usr/bin/node
// Rectangle that defines a rectangle
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      return {};
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
