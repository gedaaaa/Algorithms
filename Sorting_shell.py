# 希尔排序是一种改进的插入排序
# 数组内间隔为h的序列是有序的
# 不断缩小间隔直至1就达到了排序


def Shell(a):
    N = len(a)
    h = 1
    # 确定初始h
    while h < N / 3:
        h = 3 * h + 1
    while h >= 1:
        # 将数组变为h有序
        for i in range(h, N):
            print(a)
            # 将a[i]插入到a[i-h],a[i-2h]...中
            j = i - h
            while j >= 0:
                if a[j + h] < a[j]:
                    a[j + h], a[j] = a[j], a[j + h]
                j = j - h
        # h有序后更换更小的h
        h = int(h / 3)


if __name__ == '__main__':
    list = [
        'S',
        'H',
        'E',
        'L',
        'L',
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
    sortedlist = Shell(list)
    print(list)
