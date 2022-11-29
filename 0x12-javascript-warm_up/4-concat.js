#!/usr/bin/node

const process = require('process');

const myVar = process.argv;
if (myVar[2] === undefined) {
  console.log(`${myVar[2]} is undefined`);
} else if (myVar.length === 3){
    console.log(`${myVar[2]} is undefined`);
} else if (myVar.length === 4) {
    console.log(`${myVar[2]} is ${myVar[3]}`);
}
