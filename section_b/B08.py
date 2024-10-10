import numpy as np
N = int(input())

mat = np.zeros((1501,1501),dtype=int)
for _ in range(N):
    X, Y = map(int,input().split())
    mat[Y][X] += 1

for i in range(1,1501):
    for j in range(1, 1501):
        mat[i][j] += mat[i][j-1]

for j in range(1,1501):
    for i in range(1, 1501):
        mat[i][j] += mat[i-1][j]

Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int,input().split())
    print(mat[d][c]+mat[b-1][a-1]-mat[b-1][c]-mat[d][a-1])


# XY座標を扱う際の問題点
# pythonのリスト: matrix[行][列]
# XY座標: (x,y)
# (x,y)の順番のままリストに格納してしまうと行成分(縦)と列成分(横)が逆になってしまう
# そのためリストには、matrix[y][x]のように逆に格納する必要がある


# 要素にアクセスするとき
# (3,2)にアクセスしたいときはmatrix[2][3]のように逆にアクセスする


# 累積和のfor文
# ルール
# ・外側のループは1行または1列を指定するためのループ
# ・内側のループは指定された1行または1列の中での累積和を求めるループ
#
# ・A[i][j] += A[i][j-1]のような式の左右でindexが変わっていない方が必ず外側になる
# ・上の例の場合、左右で[i]のindexが変わっていないため[i]が必ず外側のループとなる
# ・[j],[j-1]のように左右でindexが変わっている場合[j]が必ず内側のループとなる
# 


# 列方向の累積和に関してはiとjを逆するパターンとしないパターンで以下のような2通りある

# for i in range(1,1501):
#     for j in range(1, 1501):
#         mat[j][i] += mat[j-1][i]

# for j in range(1,1501):
#     for i in range(1, 1501):
#         mat[i][j] += mat[i-1][j]

# この2パターン両方に共通する考えがある
# それは、外側のループで列を回して、内側のループで行をズラすということである
# つまり i,j の順番が逆になっていても、外側は列という事は変わらない
# 上のコード例ではどちらも mat[A-1][B] のように1つ目のindexが-1されている
# i,j を逆転させることでmat[i][j] += mat[i-1][j]のようになり
# mat[j][i] += mat[j-1][i]のように逆転させる必要がなくなる


