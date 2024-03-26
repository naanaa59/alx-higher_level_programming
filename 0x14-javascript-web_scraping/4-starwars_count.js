#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const idCharacter = 18;
const urlCharacter = 'https://swapi-api.alx-tools.com/api/people/' + idCharacter + '/';
let countFilms = 0;

request.get({ url: apiUrl, json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    const films = body.results;
    films.forEach(film => {
      film.characters.forEach(character => {
        if (character === urlCharacter) {
          countFilms++;
        }
      });
    });
    console.log(countFilms);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
