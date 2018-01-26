# 构建一大于键值对数量的列表存储键值对
# 键的散列为索引
# 冲突发生时索引+1探测冲突直至命中或空索引（）


class LinearProbingHashST:
    def __init__(self, M=16):
        self.N = 0  # 键值对数量
        self.M = M  # 散列表大小
        self.list = []

    def _hash(self, key):
        return hash(key) % self.M

    def _resize(self, size):
        t = LinearProbingHashST(size)
        for i in range(self.M):
            if self.list[i] is not None:
                k, v = self.list[i]
                t.put(k, v)
        self.list = t
        self.M = t.M

    def put(self, key, val):
        if key is None:
            raise KeyError('cant be None')
        if self.N >= self.M / 2:
            self._resize(2 * self.M)
        index = self._hash(key)
        while self.list[index] is not None:
            k, v = self.list[index]
            if k == key:
                self.list[index] = [key, val]
                return
            index = self._hash(index + 1)  # +1再散列实现了自动回到头部
        self.list[index] = [key, val]
        self.N += 1

    def get(self, key):
        index = self._hash(key)
        while self.list[index] is not None:
            k, v = self.list[index]
            if k == key:

                return v
            index = self._hash(index + 1)
        return None

    def delete(self, key):  # 删除后需要将键簇内右部的元素重新插入
        if self.get(key) is None:
            return
        index = self._hash(key)
        k, v = self.list[index]
        while k != key:
            index = self._hash(index + 1)
        self.list[index] = None
        # 重新插入时一定在原来的键簇范围内？
        index = self._hash(index + 1)
        while self.list[index] is not None:
            kToDo, vToDo = self.list[index]
            self.list[index] = None
            self.N -= 1
            self.put(kToDo, vToDo)
            index = self._hash(index + 1)
        self.N -= 1
        if self.N > 0 and self.N < self.M / 8:
            self.resize(self.M / 2)
