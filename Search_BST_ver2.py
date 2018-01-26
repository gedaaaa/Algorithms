# 使用三叉链表，包含指向父节点的链接，方便记录路径
# 更python


class TreeNode():
    def __init__(self, key, val, left=None, right=None, parent=None):
        # 初始化键、值，左右子节点及父节点的默认值为None
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __iter__(self):
        # 迭代器
        if self:
            if self.hasLeftChild():
                for elem in self.left:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.right:
                    yield elem

    # 一系列辅助函数，包括
    # 是否 有左右子树
    # 是否 某个节点的左右子树
    # 是否 根节点
    # 是否 叶节点
    # 是否 有任何子树
    # 是否 有两个子树
    # 替换节点数据

    def hasLeftChild(self):
        return self.left

    def hasRightChild(self):
        return self.right

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not self.left and not self.right

    def hasAnyChild(self):
        return self.right or self.left

    def hasBothChild(self):
        return self.right and self.left

    def replaceData(self, key, val, left, right):
        # 将本节点的各个数据替换
        # 将子树的父节点指向更新后的节点
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChild():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.left
                else:
                    self.parent.rightChild = self.left
                self.left.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.right
                else:
                    self.parent.rightChild = self.right
                self.right.parent = self.parent

    def findSucc(self):
        succ = None
        if self.hasRightChild():
            succ = self.right.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current

    def findMax(self):
        current = self
        while current.hasRightChild():
            current = current.left
        return current

    def print(self):
        x = self
        if x.key is None:
            return
        if x is None:
            return
        if x.left is not None:
            x.left.print()
        print(x.key, x.val)
        if x.right is not None:
            x.right.print()


class BinarySearchTree:
    def __init__(self):
        # 初始化：根节点为空，大小为0
        self.root = None
        self.size = 0

    # 查询树的大小，并用magic methods
    def length(self):
        return self.size

    def __len__(self):
        return self.length

    def put(self, key, val):
        # 放入一个键值对
        # 使用一个对节点操作的私有方法完成迭代
        # 插入键小于当前键，在左子树插入，反之在右子树插入
        # 等于当前键时，更新当前值
        # 查询到空节点时，作为新节点插入
        # magic methods

        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.left)
            else:
                currentNode.left = TreeNode(key, val, parent=currentNode)
            self.size += 1
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.right)
            else:
                currentNode.right = TreeNode(key, val, parent=currentNode)
            self.size += 1
        else:
            currentNode.val = val

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        # 查找某个键对应的值
        # 同样使用私有方法
        # 小于当前键在左子树中迭代，大于当前键在右子树中迭代
        # 等于当前键返回当前节点
        # 查到空子树返回None
        if self.root:
            target = self._get(key, self.root)
            if target:
                return target.val
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key < key:
            return self._get(key, currentNode.right)
        else:
            return self._get(key, currentNode.left)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)

    def delete(self, key):
        # 删除某个键及其对应的值
        # 同样使用私有方法
        #
        if self.size > 1:
            # 先查找key，如果找到则调用私有方法
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self._remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('key not in tree')

    def _remove(self, nodeToRemove):
        # 三种情况
        # nodeToRemove没有子树
        # nodeToremove只有一个子树
        # nodeToremove有两个子树

        if nodeToRemove.isLeaf():
            # 无子树，删除父节点的引用
            if nodeToRemove.parent.left == nodeToRemove:
                nodeToRemove.parent.left = None
            else:
                nodeToRemove.parent.right = None

        elif nodeToRemove.hasBothChiled:
            # 有两棵子树
            # 找到继任者（右子树中的最小键）
            # 更新当前节点的键值为继任者键值
            # 剔除原先继任者
            succ = nodeToRemove.findsucc

            nodeToRemove.key = succ.key
            nodeToRemove.val = succ.val
            succ.spliceOut
        else:
            # 只有一棵子树
            # 更新父节点的对应子树引用到该子树，并更新子树的父节点
            if nodeToRemove.hasLeftChild():
                if nodeToRemove.isLeftChild():
                    nodeToRemove.left.parent = nodeToRemove.parent
                    nodeToRemove.parent.left = nodeToRemove.left
                elif nodeToRemove.isRightChild():
                    nodeToRemove.left.parent = nodeToRemove.parent
                    nodeToRemove.parent.right = nodeToRemove.left
                else:
                    nodeToRemove.replaceData(
                        nodeToRemove.left.key,
                        nodeToRemove.left.val,
                        nodeToRemove.left.left,
                        nodeToRemove.left.right)
            else:
                if nodeToRemove.isLeftChild():
                    nodeToRemove.right.parent = nodeToRemove.parent
                    nodeToRemove.parent.left = nodeToRemove.right
                elif nodeToRemove.isRightChild():
                    nodeToRemove.right.parent = nodeToRemove.parent
                    nodeToRemove.parent.right = nodeToRemove.right
                else:
                    nodeToRemove.replaceData(
                        nodeToRemove.right.key,
                        nodeToRemove.right.val,
                        nodeToRemove.right.left,
                        nodeToRemove.right.right)

    def print(self):

        self.root.print()



def inputer(list):
    st = BinarySearchTree()

    for word in list:

        if st.get(word) is None:
            st.put(word, 1)
        else:
            st.put(word, st.get(word) + 1)
    return st


if __name__ == "__main__":

    txt = "D:\\Code\\LearningPython\\Algorithms\\algs4-data\\Tale.txt"

    with open(txt, 'r') as f:
        t = f.read()

    l = t.split()

    bst = inputer(l)
    # a=bst.min().key
    # b=bst.max().key
    #
    # m=bst.min().val
    # n=bst.min().val

    # print(l,a,b,m,n)

    bst.print()

    # bst.deleteMax()
    #
    # bst.print()
    #
    # bst.deleteMin()
    #
    # bst.print()

    # bst.put('put',37)
    # bst.print()
