#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const { argv } = require('process');

const url = argv[2];
const filePath = argv[3];

request(url, function (error, response, body) {
  if (error) throw error;
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) throw err;
  });
});
