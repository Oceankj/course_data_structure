from math import nan
from module2.stack import Stack


def calculator(input: str):
    last_num: int | None = None
    last_operator: str = ""
    num_s = Stack()

    for s in input:
        if s == " ":
            continue
        if not (s.isdigit() or s in "+-*/"):
            return nan
        if s.isdigit():
            last_num = 0 if last_num is None else last_num
            last_num = last_num * 10 + int(s)
        else:
            if last_num is None:
                raise ValueError("invalid value")
            if last_operator == "*":
                num_s.push(num_s.pop() * last_num)
            elif last_operator == "/":
                num_s.push(num_s.pop() / last_num)
            elif last_operator == "-":
                num_s.push(-last_num)
            else:
                num_s.push(last_num)

            last_num = None
            last_operator = s

    if last_num is None:
        return nan

    result = 0
    if last_operator == "*":
        result = num_s.pop() * last_num
    elif last_operator == "/":
        result = num_s.pop() / last_num
    elif last_operator == "-":
        result = -last_num
    else:
        result = last_num

    while num_s.size() > 0:
        result += num_s.pop()

    return result
