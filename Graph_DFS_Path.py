from Graph import Graph as G
class DepthFirstPaths():
    def __init__(self, graph, s):
        self.graph = graph
        self.s = s
        self.marked = []
        self.edgeTo = {}
        self.count = 0
        self._dfs(self.graph, self.s)
        if not isinstance(self.graph, G):
            raise TypeError

    def _dfs(self, G, v):
        self.marked.append(v)
        self.count += 1
        for w in G.bag[v]:
            if w not in self.marked:
                self.edgeTo[w] = v
                self._dfs(G, w)

    def hasPathTo(self, v):
        if v in self.marked:
            return True
        else:
            return False
    def pathTo(self,v):
        if not self.hasPathTo(v):
            return
        path=[]
        x=v
        while x != self.s:
            path.append(x)
            x=self.edgeTo[x]
        path.append(self.s)
        return path

if __name__ == '__main__':
    txt = "D:\\Code\\LearningPython\\Algorithms\\algs4-data\\TinyG.txt"
    graphTest = G(0)
    graphTest.importTxt(txt)
    paths=DepthFirstPaths(graphTest,0)
    print(paths.edgeTo)
    print(paths.hasPathTo(10))
    print(paths.hasPathTo(4))
    print(paths.pathTo(3))