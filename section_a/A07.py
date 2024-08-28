d = int(input())
n = int(input())
a = [0] * (d+2)
for _ in range(n):
    l, r = map(int,input().split())
    a[l] += 1
    a[r+1] -= 1

for i in range(1,d+2):
    a[i] += a[i-1]

print(*a[1:-1],sep='\n')

# 注意点
# 最終日まで参加する人がいる場合リストの最終日の+1日したindexに -1 される
# つまり最終日+1日分リストを用意しなければエラーになってしまう