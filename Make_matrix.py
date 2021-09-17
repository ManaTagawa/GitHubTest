import  torch
import  itertools

# '1'で作成
# >>> Make_matrix_one(3)
# tensor([[1, 0, 0],
#         [0, 1, 0],
#         [0, 0, 1],
#         [1, 1, 0],
#         [1, 0, 1],
#         [0, 1, 1],
#         [1, 1, 1]])

def Make_matrix_one(x_num): # 説明変数の数
    x_list  = list(range(0,x_num)) # [0, 1, 2, ..., x_num-1]
    houjo_num = 2**x_num -1  # べき集合の数（空集合除く）
    matrix = torch.zeros(houjo_num, x_num) # 要素が全部0のtensor
    # 行列作成
    R = 0
    for one_num in range(1,x_num+1):
        c = list(itertools.combinations(x_list, one_num)) # 組み合わせ計算
        for i in range(len(c)):
            row = i+R # 1列ずつ重み行列を作成
            for j in range(one_num):
                matrix[row][c[i][j]] = 1
        R += len(c)
    # 作成した行列を返す
    return matrix

##################################################

# '0'で作成
# >>> Make_matrix_zero(3)
# tensor([[0, 1, 1],
#         [1, 0, 1],
#         [1, 1, 0],
#         [0, 0, 1],
#         [0, 1, 0],
#         [1, 0, 0],
#         [0, 0, 0]])

def Make_matrix_zero(x_num): # 説明変数の数
    x_list  = list(range(0,x_num)) # [0, 1, 2, ..., x_num-1]
    houjo_num = 2**x_num -1  # べき集合の数（空集合除く）
    matrix = torch.ones(houjo_num, x_num) # 要素が全部0のtensor
    # 行列作成
    R = 0
    for one_num in range(1,x_num+1):
        c = list(itertools.combinations(x_list, one_num)) # 組み合わせ計算
        for i in range(len(c)):
            row = i+R # 1列ずつ重み行列を作成
            for j in range(one_num):
                matrix[row][c[i][j]] = 0
        R += len(c)
    # 作成した行列を返す
    return matrix