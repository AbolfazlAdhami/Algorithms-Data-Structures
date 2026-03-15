def postfix_notation(X):
    stack = []

    for x in X:
        if x.isdigit():
            stack.append(int(x))
        else:
            b, a = stack.pop(), stack.pop()

            if x == '+':
                stack.append(a+b)
            if x == '-':
                stack.append(a-b)
            if x == '*':
                stack.append(a*b)
            if x == '/':
                stack.append(a//b)
    return stack[-1]


print(postfix_notation('234*+'))
print(postfix_notation('123*+45/-'))
