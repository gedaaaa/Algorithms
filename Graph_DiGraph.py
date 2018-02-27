class DiGraph:
    """初始V个顶点，没有边
    实现了
    插入边
    从文件导入图
    某个顶点的度数
    最大度数"""

    def __init__(self, V=0, E=0):
        self.V = V
        self.E = E
        self.bag = {}  # 以字典作为邻接表的基础

    def addEdge(self, v, w):
        """与无向图不同，仅添加一次变"""
        if v not in self.bag:
            self.bag[v] = []
            self.V += 1
        self.bag[v].append(w)

        if w not in self.bag:
            self.bag[w] = []
            self.V += 1
        # self.bag[w].append(v)
        self.E += 1

    def importTxt(self, txt):
        '''从一个txt文件中读入一个有向图
        格式为：
        第一二行无效（顶点个数和边数，可以自动生成）
        随后每行为两个顶点，空格切分
        顶点用整数表示'''
        i = 0
        with open(txt, 'r') as f:
            for line in f:
                if i <= 1:
                    i += 1

                else:
                    t = line.split()
                    v, w = t
                    v,w=int(v),int(w)
                    self.addEdge(v, w)
                    i += 1

    def degree(self, v):
        vNeighbor = self.bag[v]
        degree = len(vNeighbor)
        return degree

    def maxDegree(self):
        temp = 0
        for v in self.bag:
            nowDegree = self.degree(v)
            temp = max(nowDegree, temp)
        return temp

    def toString(self):
        s = str(self.V) + '个顶点，' + str(self.E) + '条边。\n'

        v = 0
        while v < self.V:
            s += str(v) + ':'
            for w in self.bag[v]:
                s += str(w) + ' '
            s += '\n'
            v += 1
        return s

    def reverse(self):
        R=DiGraph()
        v=0
        while v<self.V:
            for w in self.bag[v]:
                R.addEdge(w,v)
            v+=1
        return R
if __name__ == '__main__':
    txt = "D:\\Code\\LearningPython\\Algorithms\\algs4-data\\TinyDG.txt"
    graphTest = DiGraph()
    graphTest.importTxt(txt)
    a = graphTest.bag
    b = graphTest.degree(10)
    c = graphTest.maxDegree()
    d = graphTest.toString()
    reverse=graphTest.reverse()
    e=reverse.toString()
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)