class Solution:

    def encode(self, strs: List[str]) -> str:
        fullstring = ''
        temp = []
        for i in strs:
            temp.append("^#$")
            temp.append(i)
        for i in temp:
            fullstring += i
        return fullstring

    def decode(self, s: str) -> List[str]:
        result = s.split("^#$")[1:]
        return result