// Ynigo Reyes
// Computer Science - TTU
// Class of 2021
// 3 / 19 / 2018
// Simple Array Sum

'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function simpleArraySum(n, ar) {

    var answer = 0;

    for(var i = 0;i < n; i++){
        answer += ar[i];
    };

    return answer

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    const ar = readLine().split(' ').map(arTemp => parseInt(arTemp, 10));

    let result = simpleArraySum(n, ar);

    ws.write(result + "\n");

    ws.end();
}
