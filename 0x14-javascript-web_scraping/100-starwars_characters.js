#!/usr/bin/node

const argsCount = process.argv.length - 2;

if (argsCount > 0) {
  const req = require('request');
  const id = process.argv[2];
  const filmsEnd = `https://swapi-api.alx-tools.com/api/films/${id}`;

  req(filmsEnd, async function (err, res, body) {
    if (err) throw err;
    else {
      const film = JSON.parse(body);
      const chars = film.characters;

      for (const charEnd of chars) {
        await req(charEnd, async function (err, res, body) {
          if (err) throw err;
          else {
            const chara = JSON.parse(body);
            await console.log(chara.name);
          }
        });
      }
    }
  });
}
