# 构建一大于键值对数量的列表存储键值对
# 键的散列为索引
# 冲突发生时索引+1探测冲突直至命中或空索引（）


class LinearProbingHashST:
    def __init__(self, M=16):
        self.N = 0
        self.M = M
        self.list = []

    def _hash(self, key):
        return hash(key) % self.M

    def _resize(self, size):
        pass

    def put(self, key, val):
        if key is None:
            raise KeyError('cant be None')
        if N >= M / 2:
            self._resize(2 * M)
        index = self._hash(key)
        while self.list[index] is not None:
            k, v = self.list[index]
            if k == key:
                self.list[index] = [key, val]
                return
            index = self._hash(index + 1)
        self.list[index] = [key, val]
        N += 1

    def get(self, key):
        index = self._hash(key)
        while self.list[index] is not None:
            k, v = self.list[index]
            if k == key:

                return v
            index = self._hash(index + 1)
        return None
