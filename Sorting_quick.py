# 快速排序
# 将数组分成两部分，每部分各自排序
# 分类的依据是左侧都小于一个值，右侧大于该值
# 判定时
# 如果==的情况不停止，可以从lo开始
# 如果==的情况也停止，要从lo+1开始
# 如果==不停止，似乎会在特定情况下造成性能损失

import random


def partition(a, lo, hi):
    # 将列表切分为a[lo:i+1],a[i],a[i+1:hi+1]
    print(a,lo,hi)
    i, j = lo, hi
    key = a[lo]
    while True:
        print('true')
        while a[i] <= key:
            if i == hi:
                print('i==hi')
                break
            i += 1
            print('i now',i)
        while a[j] >= key:
            if j == lo:
                print('j==lo')
                break
            j -= 1
            print('j now',j)
        if i >= j:
            print(i>=j)
            break
        a[i], a[j] = a[j], a[i]
        print('sorting',a[lo:hi+1])

    a[lo], a[j] = a[j], a[lo]
    return j


def quicksort(a, lo, hi):
    if hi <= lo:
        return
    j = partition(a, lo, hi)
    print(a[lo:hi+1],'j',j)
    quicksort(a, lo, j - 1)
    quicksort(a, j + 1, hi)


def sort(a):
    temp = random.sample(a,len(a))
    print('temp',temp)
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
