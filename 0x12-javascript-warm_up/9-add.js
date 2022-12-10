#!/usr/bin/node

function add(a, b) {
  return a + b;
}

const myVar2 = parseInt(process.argv[2])
const myVar3 = parseInt(process.argv[3]);
console.log(add(myVar2, myVar3));
