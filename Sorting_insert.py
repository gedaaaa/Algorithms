# 将a[i]及其之前的元素两两对比，将更小的元素放到前面以达到有序和插入的目的
# 每次开始时a[i]左侧的元素都已经有序
def InsertSorting(a):
    N = len(a)
    for i in range(1, N):
        print(a)
        j = i - 1
        while j >= 0:
            if a[j + 1] < a[j]:
                a[j + 1], a[j] = a[j], a[j + 1]
            j = j - 1



if __name__ == '__main__':
    list = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    print(list)
    InsertSorting(list)

    print(list)
