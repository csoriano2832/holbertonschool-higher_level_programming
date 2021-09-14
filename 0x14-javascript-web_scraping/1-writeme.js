#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

file = argv[2];
data = argv[3];

fs.writeFile(file, data, 'utf-8', (err) => {
  if (err) { console.log(err); }
});
