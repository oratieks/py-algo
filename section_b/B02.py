a, b = map(int,input().split())

ans = "No"
for num in range(a,b+1):
    if 100 % num == 0:
        ans = "Yes"
        
print(ans)