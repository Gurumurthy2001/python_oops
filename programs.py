# 1--simple hellworld

print("hello world")

#Or

def hello():
    return "hello world!.."
g=hello()
print(g)

# 2-- simple calculator

def simplecalc(a,b,operator):
'''the operator must be within a single qoute'''

#for addition operation
    if operator=='+':
        return a+b
#for subtraction operation
    elif operator=='-':
        return a-b
#for multiplication operation
    elif operator=='*':
        return a*b
#for division operation operation
    elif operator=='/':
        return a/b
#for floor division operation
    elif operator=='//':
        return a//b
#for power operation
    elif operator=='**':
        return a**b
#if the selected operator is wrong
    else:
        return  "please select other other operator"

