#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request.get({ url: apiUrl, json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const films = body.results;
    let countFilms = 0;
    films.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes('18')) {
          countFilms++;
        }
      });
    });
    console.log(countFilms);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
