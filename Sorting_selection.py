def Selection(a):
    # 升序排列列表
    #
    N = len(a)
    for i in range(0, N):
        # 将a[i]和a[i+1...N]中最小的交换
        min = i  # 暂存最小的元素的索引
        for j in range(i + 1, N):
            if a[j] < a[min]:
                min = j  # 找到最小的元素并记录其索引
        a[i], a[min] = a[min], a[i]  # 遍历i之后所有元素后将最小的元素和a[i]交换
        # i+1后重复操作
    return a

if __name__ == '__main__':
    list = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    sortedlist=Selection(list)
    print(sortedlist)
    print(list)
