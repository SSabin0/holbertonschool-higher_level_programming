#!/usr/bin/node
const { argv } = require('node:process');

function factorial (n) {
  // Base Case
  if (n === 1 || n === 0 || isNaN(n) === true) return 1;

  // Recursive Case
  return n * factorial(n - 1);
}

console.log(factorial(argv[2]));
