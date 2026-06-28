from typing import List

class Solution:
    def minJumps(self, arr: List[int]):
        length = len(arr)
        if length == 1:
            return 0
        
        # Create a map of values to their indices
        jumps = {}
        for i in range(length):
            tempVal = arr[i]
            if tempVal in jumps:
                jumps[tempVal].append(i)
            else:
                jumps[tempVal] = [i]
    
        # BFS
        current_count = 0
        bfs = [0]
        visited = [False] * length
    
        while True:
            if max(bfs) == length - 1:
                break
                
            temp_bfs = []
            for item in bfs:
                if not visited[item]:
                    temp_val = arr[item]
                    visited[item] = True
                    
                    # Move to next index
                    if item + 1 < length and not visited[item + 1]:
                        temp_bfs.append(item + 1)
                    
                    # Move to previous index
                    if item - 1 >= 0 and not visited[item - 1]:
                        temp_bfs.append(item - 1)
                    
                    # Jump to all indices with same value
                    if temp_val in jumps:
                        for jump in jumps[temp_val]:
                            if not visited[jump]:
                                temp_bfs.append(jump)
            
            bfs = temp_bfs
            current_count += 1
    
        return current_count
        
def main():
    thingy = Solution()
    assert thingy.minJumps(arr = [100,-23,-23,404,100,23,23,23,3,404]) == 3, "Test Case Failed"
    assert thingy.minJumps(arr = [7]) == 0, "Test Case Failed"
    assert thingy.minJumps(arr = [7,6,9,6,9,6,9,7]) == 1, "Test Case Failed"
    # assert thingy.minJumps() == , "Test Case Failed"


if __name__ == "__main__":
    main()