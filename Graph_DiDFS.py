from Graph_DiGraph import DiGraph

'''利用可变参数，实现多点可达性
每个顶点对自己都是可达的'''


class DepthFirstSearch():
    def __init__(self, graph, *args):
        self.graph = graph
        self.marked = []
        self.count = 0
        if not isinstance(self.graph, DiGraph):
            raise TypeError
        self.nodes = []
        for s in args:
            self.nodes.append(s)
        self._dfs_mutliNodes(self.graph, self.nodes)
    def _dfs(self, G, v):
        self.marked.append(v)
        self.count += 1
        print('现在的顶点', v)
        print(self.marked)
        for w in G.bag[v]:

            print('尝试目标顶点', w)
            if w not in self.marked:
                print('当前边', v, ' - ', w)
                self._dfs(G, w)
            print('回退到', v)

    def _dfs_mutliNodes(self, G, vList):
        for s in vList:
            if s not in self.marked:
                self._dfs(G, s)


if __name__ == '__main__':
    txt = "D:\\Code\\LearningPython\\Algorithms\\algs4-data\\TinyDG.txt"
    graphTest = DiGraph(0)
    graphTest.importTxt(txt)
    DepthFirstSearch(graphTest, 0)
    a=DepthFirstSearch(graphTest,1,2,6)
    print(a.marked)
