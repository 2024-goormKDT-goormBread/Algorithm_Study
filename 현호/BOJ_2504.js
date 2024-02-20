const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  console.log(solve());
  process.exit();
});

const solve = () => {
  const stack = [];
  const strArr = input.shift().split("");

  for (let i = 0; i < strArr.length; i += 1) {
    const top = stack[stack.length - 1];
    const curr = strArr[i];

    // 처음부터 닫는 기호라면 식이 성립하지 않음
    if (!checkPossible(strArr)) {
      return 0;
    }

    // 스택이 비어있고 현재 원소가 여는 기호라면 스택에 push
    // 스택의 top이 여는 기호고 현재 원소도 여는 기호라면 스택에 push
    if (curr === "[" || curr === "(") {
      stack.push(curr);
    } else if (curr === "]" || curr === ")") {
      const rev = curr === ")" ? "(" : "[";
      const val = rev === "(" ? 2 : 3;

      // 페어가 맞으면 스택에 점수를 추가
      if (top === rev) {
        stack.pop();
        stack.push(val);
      }
      // top이 점수일 경우
      // 괄호가 나올때까지 점수를 누적한다
      else {
        let temp = 0;

        while (1) {
          const pop = stack.pop();

          // 중첩의 단계가 같다면 temp에 합을 더함
          if (typeof pop === "number") {
            temp += pop;
          }
          // 괄호가 중첩되어있다면 val만큼 곱
          else if (pop === rev) {
            stack.push(temp * val);
            break;
          }
        }
      }
    }
  }

  return stack.reduce((acc, curr) => acc + curr);
};

const checkPossible = (strArr) => {
  const stack = [];

  for (let i = 0; i < strArr.length - 1; i += 1) {
    const top = stack[stack.length - 1];
    const curr = strArr[i];

    if ((curr === "]" && top === "[") || (curr === ")" && top === "(")) {
      stack.pop();
    } else {
      stack.push(curr);
    }
  }

  return stack.length ? false : true;
};
