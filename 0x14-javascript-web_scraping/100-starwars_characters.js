#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

let url = 'https://swapi-api.hbtn.io/api/films/';
const movie = argv[2];
url += movie;

request(url, (error, response, body) => {
  if (error) throw error;

  const movies = JSON.parse(body).characters;

  for (const characters of movies) {
    request(characters, (error, response, body) => {
      if (error) throw error;

      const character = JSON.parse(body);
      console.log(character.name);
    });
  }
});
