def max_val(lst):
    lst.sort()
    max_value = 0
    for i in range(len(lst)):
        mid = lst[i]
        left_index = i - 1
        right_index = len(lst) - 1
        times = 0
        mean = mid
        while left_index >= 0 and right_index > i:
            sum = mean * (2 * times + 1) + lst[left_index] + lst[right_index]
            new_mean = sum / (2 * times + 3)
            if new_mean > mean:
                max_value = max(max_value, new_mean - mid)
                left_index -= 1
                right_index -= 1
            else:
                break
    return max_value


print(max_val([1, 3, 5, 9]))
