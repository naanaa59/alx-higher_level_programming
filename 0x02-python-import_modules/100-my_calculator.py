#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    leng = len(sys.argv)
    if leng != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        result = 0
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        elif operator == '/':
            if b != 0:
                result = div(a, b)
        else:
            print(f"Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print(f"{a} {operator} {b} = {result}")
        exit(0)
