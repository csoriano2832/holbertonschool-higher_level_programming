#!/usr/bin/node
const { argv } = require('process');
const intArg = parseInt(argv[2], 10);

function factorial (num) {
  if (isNaN(num)) {
    return 1;
  }

  if (num === 0) {
    return 1;
  }

  num *= factorial(num - 1);
  return num;
}

console.log(factorial(intArg));
