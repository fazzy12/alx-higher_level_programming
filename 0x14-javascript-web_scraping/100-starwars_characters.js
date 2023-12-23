#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  charactersUrls.forEach(characterUrl => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Error: ${response.statusCode}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
