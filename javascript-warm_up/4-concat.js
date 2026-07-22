#!/usr/bin/node
const { argv } = require('node:process');

const str1 = argv[2];
const str2 = argv[3];

console.log(str1 + ' is ' + str2);
