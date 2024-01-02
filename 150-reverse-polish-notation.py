import math
from typing import List


def eval_rpn(tokens: List[str]) -> int:
  operators = {'*', '/', '+', '-'}
  operands = []
  for char in tokens:
    if char in operators:
      second_item = int(operands.pop())
      first_item = int(operands.pop())
      if char == '*':
        operands.append(first_item * second_item)
      elif char == '+':
        operands.append(first_item + second_item)
      elif char == '/':
        operands.append(int(first_item / second_item))
      else:
        operands.append(first_item - second_item)
    else:
      operands.append(int(char))
  return operands.pop()


print(eval_rpn(["18"]))