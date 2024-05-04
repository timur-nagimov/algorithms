import random


class RandomizedSet:

    def __init__(self):
        self.set_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.set_dict:
            return False
        self.set_dict[val] = True
        return True

    def remove(self, val: int) -> bool:
        if val in self.set_dict:
            self.set_dict.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.set_dict.keys()))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
