'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

# 전위순회
def preorder1(n):
    if n:
        print(n, end=' ')
        preorder1(left[n])
        preorder1(right[n])

def preorder2(n):
    if n == 0:
        return
    print(n, end=' ')
    preorder2(tree[n][0])
    preorder2(tree[n][1])

# 중위순회
def inorder1(n):
    if n:
        inorder1(left[n])
        print(n, end=' ')
        inorder1(right[n])

def inorder2(n):
    if n == 0:
        return
    inorder2(tree[n][0])
    print(n, end=' ')
    inorder2(tree[n][1])

# 후위순회
def postorder1(n):
    if n:
        postorder1(left[n])
        postorder1(right[n])
        print(n, end=' ')

def postorder2(n):
    if n == 0:
        return
    postorder2(tree[n][0])
    postorder2(tree[n][1])
    print(n, end=' ')

V = 15
E = V - 1
edge = list(map(int, input().split()))

parent = [0] * (V+1)
left = [0] * (V+1)
right = [0] * (V+1)

tree = [[0]*3 for _ in range(V+1)]

for i in range(E):  # 리스트 활용
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

# print(parent)
# print(left)
# print(right)

for i in range(E):  # 이차원 배열 활용?
    p, c = edge[i*2], edge[i*2+1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p

for row in tree:
    print(row)

root1 = 0
for i in range(1, V+1):
    if parent[i] == 0:
        root1 = i
        break

root2 = 0
for i in range(1, V+1):
    if tree[i][2] == 0:
        root2 = i
        break

print('---전위 순회---')
preorder1(root1)
print()
preorder2(root2)
print()
print('---중위 순회---')
inorder1(root1)
print()
inorder2(root2)
print()
print('---후위 순회---')
postorder1(root1)
print()
postorder2(root2)