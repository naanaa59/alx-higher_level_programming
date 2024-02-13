#!/usr/bin/node

const fs = require('fs');

const contentFileA = fs.readFileSync(process.argv[2], 'utf8');
const contentFileB = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], contentFileA + contentFileB, 'utf8');
