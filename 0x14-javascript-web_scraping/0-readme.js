#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];

fs.readFile(filepath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

// const fs = require('fs');
// fs.readFile(process.argv[2], 'utf8', function (error, content) {
//   console.log(error || content);
// });
