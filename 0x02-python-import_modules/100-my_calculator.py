#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arg = sys.argv
    arglen = len(arg)
    operr = "Unknown operator. Available operators: +, -, * and /"
    res = 0
    if (arglen != 4):
        print("Usage: {} <a> <operator> <b>".format(arg[0]))
        sys.exit(1)
    match arg[2]:
        case "+":
            res = add(int(arg[1]), int(arg[3]))
        case "-":
            res = sub(int(arg[1]), int(arg[3]))
        case "*":
            res = mul(int(arg[1]), int(arg[3]))
        case "/":
            res = div(int(arg[1]), int(arg[3]))
        case _:
            print("{}".format(operr))
            sys.exit(1)
    print("{} {} {} = {}".format(arg[1], arg[2], arg[3], res))
