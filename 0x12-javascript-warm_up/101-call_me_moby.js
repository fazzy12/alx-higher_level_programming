#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
    // Increment the number
    const incrementedNumber = number + 1;
  
    // Call the provided function with the incremented value
    theFunction(incrementedNumber);
  };