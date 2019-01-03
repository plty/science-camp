def main():
    n = int(input())
    baloons = map(int, input().split())

    arrow = {}
    arrow_used = 0
    for height in baloons: 
        if arrow.get(height, 0) == 0:
            arrow_used += 1
        else:
            arrow[height] -= 1

        arrow[height - 1] = arrow.get(height - 1, 0) + 1
    print(arrow_used) 

if __name__ == "__main__":
    main()

