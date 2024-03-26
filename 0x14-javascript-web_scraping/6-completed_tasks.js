#!/usr/bin/node

const argsCount = process.argv.length - 2;

if (argsCount > 0) {
  const req = require('request');
  const url = process.argv[2];

  req(url, function (err, res, body) {
    if (err) throw err;
    else {
      const todos = JSON.parse(body);
      const completed = {};

      todos.forEach(function (todo) {
        if (todo.completed) {
          if (todo.userId in completed) completed[todo.userId]++;
          else completed[todo.userId] = 1;
        }
      });
      console.log(completed);
    }
  });
}
