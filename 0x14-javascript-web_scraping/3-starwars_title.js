#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

const movieId = argv[2];
let url = 'https://swapi-api.hbtn.io/api/films/';
url += movieId;

request(url, function (error, response, body) {
  if (error) throw error;

  const movie = JSON.parse(body);
  console.log(movie.title);
});
