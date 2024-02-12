#!/usr/bin/node
const msg = 'C is fun';
let i = 0;
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}
while (i < Number(process.argv[2])) {
  console.log(msg);
  i++;
}
