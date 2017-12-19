import os


# 需要着重注意 None type 无法做很多操作，需要自行限定
# 方法需要括号！！！


class Node():
    def __init__(self, key, val, n=0, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.n = n

    def size(self):
        x = self
        if x is None:
            return 0
        else:
            return x.n

    def get(self, key):
        # 递归，直至x==None 或者x.key==key
        x = self
        if x is None:
            return None
        if x.key is None:
            return None
        if key < x.key:
            if x.left is None:
                x.left = Node(None, None, 0)
            return x.left.get(key)
        elif key > x.key:
            if x.right is None:
                x.right = Node(None, None, 0)
            return x.right.get(key)
        else:
            return x.val

        # 在x为根节点的子树中查找key
        # 找到则更新val
        # 没有找到时在空节点处插入它
    def put(self, key, val):
        # 递归，直至x == None
        # 或者x.key == key
        # 在空键处生成新的节点
        x = self
        if x is None:
            a = Node(key, val, 1)
            return a
        if x.key is None:
            a = Node(key, val, 1)
            return a
        if key < x.key:
            if x.left is None:
                x.left = Node(None, None, 0)
            x.left = x.left.put(key, val)
        elif key > x.key:
            if x.right is None:
                x.right = Node(None, None, 0)
            x.right = x.right.put(key, val)
        else:
            x.val = val
        if x.left is not None and x.right is not None:
            x.n = x.left.size() + x.right.size() + 1
        elif x.left is not None:
            x.n = x.left.size() + 1
        elif x.right is not None:
            x.n = x.right.size() + 1
        else:
            x.n = 1
        # print(x.n)
        return x

    # max和min：沿一边子节点查找至最后
    def max(self):
        x = self
        if x.right is None:
            return x
        return x.right.max()

    def min(self):
        x = self
        if x.left is None:
            return x
        return x.left.min()

        # 向下取整，小于key的最大键
    def floor(self, key):
        x = self
        if x is None:
            return None
        if key == x.key:
            return x
        if key < x.key:
            # key小于根节点，在左子树中查找
            # 要么不存在，要么在左子树里
            return x.left.floor(key)
        # key大于根节点，在右子树中查找
        # 如果不存在，则根节点为目标
        t = x.right.floor(key)
        if t is not None:
            return t
        else:
            return x

            # 向上取整，和floor一致
    def ceiling(self, key):
        x = self
        if x is None:
            return None
        if key == x.key:
            return x
        if key > x.key:
            # key大于根节点，在右子树中查找
            # 要么不存在，要么在右子树里
            return x.right.ceiling(key)
        # key小于根节点，在左子树中查找
        # 如果不存在，则根节点为目标
        t = x.left.ceiling(key)
        if t is not None:
            return t
        else:
            return x

            # 找到排名为k的键
    def select(self, k):
        # 返回排名为k的节点
        x = self
        if x is None:
            return None
        # 左子树大小为t
        t = x.left.size
        if t > k:
            # t>k,在左子树中递归
            return x.left.select(k)
        elif t < k:
            # t>k,在右子树中查找排名k-t-1的键
            return x.right.select(k - t - 1)
        else:
            return x

    def rank(self, key):
        x = self
        if x is None:
            return 0
        # 给定的键小于根节点，在左子树中递归
        if key < x.key:
            return x.left.rank(key)
        # 给定的键大于根节点，返回t+1（根节点的排名）+右子树中的排名
        elif key > x.key:
            return 1 + x.left.size() + x.right.rank(key)
        # 相等时返回根节点的左子树的大小
        else:
            return x.left.size()

    def deleteMin(self):
        x = self
        # 左子树为空时，该根节点为最小键
        # 将链接指向右子树
        if x.left is None:
            return x.right
        # 左子树不为空，递归,维护节点长度
        x.left = x.left.deleteMin()
        if x.left is not None and x.right is not None:
            x.n = x.left.size() + x.right.size() + 1
        elif x.left is not None:
            x.n = x.left.size() + 1
        elif x.right is not None:
            x.n = x.right.size() + 1
        else:
            x.n = 1
        return x

    def deleteMax(self):
        x = self
        # 右子树为空时，该根节点为最小键
        # 将链接指向左子树
        if x.right is None:
            return x.left
        # 右子树不为空，递归,维护节点长度
        x.right = x.right.deleteMax()
        if x.left is not None and x.right is not None:
            x.n = x.left.size() + x.right.size() + 1
        elif x.left is not None:
            x.n = x.left.size() + 1
        elif x.right is not None:
            x.n = x.right.size() + 1
        else:
            x.n = 1
        return x

    def delete(self, key):
        x = self
        if x is None:
            return None
        # 未找到key时递归
        if key < x.key:
            x.left = x.left.delete(key)
        elif key > x.key:
            x.right = x.right.delete(key)
            # 找到key后，若只有一边节点，将自己的链接指向剩余的节点完成删除
            if x.right is None:
                return x.left
            elif x.left is None:
                return x.right
            # 两个子节点都存在时
            # 四步
            # 1.保存待删除节点x及其后面的链接为t
            # 2.将x指向后继节点--min(t.right)
            # 3.将x的右链接重设为deleteMin(t.right)
            # 4.将x的左链接重设为t.left
            else:
                t = x
                x = t.right.min()
                x.right = t.right.deleteMin()
                x.left = t.left
            # 维护长度
            if x.left is not None and x.right is not None:
                x.n = x.left.size() + x.right.size() + 1
            elif x.left is not None:
                x.n = x.left.size() + 1
            elif x.right is not None:
                x.n = x.right.size() + 1
            else:
                x.n = 1
            return x

    def print(self):
        x=self
        if x.key is None:
            return
        if x is None:
            return
        if x.left is not None:
            x.left.print()
        print(x.key,x.val)
        if x.right is not None:
            x.right.print()

class BST():
    def __len__(self):
        return self.root.size()

    def __init__(self):
        self.root = Node(None, None, 0)

    def length(self):

        return self.root.size()

    def get(self, key):
        # 以x为根节点的子树中查找并返回key对应的val
        return self.root.get(key)

    def put(self, key, val):
        print(key,'+1=',val)

        self.root = self.root.put(key, val)

    def max(self):
        return self.root.max()

    def min(self):
        return self.root.min()

    def floor(self, key):

        x = self.root.floor(key)
        if x is None:
            return None
        return x.key

    def ceiling(self, key):
        x = self.root.ceiling(key)
        if x is None:
            return None
        return x.key

    def select(self, k):
        return self.root.select(k).key

    def rank(self, key):
        return self.root.rank(key)

    def delete(self, key):
        self.root = self.root.delete(key)

    def deleteMin(self):
        self.root = self.root.deleteMin()

    def deleteMax(self):
        self.root = self.root.deleteMax()

    def keys(self):
        pass

    def print(self):

        self.root.print()


def inputer(list):
    st = BST()

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
    a=bst.min().key
    b=bst.max().key

    m=bst.min().val
    n=bst.min().val

    print(l,a,b,m,n)

    bst.print()

    bst.deleteMax()

    bst.print()

    bst.deleteMin()

    bst.print()

    bst.put('put',37)
    bst.print()
    # st = BST()
    # st.put(1, 'a')
    # st.put(2, 'b')
    # st.put(3, 'c')
    # st.put(4, 'd')
    # st.put(5, 'e')
    # st.put(6, 'f')
    # st.put(7, 'g')


