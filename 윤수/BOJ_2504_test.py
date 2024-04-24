import unittest

def calculateBrackets(s: str) -> int:
    stack = []  # 스택 초기화
    pair = {')': '(', ']': '['}  # 괄호의 짝을 나타내는 딕셔너리
    score = {')': 2, ']': 3}  # 괄호 종류에 따른 점수
    temp = 1  # 현재 깊이에서의 임시 점수
    result = 0  # 최종 결과값

    for i, char in enumerate(s):  # 문자열을 순회하며 각 문자(char)와 인덱스(i)에 대해 반복
        if char in "([":
            stack.append(char)  # 여는 괄호는 스택에 추가
            # 괄호에 따른 점수를 temp에 곱함 (2배 또는 3배)
            temp *= score.get(char, 1) * 2 if char == '(' else 3
        elif char in ")]":
            # 스택이 비었거나 스택의 마지막 요소가 해당 닫는 괄호와 짝이 맞지 않는 경우 0 반환
            if not stack or stack[-1] != pair[char]:
                return 0
            # 직전 문자가 해당하는 여는 괄호인 경우, 결과값에 현재 임시 점수(temp) 추가
            if s[i - 1] == pair[char]:
                result += temp
            stack.pop()  # 스택에서 괄호 제거
            temp //= score[char]  # temp를 해당 괄호의 점수로 나눔

    # 모든 순회가 끝난 후 스택이 비어있지 않으면 0 반환, 그렇지 않으면 계산된 결과 반환
    return result if not stack else 0

class TestBracketCalculate(unittest.TestCase):
    def test_valid_brackets(self):
        self.assertEqual(calculateBrackets("()"), 2)
        self.assertEqual(calculateBrackets("[]"), 3)
        self.assertEqual(calculateBrackets("(()[[]])([])"), 28)

    def test_invalid_brackets(self):
        self.assertEqual(calculateBrackets(")("), 0)
        self.assertEqual(calculateBrackets("([)"), 0)
        self.assertEqual(calculateBrackets("(()"), 0)
        self.assertEqual(calculateBrackets("([)]"), 0)

if __name__ == "__main__":
    unittest.main()