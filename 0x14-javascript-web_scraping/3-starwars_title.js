#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + filmId;

request.get({ url: apiUrl, json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    console.log(body.title);
  }
});
