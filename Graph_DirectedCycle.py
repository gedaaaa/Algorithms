from Graph_DiGraph import DiGraph as G

'''寻找有向图中的有向环
由于环的数量可能是图大小的指数级别
因此找到一个有向环即可

维护一个数组onStack
在每次调用dfs时将对应的顶点放入
调用结束去除
调用中遇到在onStack上时即为环
利用edgeTo给出环上的路径'''


class DirectedCycle():
    def __init__(self, graph):
        self.graph = graph

        self.marked = []
        self.edgeTo = {}
        self.cycle = []
        self.onstack = []
        if not isinstance(self.graph, G):
            raise TypeError

        for v in range(self.graph.V):
            if self.hasCycle():
                break
            if v not in self.marked:
                self._dfs(self.graph, v)

    def _dfs(self, G, v):
        self.marked.append(v)
        self.onstack.append(v)

        print('现在的顶点', v)
        print(self.marked)

        for w in G.bag[v]:
            print('尝试目标顶点', w)
            if self.hasCycle():
                # 每次都从方法中判定是否消耗性能过多？
                print('找到环')
                break

            elif w not in self.marked:
                print('当前边', v, ' - ', w)
                self.edgeTo[w] = v
                self._dfs(G, w)
            # 找到环后记录环上路径
            elif w in self.onstack:
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edgeTo[x]
                self.cycle.append(w)
                self.cycle.append(v)
            print('回退到', v)
        self.onstack.remove(v)

    def hasCycle(self):
        if self.cycle:
            return True
        else:
            return False


if __name__ == '__main__':
    txt = "D:\\Code\\LearningPython\\Algorithms\\algs4-data\\TinyDG.txt"
    graphTest = G(0)
    graphTest.importTxt(txt)
    a = DirectedCycle(graphTest).cycle
    print(a)
