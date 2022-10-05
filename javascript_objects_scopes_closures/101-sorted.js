#!/usr/bin/node
const dict = require('./101-data.js').dict;
let const = {};
for (let key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[const]].push(const);
  }
}
console.log(const);
