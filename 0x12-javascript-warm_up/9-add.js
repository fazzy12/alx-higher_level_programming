#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  a = args[0] = parseInt(args[0]);
  b = args[1] = parseInt(args[1]);

  return console.log(a + b);
}
add();
