from Search_BST_ver2 import TreeNode as TN


# 删除操作需要补充


class RedBlackNode(TN):
    # 红黑树的节点，较二叉树节点多一个连接颜色属性
    # 表示指向自己的链接的颜色
    def __init__(self, key, val, left=None, right=None, color='BLACK'):
        TN.__init__(self, key, val, left, right)
        self.color = color

    def isRed(self):
        return self.color == 'RED'

    def rotateLeft(self):
        # 将一个右斜红链接旋转为左斜
        # 交换红链接两端两个节点，将3个子节点的中间节点转移到新出现的连接上
        x = self.right
        self.right = x.left
        x.left = self
        x.color = self.color
        self.color = 'RED'
        return x

    def rotateRight(self):
        x = self.left
        self.left = x.right
        x.right = self
        x.color = self.color
        self.color = 'RED'
        return x

    def flipColors(self):
        self.color = 'RED'
        self.left.color = 'BLACK'
        self.right.color = 'BLACK'

    def is23(self):
        x = self

        if x is None:
            return True
        if x.left is not None:
            return self.left.is23()
        if x.right and x.right.isRed():
            print('not RBT', x.key)
            return False
        elif x.left and (x.left.left or x.left.right) and x.left.isRed() and (x.left.left.isRed() or x.left.right.isRed()):
            print('not RBT', x.key)
            return False
        elif x.right and x.left and x.left.isRed() and x.right.isRed():
            print('not RBT', x.key)
            return False
        elif x.right and (x.right.right or x.right.left) and x.right.isRed() and (x.right.left.isRed() or x.right.right.isRed()):
            print('not RBT', x.key)
            return False
        else:
            return True
        if x.right is not None:
            return self.right.is23()


class RBTree(object):
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
        if self.root:
            self.root = self._put(key, val, self.root)
            self.root.color = 'BLACK'
        else:
            self.root = RedBlackNode(key, val)

    def _put(self, key, val, currentNode):
        if currentNode is None:
            currentNode = RedBlackNode(key, val, None, None, 'RED')

        if key < currentNode.key:
            currentNode.left = self._put(key, val, currentNode.left)
        elif key > currentNode.key:
            currentNode.right = self._put(key, val, currentNode.right)
        else:
            currentNode.val = val

        # 插入完成后，红链接应向上转移
        # 因此在递归后进行检测
        # 左右连红则左旋转，有可能转变为二连左红
        # 二连左红右旋转，转变为左右双红
        # 左右双红则变色将红链接进一步传递
        if currentNode.right and currentNode.right.isRed() and (
                (currentNode.left and not currentNode.left.isRed()) or not currentNode.left):
            currentNode = currentNode.rotateLeft()

        elif currentNode.left and currentNode.left.left and currentNode.left.isRed() and currentNode.left.left.isRed():
            currentNode = currentNode.rotateRight()
        elif currentNode.left and currentNode.right and currentNode.left.isRed() and currentNode.right.isRed():
            currentNode.flipColors()
        return currentNode

    def print(self):

        self.root.print()

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

    def _get(self, key, currentNode):
        if currentNode is None:
            return None
        if currentNode.key == key:
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


def inputer(list):
    st = RBTree()

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
    bst.root.is23()
    if bst.root.is23():
        print('是23树')
