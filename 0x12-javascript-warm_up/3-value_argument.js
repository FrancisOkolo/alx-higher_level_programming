#!/usr/bin/node

const process = require('process');

const myVar = process.argv;
if (myVar[1]) {
  console.log('No argument');
}  else if (myVar[2]) {
     console.log('No argument');
}  else {
     console.log(myVar);
}
