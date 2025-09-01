import collections

class LRUCache:
    capacity: int
    cache: collections.OrderedDict
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        value: int = -1
        try:
            # updates usage
            value = self.cache.pop(key)
            self.cache[key] = value
        except:
            value = -1
        return value

    def put(self, key: int, value: int) -> None:
        try: 
            # updates usage
            self.cache.pop(key)
        except :
            if (len(self.cache)) >= self.capacity :
                # removes the LRU here
                self.cache.popitem(last=False)
        self.cache[key] = value

cache = LRUCache(2)
cache.put(2, 1)
cache.put(1, 1)
cache.put(2, 3)
cache.put(4, 1)
print(cache.get(1))       # returns -1 (not found)
print(cache.get(2))       # returns 3