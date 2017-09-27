#!/usr/bin/env python3

cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    if n == 0:
        return []
    fib = [0]
    a, b = 0, 1
    while len(fib) < n:
        fib.append(b)
        a, b = b, a+b
    return list(map(cube, fib))

    # return a list of fibonacci numbers
if __name__ == '__main__':
    N = int(input())
    print(fibonacci(N))

