class Solution:
    def addBinary(self, a: str, b: str) -> str:
        str1 = a[::-1]
        str1_sum = 0
        for i in range(len(str1)):
            str1_sum += (2**i)*int(str1[i])

        str2 = b[::-1]
        str2_sum = 0
        for i in range(len(str2)):
            str2_sum += (2**i)*int(str2[i])

        total = str1_sum+str2_sum
        binary = ""

        if total==0:
            return "0"
        else:
            while total!=0:
                binary+=str(total%2)
                total = total//2

            return binary[::-1]


        