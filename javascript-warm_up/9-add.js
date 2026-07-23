#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  if (isNaN(a) === true || isNaN(b) === true) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}

add(argv[2], argv[3]);
