function binarySearch(array, value) {
	let min = 0;
	let max = array.length - 1;
	let middle = Math.floor((min + max) / 2);

	while (array[middle] !== value && min < max) {
		if (value < array[middle]) {
			max = middle - 1;
		} else {
			min = middle + 1;
		}

		middle = Math.floor((min + max) / 2);
	}

	return array[middle] !== value ? -1 : middle;
}

let list_with_10_items = [3, 9, 10, 11, 12, 13, 14, 17, 18, 19];

console.log(binarySearch(simple_list, 13));