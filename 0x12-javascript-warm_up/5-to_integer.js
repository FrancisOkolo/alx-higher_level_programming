#!/usr/bin/node

const process = require('process');

const myVar = parseInt(process.argv[2], 10);
if (isNaN(myVar)) {
  console.log('Not a number');
} else {
    console.log(`My number: ${myVar}`)
}
