# exercise 2
stack = ['A', 'B', 'C', 'D', 'E', 'F']
new_stack = []
def reverse():
    print('Stack reversed : ',end ='')
    tmp = stack.copy()
    i = len(tmp)-1
    while i >= 0:
        new_stack.append(tmp.pop(i))
        i -= 1
    print(new_stack)

def main():
    print(f'This is stack : {stack}')
    reverse()

if __name__ == "__main__":
    main()