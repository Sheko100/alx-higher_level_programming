#!/usr/bin/node

const req = require('request');
const argsCount = process.argv.length - 2;

if (argsCount > 0) {
  const endpoint = process.argv[2];

  req(endpoint, function (err, res, body) {
    if (err) throw err;
    else {
      const data = JSON.parse(body);
      const films = data.results;
      const filmsCount = films.length;
      const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
      let presenceCount = 0;

      for (let i = 0; i < filmsCount; i++) {
        const chars = films[i].characters;
        if (chars.includes(charUrl)) presenceCount++;
      }

      console.log(presenceCount);
    }
  });
}
