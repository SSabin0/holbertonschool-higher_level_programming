#!/usr/bin/node

if (isNaN(argv[2]) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argv[2]));
}
