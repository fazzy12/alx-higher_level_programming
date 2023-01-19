#!/usr/bin/node
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

fetch(url)
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Error: Could not retrieve movie information.');
    }
  })
  .then(data => {
    console.log(data.title);
  })
  .catch(error => {
    console.log(error);
  });
