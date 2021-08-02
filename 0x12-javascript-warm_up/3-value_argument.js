#!/usr/bin/node
const { argv } = require('process');
let argc = 0;

while (argv[argc]) {
  argc++;
}

if (argc < 3) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
