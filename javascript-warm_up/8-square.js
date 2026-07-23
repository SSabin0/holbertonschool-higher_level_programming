#!/usr/bin/node
const { argv } = require('node:process');
const myNumber = argv[2];
if (isNaN(myNumber) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNumber; i++) {
    let row = '';
    for (let j = 0; j < myNumber; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
