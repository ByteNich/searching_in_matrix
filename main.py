import time
def binary_search(table, target, n, m):
    for j in range(m):
        left, right, i = 0, n - 1, 0
        while left <= right:
            i = left + (right - left) // 2
            if table[i][j] == target:
                return [i, j]
            elif table[i][j] < target:
                left = i + 1
            else:
                right = i - 1
    return [-1, -1]

def is_within_bounds(i, j, n, m):
    return i >= 0 and i < n and j >= 0 and j < m

def diagonal_search(table, target, n, m):
    i, j = 0, m - 1
    while is_within_bounds(i, j, n, m):
        if table[i][j] == target:
            return True
        elif table[i][j] < target:
            i += 1
        else:
            j -= 1
    return False

def exp_search(table, i, j, n, target):
    st = 1
    while i + st < n and table[i + st][j] < target:
        st *= 2
    left = i + st // 2 + 1
    right = min(n - 1, i + st)
    while left <= right:
        mid = left + (right - left) // 2
        if table[mid][j] == target:
            return mid
        elif table[mid][j] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def diagonal_search_exp_acc(table, target, n, m):
    i, j = 0, m - 1
    while is_within_bounds(i, j, n, m):
        if table[i][j] == target:
            return True
        elif table[i][j] < target:
            if i < n - 2:
                i = exp_search(table, i, j, n, target)
            else:
                i += 1
        else:
            j -= 1
    return False
  # DIAGONAL SEARCH WITH EXPONONCIAL ACCELERATION
n = 8192
target = 16 * n + 1
for k in range(1, 14):
    m = pow(2, k)
    table = [[int((n / m) * i * j) * 2 for j in range(m)] for i in range(n)]

    t0 = time.perf_counter()
    print(diagonal_search_exp_acc(table, target, n, m))
    t1 = time.perf_counter()
    print((t1 - t0) * 1000)

  # BINARY SEARCH
'''t0 = time.perf_counter()
print(binary_search(table, target, n, m))
t1 = time.perf_counter()
print((t1 - t0)*1000)'''
# DIAGONAL SEARCH
'''t0 = time.perf_counter()
print(diagonal_search(table, target, n, m))
t1 = time.perf_counter()
print((t1 - t0)*1000)'''
