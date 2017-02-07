# http://www.lintcode.com/en/problem/longest-palindromic-substring/

# Given the string = "abcdzdcab", return "cdzdc"
class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s

        self.data = s
        self.data_length = len(s)
        self.max_len = 0
        self.result = None
        self.max_len2 = 0
        self.result2 = None

        index = self.search_pal(0)
        while index < self.data_length:
            index = self.search_pal(index)
        result1 = None if self.result is None else self.data[self.result[0]:self.result[1]+1]

        index = self.search_pal2(0)
        while index < self.data_length:
            index = self.search_pal2(index)
        result2 = None if self.result2 is None else self.data[self.result2[0]:self.result2[1]+1]

        print('result1=' + str(result1))
        print('result2=' + str(result2))
        #return max(0 if result1 is None else len(result1), 0 if result2 is None else len(result2))
        if result1 is None:
            return result2
        elif result2 is None:
            return result1
        else:
            return result1 if len(result1) > len(result2) else result2


    def search_pal2(self, index):
        left = index
        right = index + 1

        found = False

        while left >= 0 and right < self.data_length:
            if self.data[left] == self.data[right]:
                found = True
                left -= 1
                right += 1
            else:
                break

        if found:
            tmp_len = right - left - 1
            if tmp_len > self.max_len2:
                self.max_len2 = tmp_len
                self.result2 = (left + 1, right - 1)
            return right - 1
        else:
            return index + 1


    def search_pal(self, index):
        left = index - 1
        right = index + 1

        found = False

        while left >= 0 and right < self.data_length:
            if self.data[left] == self.data[right]:
                found = True
                left -= 1
                right += 1
            else:
                break

        if found:
            tmp_len = right - left - 1
            if tmp_len > self.max_len:
                self.max_len = tmp_len
                self.result = (left + 1, right - 1)
            return right - 1
        else:
            return index + 1

test_data = 'aaaa'
#test_data = 'abcdzdcab'
#test_data = ''
solution = Solution()
solution.longestPalindrome(test_data)

