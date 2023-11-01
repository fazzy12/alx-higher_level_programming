#!/usr/bin/node
// Imports an array and computes a new array.
const {dict} = require('./101-data');
const newDict = {};
for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [];
  }
  newDict[dict[key]].push(key);
}
