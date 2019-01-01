def main():
    count = {}

    n = int(input())
    for _ in range(n):
        s = input()
        print(count.get(s, 0))
        for i in range(len(s)):
            prefix = s[:i + 1]
            count[prefix] = count.get(prefix, 0) + 1

if __name__ == "__main__":
    main()
