# ord('A') == 65
# pypy3: 104ms
# python3: 72ms

N = int(input())
tree_left = [0] * (N+1)
tree_right = [0] * (N+1)
for _ in range(N):
    par, l, r = input().split()
    if l != '.':
        tree_left[ord(par)-64] = ord(l) - 64
    if r != '.':
        tree_right[ord(par)-64] = ord(r) - 64

pre_or = []
in_or = []
po_or = []


def preorder(V):
    if V:
        pre_or.append(chr(V+64))
        preorder(tree_left[V])
        preorder(tree_right[V])


def inorder(V):
    if V:
        inorder(tree_left[V])
        in_or.append(chr(V+64))
        inorder(tree_right[V])


def postorder(V):
    if V:
        postorder(tree_left[V])
        postorder(tree_right[V])
        po_or.append(chr(V+64))


preorder(1)
inorder(1)
postorder(1)

print(''.join(pre_or))
print(''.join(in_or))
print(''.join(po_or))
