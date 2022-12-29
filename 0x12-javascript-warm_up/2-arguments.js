#!/usr/bin/node

const process = require('process');

const myVar = process.argv;
if (myVar.length < 3) {
  console.log('No argument');
} else if (myVar.length === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
