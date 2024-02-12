// 백준 10773 : 제로
// 통과여부 : O
// 설명 : 최종적으로 적어낸 수의 합을 출력하기

const fs = require("fs");
const input = fs
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .map(Number);
const command_amount = input.shift();

const solve = () => {
    const arr = [];
    let sum = 0;

    for (let i = 0; i < command_amount; i += 1) {
        if (input[i]) arr.push(input[i]);
        else arr.pop();
    }

    arr.forEach((el) => (sum += el));
    return sum;
}

console.log(solve());
