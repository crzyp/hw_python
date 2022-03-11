def sort_list(a):
    n = len(a)
    for i in range(n):
        for x in range (n-i-1):
            if a[x] > a[x+1]:
                a[x], a[x+1] = a[x+1], a[x]
    return a
