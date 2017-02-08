# http://www.lintcode.com/en/problem/maximum-average-subarray/
# http://mathoverflow.net/questions/112422/largest-subarray-with-average-geq-k

#Given nums = [1, 12, -5, -6, 50, 3], k = 3
#Return 15.667 // (-6 + 50 + 3) / 3 = 15.667

class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):
        self.data = nums
        self.data_length = len(nums)
        result = self.loopData(k)
        return result

    def loopData(self, k):
        max_avg = self.calcAvg(0, k)
        #prev_val = self.data[0]

        for index in range(self.data_length - k + 1):
            #curr_val = self.data[index]
            #if curr_val < prev_val:
            #    print('skip {} at index {}'.format(curr_val, index))
            #    continue

            #prev_val = curr_val
            tmp_avg = self.loopDataIndex(index, k)
            max_avg = max(max_avg, tmp_avg)
        
        return max_avg

    def loopDataIndex(self, index, k):
        max_avg = self.calcAvg(index, k)
        for step in range(k, self.data_length - index + 1):
            tmp = self.data[index + step - 1]
            if tmp < max_avg: 
                continue

            tmp_avg = self.calcAvg(index, step)
            max_avg = max(max_avg, tmp_avg)
        return max_avg

    def calcAvg(self, index, length):
        total = float(0)
        for index in range(index, index+length):
            total += self.data[index]

        return total / length
        


solution = Solution()
result = solution.maxAverage([1,12,-5,-6,50,3], 3)
print(result)

