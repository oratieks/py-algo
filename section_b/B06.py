n = int(input())
a = [0] + list(map(int,input().split()))
for i in range(1,n+1):
    if a[i] == 0:
        a[i] = -1
    a[i] += a[i-1]

q = int(input())

for i in range(q):
    l, r = map(int,input().split())
    r = a[r]-a[l-1]
    if r == 0:
        print("draw")
    elif r > 0:
        print("win")
    elif r < 0:
        print("lose")