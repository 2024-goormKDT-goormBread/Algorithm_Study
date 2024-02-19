const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

const COMMAND = {
  reverse: "R",
  delete: "D",
};

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  const tryCount = Number(input.shift());
  solve(tryCount);
  process.exit();
});

const solve = (tryCount) => {
  for (let i = 0; i < tryCount; i += 1) {
    const commands = input.shift().split("");
    const arrLen = Number(input.shift());
    const shiftedArray = input.shift().slice(1, -1).split(",").map(Number);
    const arr = arrLen ? shiftedArray : [];
    let direction = 0;
    let flag = 1;

    for (let j = 0; j < commands.length; j += 1) {
      if (commands[j] === COMMAND.reverse) {
        direction = direction ? 0 : 1;
        continue;
      }
      if (commands[j] === COMMAND.delete && !arr.length) {
        flag = 0;
        console.log("error");
        break;
      }

      remove(arr, direction);
    }

    if (flag) {
      direction
        ? console.log(`[${arr.reverse().join(",")}]`)
        : console.log(`[${arr.join(",")}]`);
    }
  }
};

const remove = (arr, direction) => {
  direction ? arr.pop() : arr.shift();
};
