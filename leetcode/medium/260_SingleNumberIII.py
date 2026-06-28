class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        dif_bit = 1
        while not (dif_bit & xor):
            dif_bit = dif_bit << 1

        a, b = 0, 0

        for num in nums:
            if num & dif_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]
