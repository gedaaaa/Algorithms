# 归并排序是基于将两个有序数组归并成一个新的有序数组的操作
# 通过递归调用实现


def Merge(left, right):
    #print(left,right)
    # 归并的核心操作
    result = []
    i, j = 0, 0
    # 归并至原数组
    while i < len(left) and j < len(right):
        # 右侧元素比左侧元素大取左侧元素
        if left[i] < right[j]:
            result += left[i]
            i += 1
        # 左侧元素比右侧元素不大取右侧元素
        else:
            result += right[j]
            j += 1
    # 左边元素用尽则直接添加右边
    result+=right[j:]

    # 右边元素用尽则直接添加左边
    result+=left[i:]
    #print(result)
    return result


def Sort(a):
        # 递归
        mid=int(len(a)/2)
        if len(a)<=1:
            # print('N<2',a)
            return a
        left=Sort(a[:mid])
        right=Sort(a[mid:])
        #print('l,r',left,right)
        return Merge(left,right)







if __name__ == '__main__':
    list = [
        'M',
        'E',
        'R',
        'G',
        'E',
        'S',
        'O',
        'R',
        'T',
        'E',
        'X',
        'A',
        'M',
        'P',
        'L',
        'E']

    sortedlist=Sort(list)
    print(list)
    print(sortedlist)


