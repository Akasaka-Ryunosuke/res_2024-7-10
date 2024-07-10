def min_sub_times(source, target):
    if len(source) == 0 or len(target) == 0:
        return -1
    times = 0
    flag = True
    j = 0
    while flag and j < len(target):
        flag = False
        for i in range(len(source)):
            if j < len(target) and source[i] == target[j]:
                j += 1
                flag = True
        times += 1
    if flag:
        return times
    else:
        return -1


if __name__ == '__main__':
    print(min_sub_times("abc", "abcbc"))
    print(min_sub_times("abc", "acdbc"))
    print(min_sub_times("xyz", "xzyxz"))
    print(min_sub_times("xyz", ""))
    print(min_sub_times("xyzyz", "yxzy"))
