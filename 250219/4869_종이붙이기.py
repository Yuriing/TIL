import sys
sys.stdin = open('input4869.txt')
'''
너비 10을 만드는 경우의 수는 10*20 하나
너비 20을 만드는 경우의 수는 10*20*2, 20*10*2, 20*20 셋
너비 30을 만드는 경우의수부터는
    너비 10을 만드는 경우 오른쪽에 20*10*2, 20*20을 붙이거나
    너비 20을 만드는 경우 오른쪽에 10*20을 붙이면 된다
너비 10을 만드는 경우 오른쪽에 10*20을 붙이는 경우는 너비 20을 만드는 경우 오른쪽에 10*20을 붙이는 경우에서 count된다
따라서 30 이후부터는 f(n-1)+f(n-2)*2 로 작동한다
'''
def paperstick(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    
    return paperstick(n-1) + paperstick(n-2)*2

T = int(input())
for tc in range(1, T+1):

    N = int(input()) // 10
    result = paperstick(N)
    print(f'#{tc} {result}')