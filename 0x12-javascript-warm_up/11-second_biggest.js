#!/usr/bin/node
const { argv } = require('process');
const argc = argv.length;
const arr = Array();

if (argc < 4) {
  console.log(0);
} else {
  for (let index = 2; index < argc; index++) {
    arr.push(parseInt(argv[index], 10));
  }
  arr.sort();
  console.log(arr[arr.length - 2]);
}
