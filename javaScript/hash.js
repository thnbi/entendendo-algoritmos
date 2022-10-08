"use strict";

const voted = {};

function checkVoter (name) {
   if(voted[name]){
      console.log('tire-o daqui!');
   }else {
      voted[name] = true;
      console.log("pode votar");
   }
}

checkVoter('jordanna');
checkVoter('renato');
checkVoter('renato');