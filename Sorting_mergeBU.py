# 自底向上归并：现将数组分割为单元素小数组，两两归并，在两两归并双元素数组，直至整个数组归并
# def Merge(a, lo, mid, hi):
#     # 归并的核心操作
#     aux = [] + a[lo:hi + 1]
#     i = lo
#     j = mid + 1
#
#     # 归并至原数组
#     for k in range(lo, hi + 1):
#         # 左边元素用尽则取右边最小元素
#         if i > mid:
#             a[k] = aux[j-lo]
#             j += 1
#         # 右边元素用尽则取左边最小元素
#         elif hi < j:
#             a[k] = aux[i-lo]
#             i += 1
#         # 右侧元素比左侧元素大取左侧元素
#         elif aux[i-lo] < aux[j-lo]:
#             a[k] = aux[i-lo]
#             i += 1
#         # 左侧元素比右侧元素不大取右侧元素
#         else:
#             a[k] = aux[j-lo]
#             j += 1
#

from Sorting_merge import Merge as Merge
# 这个Merge更python


def MergeBU(a):
    N = len(a)
    result = a.copy()

    # 初始数组大小为1,以2的次方递增
    def sz_list():
        n = 0
        while True:
            sz = 2**n
            yield sz  # 生成器
            n += 1

    for x in sz_list():

        if x < N:

            # 对每个小于总长度数组尺寸都进行归并
            for lo in range(0, N - 1, x + x):
                mid = lo + x
                hi = min(lo + x + x, N)
                print(result[lo:mid], result[mid:hi])
                result[lo:hi] = Merge(result[lo:mid], result[mid:hi])
        else:
            break

    return result


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
        'E', '.', '.', '.']

    print(MergeBU(list))
    print(list)
