#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

const filename = argv[2];

fs.readFile(filename, 'utf-8', (err, data) => {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});
