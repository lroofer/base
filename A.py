def f(left, used):
    if left == 0:
        print(*cur)
        return
    for i in range(len(used)):
        if not used[i]:
            cur.append(i+1)
            used[i] = True
            f(left - 1, used)
            cur.pop()
            used[i] = False
n = int(input())
cur = []
used = [False for i in range(n)]
f(n, used)
