###総当たり法###
items = [
    (4, 6), (8, 12), (3, 4), (5, 3), (9, 7), (2, 1), 
    (3, 3), (1, 2), (5, 7), (2, 3), (4, 4), (2, 2), 
    (7, 10), (10, 13), (3, 5), (13, 16), (11, 14), (8, 9)
]

capacity = 45
n = len(items)

best_value = 0
best_combination = []
best_weight = 0

for i in range(1 << n):
    current_weight = 0
    current_value = 0
    current_combination = []
    
    for j in range(n):
        # i の j ビット目が1ならば、品物 j を選ぶ
        if (i >> j) & 1:
            current_weight += items[j][0]
            current_value += items[j][1]
            current_combination.append(j + 1) # 品物番号は1始まりにする
            
    # 容量の範囲内で、これまでの最大値段を更新した場合
    if current_weight <= capacity:
        if current_value > best_value:
            best_value = current_value
            best_combination = current_combination
            best_weight = current_weight

# 結果の出力
print(f"最大値段: {best_value}")
print(f"品物の組み合わせ (品物番号): {best_combination}")
print(f"合計容量: {best_weight}")