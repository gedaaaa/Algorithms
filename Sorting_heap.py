def sink(a, i, size):
    # 将一个位置不正确的元素下沉至大于其两个子节点

    while 2 * i + 1 < size:
        # print('父节点位置',i)
        # 左子节点没有越界
        # 判断父节点是否大于子节点
        j = 2 * i + 1
        if j + 1 < size:
            # 有右子节点
            print('最后一个堆有两个子节点')
            if j < size and a[j] < a[j + 1]:
                # 右子节点比左子节点大，标记
                print('右子节点大')
                j += 1
            if a[i] < a[j]:
                # 父节点不是最大的，和最大的子节点交换
                print('需要下沉')
                a[i], a[j] = a[j], a[i]
                print(a[i], a[j], a)
                # 标记异常元素的新位置
                i = j

            else:
                # 子节点小于父节点，因为是从堆底向上，父节点以下有序，位置正确
                print('父节点大于两个子节点')
                break

        elif j + 1 == size:
            # 没有右子节点（右子节点越界）
            # 直接比较两个节点大小
            print('最后一个堆有一个子节点')
            if a[i] < a[j]:
                print('需要下沉')
                a[i], a[j] = a[j], a[i]
                print(a[i], a[j], a)

            else:
                print('父节点大于子节点')
                break
        print('sink', a, i, size)


def sort(a):
    N = len(a)
    # 倒序遍历数组前一半的元素（后一半的元素在堆底，没有子节点）
    #
    for i in range(int((N - 2) / 2), -1, -1):
        print(i)

        sink(a, i, N)
        print(a)
    print('第一次构建结束')
    while N > 1:
        a[0], a[N - 1] = a[N - 1], a[0]
        print('堆顶已剔除', a)
        N -= 1
        sink(a, 0, N)
    return a


def heapsort(a):
    temp = [] + a
    print('temp', temp)
    return sort(temp)


if __name__ == '__main__':
    list = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    sortedlist = heapsort(list)
    print(sortedlist)
    print(list)
