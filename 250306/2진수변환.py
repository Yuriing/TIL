lst = list(map(int, input().strip()))
N = len(lst)

# 내장함수 int() 사용
i = 0
while i+7 < N:
    print(int(''.join(map(str, lst[i:i+7])), 2), end=' ')
    i += 7

# 내장함수 미사용
j = 0
while j+7 < N:
    bin_num = ''.join(map(str, lst[j:j+7]))
    dec_num = 0
    for i in range(7):
        dec_num += (int(bin_num[i]) * (2**(6-i)))
    print(dec_num, end=' ')
    j += 7
