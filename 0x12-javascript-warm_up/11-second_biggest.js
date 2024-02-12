#!/usr/bin/node
const stringArgs = process.argv.slice(2);
const args = stringArgs.map(Number);

if (isNaN(process.argv[2]) || args.length === 1) {
  console.log(0);
} else {
  args.sort();
  console.log(args[args.length - 2]);
}
