#!/usr/bin/node
const list = require('./100-data').list;
const factor = list.map((element, index) => {
  return element * index;
});

console.log(list);
console.log(factor);
