from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
nodeInfos = [input().split() for _ in range(N)]
dic = defaultdict(list)
root = 'A'

for nodeInfo in nodeInfos:
    a, b, c = nodeInfo
    dic[a].append(b)
    dic[a].append(c)

def preOrder(node):
    if node != '.':
        print(node, end='')
        preOrder(dic[node][0])
        preOrder(dic[node][1])

def inOrder(node):
    if node != '.':
        inOrder(dic[node][0])
        print(node, end='')
        inOrder(dic[node][1])

def postOrder(node):
    if node != '.':
        postOrder(dic[node][0])
        postOrder(dic[node][1])
        print(node, end='')

preOrder(root)
print()
inOrder(root)
print()
postOrder(root)