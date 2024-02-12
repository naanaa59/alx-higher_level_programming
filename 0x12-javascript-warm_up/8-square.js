#!/usr/bin/node
const p = 'X';
let i = 0;
let j = 0;
let row = '';
const arg = Number(process.argv[2]);

if (isNaN(arg)) {
  console.log('Missing size');
}
while (i < arg) {
  while (j < arg) {
    row = row + p;
    j++;
  }

  console.log(row);
  i++;
}
