class Solution:
    def intToRoman(self, num: int) -> str:
        def maximalSymbol(num: int):
            syms = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
            maximal = ""
            while num!=0:
                curr = ""
                sub = 0
                for i,j in syms.items():
                    if num - j>=0:
                        curr = i
                        sub = j
                    else:
                        break
                maximal+=curr
                num -= sub
            return maximal
        
        subtractive_forms = {4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM"}
        roman = ""

        max_place_val = 1
        temp = num
        while temp>9:
            max_place_val*=10
            temp = temp//10

        while num!=0:
            x = (num//max_place_val)*max_place_val
            print(x)
            if x in (4,9,40,90,400,900):
                roman+=subtractive_forms[x]
            else:
                roman+=maximalSymbol(x)
            num = num%max_place_val
            max_place_val = max_place_val//10

        return roman    