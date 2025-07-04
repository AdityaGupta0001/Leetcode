class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        score = list('#' + order)
        temp = True
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            m = min(len(w1), len(w2))
            for j in range(m):
                if w1[j] == w2[j]:
                    continue
                elif score.index(w1[j]) > score.index(w2[j]):
                    return False
                else:
                    break
            else:
                if len(w1) > len(w2):
                    return False

        return True
        # for i in range(m):
        #     temp = []
        #     for j in words:
        #         if j[i] not in temp:
        #             temp.append(j[i])
        #     print(temp)
        #     if len(temp)>1:
        #         val = -1
        #         for k in temp:
        #             if score.index(k)>val:
        #                 val = score.index(k)
        #             else:
        #                 check = False
        #                 break
        #         break
        #     print(check)
        
        # return check