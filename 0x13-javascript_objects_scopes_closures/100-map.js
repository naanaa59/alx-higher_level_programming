#!/usr/bin/node
const impList = require('./100-data.js');

const impArr = impList.list;
console.log(impArr);
const modArr = impArr.map((value, index) => {
  return value * index;
});
console.log(modArr);
