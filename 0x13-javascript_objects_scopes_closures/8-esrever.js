#!/usr/bin/node

exports.esrever = function (list) {
	let list_size = list.length - 1;
	let rev_list = [];

	for (let index = 0; 0 <= list_size; index++) {
		rev_list[index] = list[list_size];
		list_size--;
	}
	return rev_list;
}
