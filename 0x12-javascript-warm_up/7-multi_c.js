#!/usr/bin/node
const { argv } = require('process');
const x = parseInt(argv[2], 10);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  if (x > 0) {
    for (let index = 0; index < x; index++) {
      console.log('C is fun');
    }
  }
}
