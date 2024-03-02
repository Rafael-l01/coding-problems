class MyHashSet(object):

    def __init__(self):
        self.hashSet = [None] * 1000001

    def __hash(self, key):
        hash = key % len(self.hashSet)
        return hash

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.__hash(key)

        if self.hashSet[index] == None:
            self.hashSet[index] = []

        if self.contains(key):
            return

        self.hashSet[index].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.__hash(key)

        if self.hashSet[index] is not None:
            for i, recordKey in enumerate(self.hashSet[index]):
                if recordKey == key:
                    del self.hashSet[index][i]
                    return

        return

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = self.__hash(key)

        if self.hashSet[index] is not None:
            for recordKey in self.hashSet[index]:
                if recordKey == key:
                    return True

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
