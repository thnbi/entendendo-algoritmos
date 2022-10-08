function arraySort(array) {
   let length = array.length;
   let temp = 0;

   for (let i = 0; i < length; i++) {
      for (let j = 0; j < length; j++) {
         if (array[i] < array[j]) {
            temp = array[i];
            array[i] = array[j];
            array[j] = temp;
         }
      }
   }

   return array;
}