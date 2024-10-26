# https://leetcode.com/problems/flipping-an-image/submissions/1433909497/
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = list(map(lambda x:1 if x == 0 else 0, image[i]))[::-1]
        return image
