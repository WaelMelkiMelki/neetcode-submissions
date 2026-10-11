class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionaire = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - 97] += 1

            key = tuple(count)

            if key in dictionaire:
                dictionaire[key].append(s)
            else:
                dictionaire[key] = [s]

        return list(dictionaire.values())