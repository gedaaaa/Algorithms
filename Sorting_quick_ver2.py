import random


def partition(a, lo, hi):
    i, j, index = lo, hi, lo
    # 用index记录哨兵目前的位置，每次都交换哨兵和异常值
    print('子数组为', a[lo:hi + 1])
    while j > i:
        while j > i:
            if a[j] > a[i]:
                j -= 1
                print('j-1', i, j)
            else:
                a[j], a[index] = a[index], a[j]
                index = j
                i += 1
                print('右侧发现小数 i+1', a, i, j)
                break
        while j > i:
            if a[i] < a[j]:
                i += 1
                print('i+1', i, j)
            else:
                a[j], a[i] = a[i], a[j]
                index = i
                j -= 1
                print('左侧发现大数 j-1', a, i, j)
                break
    return index


def quicksort(a, lo, hi):
    if hi <= lo:
        print('好短')
        return
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
