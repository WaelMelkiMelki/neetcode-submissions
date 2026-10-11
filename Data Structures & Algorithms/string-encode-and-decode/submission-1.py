
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:

        s = ""
        for item in strs:
            s += f"{len(item)}#{item}"
        return s

    def decode(self, s: str) -> List[str]:

        output = []
        i = 0
        while i < len(s):
            delimiter = s.find("#", i)
            length = int(s[i:delimiter])
            start = delimiter + 1
            output.append(s[start:start + length])
            i = start + length
        return output
