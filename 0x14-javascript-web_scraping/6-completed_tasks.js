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
      if (!completeCount[task.userId]) {
        completeCount[task.userId] = 1;
      }
      if (task.completed) {
        completeCount[task.userId]++;
      }
    });
    console.log(completeCount);
  }
});
