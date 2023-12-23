#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // The first argument is the URL
const filePath = process.argv[3]; // The second argument is the file path

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(`The content has been saved to ${filePath}`);
  });
});
