import sys
sys.stdin = open('input5356.txt')

T = int(input())
for tc in range(1, T+1):

    text = [[False]*15 for _ in range(5)]
    for i in range(5):
        strs = input().strip()
        text[i][:len(strs)] = list(strs)

    r = 0
    c = 0
    aligntext = []
    for c in range(15):
        for r in range(5):
            if text[r][c] != False:
                aligntext.append(text[r][c])

    print(f'#{tc} {"".join(map(str, aligntext))}')
