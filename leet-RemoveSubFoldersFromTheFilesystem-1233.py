from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if (len(folder)) <= 1:
            return folder
        folder.sort()
        retVal: List[str] = [folder[0]]
        lastRoot = folder[0] + "/"
        for i in range(1, len(folder)):
            try: 
                tempIndex: int = folder[i].index(lastRoot)
                if tempIndex != 0:
                    lastRoot = folder[i] + "/"
                    retVal.append(folder[i])    
            except:
                lastRoot = folder[i] + "/"
                retVal.append(folder[i])

        return retVal
    

thingy = Solution()

# ["/a","/c/d","/c/f"]
# print(thingy.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])) 

# ["/a"]
# print(thingy.removeSubfolders(["/a","/a/b/c","/a/b/d"])) 

# ["/a/b/c","/a/b/ca","/a/b/d"]
# print(thingy.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])) 


# print(thingy.removeSubfolders([])) 

# ["/c","/d/c/e"]
print(thingy.removeSubfolders(["/c","/d/c/e"])) 