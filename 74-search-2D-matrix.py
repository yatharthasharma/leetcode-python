from typing import List

def binary_search(array: List[int], target) -> bool:
  p1 = 0
  p2 = len(array) - 1
  while p1 <= p2:
    median = (p1+p2)//2
    if target == array[median]:
      return True
    elif target < array[median]:
      p2 = median - 1
    else:
      p1 = median + 1
  return True if target == array[p1] else False

def search_matrix(matrix: List[List[int]], target: int) -> bool:
  p1 = 0
  p2 = len(matrix) - 1
  row_length = len(matrix[0])
  while p1 <= p2:
    median = (p1 + p2) // 2
    if target >= matrix[median][0] and target <= matrix[median][row_length - 1]:
      return binary_search(matrix[median], target)
    elif target < matrix[median][0]:
      p2 = median - 1
    else:
      p1 = median + 1
  return False
  
print(search_matrix([[1]], 1))