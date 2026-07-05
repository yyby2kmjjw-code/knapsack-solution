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

### 動的計画法###
# 1. [span_1](start_span)各品物の (容量, 値段) のリスト (品物1 〜 品物18)[span_1](end_span)
items = [
    (4, 6), (8, 12), (3, 4), (5, 3), (9, 7), (2, 1), 
    (3, 3), (1, 2), (5, 7), (2, 3), (4, 4), (2, 2), 
    (7, 10), (10, 13), (3, 5), (13, 16), (11, 14), (8, 9)
]

capacity = 45 # ナップサックの容量[span_2](end_span)
n = len(items)

# 2. DPテーブルの初期化
# dp[w] は「容量 w のときに達成できる最大の値段」を記録する
dp = [0] * (capacity + 1)

# item_history[w] は「容量 w のときに選んだ品物の番号リスト」を記録する
item_history = [[] for _ in range(capacity + 1)]

# 3. 動的計画法（DP）のループ処理
for idx, (w, v) in enumerate(items):
    item_num = idx + 1 # 品物番号は1始まり
    
    # ナップサックの最大容量から、今注目している品物の容量 w まで逆順にループ
    # （逆順にする理由は、同じ品物を何回も選んでしまう重複を防ぐため）
    for current_w in range(capacity, w - 1, -1):
        
        # 「この品物を選んだ場合の値段」が「これまでの最大値段」より高くなる場合
        if dp[current_w - w] + v > dp[current_w]:
            # 値段を更新
            dp[current_w] = dp[current_w - w] + v
            # 選んだ品物の組み合わせ（履歴）を更新
            item_history[current_w] = item_history[current_w - w] + [item_num]

# 4. 結果の抽出
best_value = dp[capacity]
best_combination = item_history[capacity]

# 選択された品物の合計容量を計算
best_weight = sum(items[num - 1][0] for num in best_combination)

# 結果の出力
print(f"最大値段: {best_value}")
print(f"品物の組み合わせ (品物番号): {best_combination}")
print(f"合計容量: {best_weight}")