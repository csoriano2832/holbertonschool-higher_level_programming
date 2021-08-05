#!/usr/bin/node

exports.esrever = function (list) {
  let listSize = list.length - 1;
  const revList = [];

  for (let index = 0; listSize >= 0; index++) {
    revList[index] = list[listSize];
    listSize--;
  }
  return revList;
};
