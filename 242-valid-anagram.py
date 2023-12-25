class Solution:
    # change method name to isAnagram when submitting on Leetcode
    def is_anagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}
        if len(s) != len(t):
            return False
        for ch in list(s):
            get_value = s_chars.get(ch)
            if get_value:
                s_chars.update({ch: get_value + 1})
            else:
                s_chars.update({ch: 1})
        for ch in list(t):
            get_value = t_chars.get(ch)
            if get_value:
                t_chars.update({ch: get_value + 1})
            else:
                t_chars.update({ch: 1})
        for key, value in s_chars.items():
            if t_chars.get(key) != value:
                return False
        return True