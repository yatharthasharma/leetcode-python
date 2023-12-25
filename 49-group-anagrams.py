from typing import List


class Solution:
    # change method name to groupAnagrams when submitting on Leetcode
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        set_with_anagrams = {}
        for str in strs:
            sorted_string = ''.join(sorted(str))
            if sorted_string in set_with_anagrams:
                set_with_anagrams.get(sorted_string).append(str)
            else:
                set_with_anagrams.update({sorted_string: [str]})
        return list(set_with_anagrams.values())