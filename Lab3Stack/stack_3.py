# exercise 3
operation_stack = ['+','-','*','/','(',')']
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
def seperate(equation):
    stack = []
    output = ''
    for i in equation:
        if i not in operation_stack:
            output += i
        elif i == '(':
            stack.append('(')
        elif i == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and priority[i] <= priority[stack[-1]]:
                output += stack.pop()
            stack.append(i)
    while stack:
        output += stack.pop()
    return output

def main():
    equation = input('Enter : ')
    print(seperate(equation))

if __name__ == "__main__":
    main()