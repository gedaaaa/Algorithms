def sink(list,i,size):
    # 未比较时父节点最大
    l=2*i+1
    r=2*i+2
    max=i
    # 元素不是堆底
    if i<size/2:
        # 先判定左子节点的大小
        if l<size and list[l]>list[max]:
            # 如果子节点大，标记它
            max=l
        # 再判定右子节点
        if r<size and list[r]>list[max]:
            # 如果右子节点比标记大，标记它
            max=r
        # 标记等于父节点时，两种情况1.父节点最大，2.没有子节点
        # 不等于父节点时，说明父节点位置错误，下沉
        # 再新的位置重新判定

        if max !=i:
            list[i],list[max]=list[max],list[i]
            sink(list,max,size)
def build(a):
    N=len(a)
    # 只有第一次有序化堆的时候，需要倒序遍历所有元素（前一半）
    for i in range(int(N/2-1),-1,-1):
        sink(a,i,N)
def heapsort(a):
    temp=[]+a
    build(temp)
    N=len(temp)
    # 因为每次只破坏堆顶一个元素，只要它的位置正确，整个堆就有序
    # 遍历的是堆的最后一个元素，也是有序部分的下个待排序位置
    for i in range(N-1,-1,-1):
        temp[i],temp[0]=temp[0],temp[i]
        sink(temp,0,i)
    return temp
if __name__ == '__main__':
    list = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    sortedlist = heapsort(list)
    print(sortedlist)
    print(list)