# https://leetcode.com/problems/relative-sort-array/description/
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for num in arr1:
            count[num] = count.get(num, 0) + 1
        
        result = []
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]
        remaining = sorted([num for num in count.keys() for _ in range(count[num])])
        result.extend(remaining)

        return result