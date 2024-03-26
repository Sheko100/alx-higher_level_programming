#!/usr/bin/node

const req = require('request');
const argsCount = process.argv.length - 2;

if (argsCount > 0) {
  const id = process.argv[2];
  const endpoint = `https://swapi-api.alx-tools.com/api/films/${id}`;

  req(endpoint, function (err, res, body) {
    if (err) throw err;
    else {
      const film = JSON.parse(body);
      console.log(film);
    }
  });
}
