H, W = map(int,input().split())
X = [[0 for _ in range(W+1)] for _ in range(H+1)]

for i in range(1,H+1):
    row = list(map(int,input().split()))
    for j in range(1,W+1):
        X[i][j] = row[j-1]

for i in range(1,H+1):
    for j in range(1,W+1):
        X[i][j] += X[i][j-1]

for i in range(1,W+1):
    for j in range(1,H+1):
        X[j][i] += X[j-1][i]

Q = int(input())
for i in range(Q):
    A, B, C, D = map(int,input().split())
    print(X[C][D] + X[A-1][B-1] - X[A-1][D] - X[C][B-1])
    

# 和を求めたい領域周辺の特定の4点の値を使用することでなぜ和が求まるのか
# 4点の値を使って計算しているのは言い換えると長方形の引き算をしていると言える

# 求めたい領域の和 = 右上（全体）- 右上（上側）- 左下（左側）+ 左上（引きすぎた分）

# 右下 = 全体を含む一番大きな長方形
# 右上 = 全体のうち不要な領域となっている上側の長方形
# 左下 = 全体のうち不要な領域となっている左側の長方形
# 左上 = 上側の長方形と下側の長方形を全体から引くときに被る領域があるのでそれを足す