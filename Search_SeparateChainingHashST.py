#基于拉链法的散列表
class SeparateChainingHashST:
    def __init__(self,M=97):
        self._num=M
        self._list=[]
        for _ in range(self._num):
            self._lsit.append([])

    def _hash(self,key):
        return hash(key)%self._num
    def get(self,key):
        index=self._hash(key)
        for k,v in self._list[index]:
            if k == key:
                return v
            else:
                raise KeyError('{} not fond'.format(key))
    def del(self,key):
        index=self._hash(key)
        for k,v in self._list[index]:
            if k==key:
                self._list.remove([k,v])
            else:
                raise KeyError('{} not fond'.format(key))
    def put(self,key,value):
        index=self._hash(key)
        for i,(k,v) in enumerate(self._list[index]):#枚举，i递增，同时每个i对应一个元素，对这个例子，元素的结构是k,v
            if k == key:
                self._list[index][i]=[key,value]
                break
            else:
                self._list[index].append([key,value])



    def keys(self):#获取所有的key,实现.next(),可以同样实现values和items
        for index in range(self.num):
            for k,v in self._list[index]:
                yield k