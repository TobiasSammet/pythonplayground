from typing import List

class MyHashSet:
    myList: List[int]

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myList = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.myList.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key) :
            self.myList.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.myList
        


# Your MyHashSet object will be instantiated and called as such:
thing: MyHashSet = MyHashSet()
thing.add(1)
thing.add(2)
print(thing.contains(1)) #true
print(thing.contains(3)) #false (not found)
thing.add(2)
print(thing.contains(2)) #true
thing.remove(2)
print(thing.contains(2)) #false (already removed)