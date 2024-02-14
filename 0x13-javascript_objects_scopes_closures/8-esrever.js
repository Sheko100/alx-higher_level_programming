#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];

  let length = list.length;

  while (length > 0) {
    newList.push(list[length - 1]);
    length--;
  }

  return newList;
};
