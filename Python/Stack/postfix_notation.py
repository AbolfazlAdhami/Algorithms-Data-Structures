precedence={'(':0, ')':1,'+':2,'-':2,'*':3,'/':3}


def postfix_notation(X):
        stack,postfix=[],""
        
        for x in X:
                if x.isalpha(): postfix+=x
                elif x == '(' : stack.append(x)
                else:
                        while stack and  precedence[x] <= precedence[stack[-1]]:
                                postfix+= stack.pop()
                        if x == ')' : stack.pop() # remove (
                        else: stack.append(x)               
        while stack:
                postfix+= stack.pop()
        return postfix


X =input()
print(postfix_notation(X)) 