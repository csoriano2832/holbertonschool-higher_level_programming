#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

const url = argv[2];

request(url, function (error, response, body) {
  console.log('code:', response && response.statusCode);
});
