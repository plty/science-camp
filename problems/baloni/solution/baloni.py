def main():
    n = int(input())
    h = map(int, input().split())

    d = {}
    ans = 0
    for x in h: 
        if d.get(x, 0) == 0:
            ans += 1
            d[x - 1] = d.get(x - 1, 0) + 1
        else:
            d[x] -= 1
            d[x - 1] = d.get(x - 1, 0) + 1
    print(ans) 

if __name__ == "__main__":
    main()

