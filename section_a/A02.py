n,x = map(int,input().split())
a = list(map(int,input().split()))

ans = "No"

for num in a:
    if num == x:
        ans = "Yes"
        
print(ans)
