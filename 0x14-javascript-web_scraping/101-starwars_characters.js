#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  // Using a recursive function to handle asynchronous requests in sequence
  function fetchCharacter (index) {
    if (index >= characterUrls.length) return;

    request(characterUrls[index], (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);

      // Fetch the next character
      fetchCharacter(index + 1);
    });
  }

  fetchCharacter(0);
});
