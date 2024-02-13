N = int(input())
stack, ans, res, var = [], [], True, 1
for _ in range(N):
    num = int(input())
    while var <= num:
        stack.append(var)
        ans.append('+')
        var += 1
    if num == stack[-1]:
        stack.pop()
        ans.append('-')
    else:
        res = False
if not res:
    print('NO')
else:
    for i in ans:
        print(i)