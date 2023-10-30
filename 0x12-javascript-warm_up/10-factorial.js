#!/usr/bin/node
const args = process.argv.slice(2);

function factorial (n) {
    if (isNaN(n) || n === 1) {
        return 1;
    }
    const result = n * factorial(n - 1);
    return console.log(result);
}
factorial(parseInt(args[0]));