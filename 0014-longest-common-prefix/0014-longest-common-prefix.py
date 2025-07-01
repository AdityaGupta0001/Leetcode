class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string_lengths = []
        for i in strs:
            string_lengths.append(len(i))
        minimum_str_index = string_lengths.index(min(string_lengths))

        string = strs[minimum_str_index]
    
        out = ""
        
        continuity = -1
        for i in range(len(string)):
            flag = False
            for j in strs:
                if j[i]!=string[i]:
                    flag = True
                    break
            if flag == False:
                if continuity+1 != i:
                    break
                else:
                    continuity+=1
                    out+=string[i]
            
        
        if string.find(out)==0 and out!="":
            return out
        else:
            return ""

