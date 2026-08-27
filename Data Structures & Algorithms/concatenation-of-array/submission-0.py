class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        input_length = len(nums)

        ans = [0] * (2 * input_length)

        for i, num in enumerate(nums):
            ans[i] = ans[i + input_length] = num
        
        return ans