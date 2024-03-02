class MyHashMap(object):

    def __init__(self):
        self.hashMap = [None] * 1000001

    def __hash(self, key):
        hash = key % len(self.hashMap)
        return hash

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self.__hash(key)

        if self.hashMap[index] == None:
            self.hashMap[index] = []

        for i, pair in enumerate(self.hashMap[index]):
            recordKey, recordValue = pair
            if recordKey == key:
                self.hashMap[index][i] = [key, value]
                return

        self.hashMap[index].append([key, value])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = self.__hash(key)

        if self.hashMap[index] is not None:
            for pair in self.hashMap[index]:
                recordKey, recordValue = pair
                if recordKey == key:
                    return recordValue

        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.__hash(key)

        if self.hashMap[index] is not None:
            for i, pair in enumerate(self.hashMap[index]):
                recordKey, recordValue = pair
                if recordKey == key:
                    del self.hashMap[index][i]
                    return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
