class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ds = [str(i) for i in digits]
        digit_str = str(eval(''.join(ds)) + 1)
        j = 0
        new_digits = []
        for item in digit_str:
            new_digits.append(int(item))
            j += 1
        return new_digits
