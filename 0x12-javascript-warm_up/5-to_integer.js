#!/usr/bin/node
const { argv } = require('process');
const myNum = parseInt(argv[2], 10);

if (typeof (myNum) === 'number' && !isNaN(myNum)) {
  console.log('My number: ' + myNum);
} else {
  console.log('Not a number');
}
