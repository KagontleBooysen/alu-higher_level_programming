#!/usr/bin/node
const dict = require('./101-data.js').dict;
let newDict = {};
for (let const in dict) {
  if (newDict[dict[const]] === undefined) {
    newDict[dict[const]] = [const];
  } else {
    newDict[dict[const]].push(const);
  }
}
console.log(newDict);
