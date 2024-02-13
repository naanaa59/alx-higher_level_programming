#!/usr/bin/node

exports.esrever = function (list) {
  const length = list.length;
  let tmp;
  for (let i = 0; i < length / 2; i++) {
    tmp = list[i];
    list[i] = list[length - i - 1];
    list[length - i - 1] = tmp;
  }
  return list;
};
