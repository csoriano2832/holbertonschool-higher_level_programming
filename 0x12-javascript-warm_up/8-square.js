#!/usr/bin/node
const { argv } = require('process');
const size = parseInt(argv[2], 10);
let str = '';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    str += 'X';
  }
  for (i = 0; i < size; i++) {
    console.log(str);
  }
}
