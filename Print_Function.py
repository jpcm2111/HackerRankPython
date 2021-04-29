if __name__ == '__main__':
    n = int(input())
    cnt = 1
    res = []
    while cnt <= n:
        res.append(cnt)
        cnt = cnt + 1
    cnt = 0
    while cnt < n:
        print(res[cnt], end = '')
        cnt = cnt + 1