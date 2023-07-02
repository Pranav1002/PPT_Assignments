class Solution:
    def reverseWords(self, s: str) -> str:

        l = s.split()

        for i in range(len(l)):
            l[i] = l[i][::-1]

        l = ['{0} '.format(elem) for elem in l]

        st = ''.join(l)
        st = st.rstrip()
        
        return st