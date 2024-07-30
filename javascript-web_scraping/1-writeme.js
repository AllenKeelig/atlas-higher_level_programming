#!/usr/bin/node
//feels wierd not having these be mandatory
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
