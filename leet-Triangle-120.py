from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(0, i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]
    


def main():
    thingy = Solution()
    print(thingy.minimumTotal([[-10]])) # -10
    print(thingy.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])) # 11
    # print(thingy.minimumTotal()) # 

if __name__ == "__main__":
    main()