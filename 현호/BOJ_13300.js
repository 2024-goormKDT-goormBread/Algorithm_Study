const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  const [n, k] = input.shift().split(" ").map(Number);
  solve(n, k);
  process.exit();
});

const solve = (n, k) => {
  const students = getStudents();

  console.log(allocatedRoom(students[0], k) + allocatedRoom(students[1], k));
};

const getStudents = () =>
  input.reduce(
    (acc, curr) => {
      const [gender, grade] = curr.split(" ");
      acc[gender][grade - 1] += 1;
      return acc;
    },
    [
      [0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
    ]
  );

const allocatedRoom = (students, k) =>
  students.reduce((acc, curr) => {
    return (acc += Math.ceil(curr / k));
  }, 0);
