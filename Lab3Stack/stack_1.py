# exercise 1
stack = ['A', 'B', 'C', 'D', 'E', 'F']

# part 1
def fifo():
    tmp = stack.copy()
    print('\nFIFO : ', end='')
    while len(tmp) > 0:
        print(tmp.pop(0), end=' ')

# part 2
def filo():
    tmp = stack.copy()
    print('\nFILO : ', end='')
    i = len(tmp)-1
    while i >= 0:
        print(tmp.pop(i), end=' ')
        i -= 1

def main():
    print(f'This is stack : {stack}')
    filo()
    fifo()

if __name__ == "__main__":
    main()

