#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = argv[2];

request(url, (error, response, body) => {
  if (error) throw error;

  const dictionary = JSON.parse(body);
  const tasks = {};

  for (const task of dictionary) {
    if (task.completed) {
      const user = task.userId;

      if (!tasks[user]) {
        tasks[user] = 0;
      }

      tasks[user] = tasks[user] + 1;
    }
  }
  console.log(tasks);
});
