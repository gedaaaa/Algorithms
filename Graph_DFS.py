from Graph import Graph as G


class DepthFirstSearch():
    def __init__(self, graph, s):
        self.graph = graph
        self.s = s
        self.marked = []
        self.count = 0
        self._dfs(self.graph, self.s)
        if not isinstance(self.graph, G):
            raise TypeError

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


if __name__ == '__main__':
    txt = "D:\\Code\\LearningPython\\Algorithms\\algs4-data\\TinyG.txt"
    graphTest = G(0)
    graphTest.importTxt(txt)
    DepthFirstSearch(graphTest, 0)
