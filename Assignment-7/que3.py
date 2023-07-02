class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        def str_to_int(num):

            dic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

            ans = 0

            for d in num:
                ans = ans*10 + dic[d]
            return ans
        print(str_to_int(num1) + str_to_int(num2))

        return str(str_to_int(num1) + str_to_int(num2))