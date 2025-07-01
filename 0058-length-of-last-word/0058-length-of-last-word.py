class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = []
        string = ""
        for i in s:
            if i!=" ":
                string+=i
            else:
                if string!="":
                    l.append(string)
                string=""
        if string!="":
            l.append(string)

        return len(l[-1])
