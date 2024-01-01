def is_valid(s: str) -> bool:
    brackets = {'}': '{', ']': '[', ')': '('}
    string_list = list(s)
    stack = []
    for ch in string_list:
        if ch in brackets.values():
            stack.append(ch)
        else:
            if len(stack) != 0 and stack[-1] == brackets.get(ch):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
