#!/usr/bin/node
const arg = Number(process.argv[2]);

function factorial (num) {
  if (num === 0 || num === 1 || isNaN(arg)) {
    return 1;
  } else {
    num *= factorial(num - 1);
  }
  return num;
}

console.log(factorial(arg));
