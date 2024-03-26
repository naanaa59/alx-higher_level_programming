#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

const completeCount = {};

request.get({ url, json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode === 200) {
    body.forEach(task => {
      if (task.completed) {
        if (completeCount[task.userId] === undefined) {
          completeCount[task.userId] = 1;
        } else {
          completeCount[task.userId]++;
        }
      }
    });
    console.log(completeCount);
  }
});
