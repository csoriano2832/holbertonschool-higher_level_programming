#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = argv[2];
const id = '18/';

request(url, function (error, response, body) {
  if (error) throw error;

  const movies = JSON.parse(body);
  let occurence = 0;

  for (const i in movies.results) {
    for (const j in movies.results[i].characters) {
      if (movies.results[i].characters[j].slice(-3) === id) {
        occurence++;
      }
    }
  }
  console.log(occurence);
});
