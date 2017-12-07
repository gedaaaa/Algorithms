import random


def partition(a, lo, hi):
    i, j, key = lo, hi, a[lo]
    # 用key记录关键值
    # 每次检测到异常值都把异常值直接复制到上一个异常值的位置
    # 每复制一次异常值就换一个方向实现异常值的交换
    # 初始的异常值就是key
    # 双向指针碰头的位置上一定是一个刚刚被复制的异常值
    # 用key替换它

    # 不进行复制也可以等两侧都检测出来后直接交换
    # 和ver1一样,最后将lo,a[j]交换
    print('子数组为', a[lo:hi + 1])
    while i < j:
        while i < j and key <= a[j]:
            j -= 1
            print('j-1', i, j)
        a[i] = a[j]
        while i < j and key >= a[i]:
            i += 1
            print('i+1', i, j)
        a[j] = a[i]
        print('a', a)
    a[j] = key
    return j


def quicksort(a, lo, hi):
    if hi <= lo:
        print('好短', a)
        return a
    j = partition(a, lo, hi)
    quicksort(a, lo, j - 1)
    quicksort(a, j + 1, hi)


def sort(a):
    temp = random.sample(a, len(a))
    print('temp', temp)
    quicksort(temp, 0, len(a) - 1)
    return temp


if __name__ == '__main__':
    list = [
        'Q',
        'U',
        'I',
        'C',
        'K',
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
    sorted = sort(list)
    print(sorted)
