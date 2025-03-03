import sys
sys.stdin = open('input1225.txt')

for _ in range(1, 11):
    T = int(input())
    lst = list(map(int, input().split()))

    now = True
    while now == True:
        for i in range(1, 6):
            num = lst.pop(0)
            if num-i <= 0:
                lst.append(0)
                now = False
                break
            lst.append(num-i)

    
    print(f'#{T} {" ".join(map(str, lst))}')