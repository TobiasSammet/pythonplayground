# Write an API that generates fancy sequences using the append, addAll, and multAll operations.
# Implement the Fancy class:
#     Fancy() Initializes the object with an empty sequence.
#     void append(val) Appends an integer val to the end of the sequence.
#     void addAll(inc) Increments all existing values in the sequence by an integer inc.
#     void multAll(m) Multiplies all existing values in the sequence by an integer m.
#     int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.

# Example 1:
# Input
# ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
# [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
# Output
# [null, null, null, null, null, 10, null, null, null, 26, 34, 20]

# Explanation
# Fancy fancy = new Fancy();
# fancy.append(2);   // fancy sequence: [2]
# fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
# fancy.append(7);   // fancy sequence: [5, 7]
# fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
# fancy.getIndex(0); // return 10
# fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
# fancy.append(10);  // fancy sequence: [13, 17, 10]
# fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
# fancy.getIndex(0); // return 26
# fancy.getIndex(1); // return 34
# fancy.getIndex(2); // return 20

# Constraints:
#     1 <= val, inc, m <= 100
#     0 <= idx <= 10^5
#     At most 10^5 calls total will be made to append, addAll, multAll, and getIndex.

# we're going to store all the operations and only perform them when necessary
# BTW this gives a TLE in Python -- but the same code is ok in typescript :P
class Fancy:
    __values = []
    __operations = []
    def __init__(self):
        pass        

    def append(self, val: int) -> None:
        self.__values.append((val, len(self.__operations)))

    def addAll(self, inc: int) -> None:
        self.__operations.append(('a', inc))

    def multAll(self, m: int) -> None:
        self.__operations.append(('m', m))

    def getIndex(self, idx: int) -> int:
        modulo: int = 1e9 + 7
        if idx >= len(self.__values):
            return -1
        ret_val: int = self.__values[idx][0]
        start_index: int = self.__values[idx][1]
        for i in range(start_index, len(self.__operations)):
            operation, value = self.__operations[i]
            if operation == "a":
                ret_val += value
            else:
                ret_val = (int)((ret_val * value) % modulo)
        # cache the value for next time!
        self.__values[idx] = (ret_val, len(self.__operations))
        return int(ret_val)


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)

def main():
    fancy = Fancy()
    fancy.append(2); # fancy sequence: [2]
    fancy.addAll(3); # fancy sequence: [2+3] -> [5]
    fancy.append(7); # fancy sequence: [5, 7]
    fancy.multAll(2); # fancy sequence: [5*2, 7*2] -> [10, 14]
    assert fancy.getIndex(0) == 10, "Test Case Failed" # return 10
    fancy.addAll(3); # fancy sequence: [10+3, 14+3] -> [13, 17]
    fancy.append(10); # fancy sequence: [13, 17, 10]
    fancy.multAll(2); # fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
    assert fancy.getIndex(0) == 26, "Test Case Failed" # return 26
    assert fancy.getIndex(1) == 34, "Test Case Failed" # return 34
    assert fancy.getIndex(2) == 20, "Test Case Failed" # return 20



if __name__ == "__main__":
    main()