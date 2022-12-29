#!/usr/bin/node

const myVar = parseInt(process.argv[2], 10);
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVar; i++) {
    console.log('X'.repeat(myVar));
  }
}
