import re

def is_palindrome(s: str) -> bool:
  lower_string = s.lower()
  sanitised_string = re.sub(r'\W+', '', lower_string)
  sanitised_string = sanitised_string.replace('_', '')
  sanitised_string_list = list(sanitised_string)
  if len(sanitised_string_list) <= 1:
    return True
  fw_counter = 0
  rv_counter = len(sanitised_string_list) - 1
  while fw_counter < rv_counter:
    if sanitised_string_list[fw_counter] != sanitised_string_list[rv_counter]:
      return False
    fw_counter+=1
    rv_counter-=1
  return True


print(is_palindrome("ab_a"))