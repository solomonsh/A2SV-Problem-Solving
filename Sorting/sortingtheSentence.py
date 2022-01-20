class Solution:

    # Approach one using selection sort
    # Time complexity N^2
    # Space complexity N
    def sortSentence(self, s: str) -> str:

        s_list = list(s.split(" "))

        for i in range(len(s_list)-1):
            for j in range(i+1, len(s_list)):
                if s_list[j][-1] < s_list[i][-1]:
                    s_list[j], s_list[i] = s_list[i], s_list[j]

        result = " ".join(s[0:len(s)-1] for s in s_list)

        return result

    # Approach two using counting sort
    # Time complexity N^2
    # Space complexity N

    def sortSentence2(self, s: str) -> str:

        s_list = list(s.split(" "))

        counts = [0] * (len(s_list))
        result = ""

        for word in s_list:
            index = int(word[-1])
            counts[index-1] = word[:-1]

        result = " ".join(counts)

        return result


sol = Solution()

s = "is2 sentence4 This1 a3"
sol.sortSentence2(s)
