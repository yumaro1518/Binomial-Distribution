import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib 
from scipy.stats import binom
from scipy.stats import norm

# 日本語フォントの設定
plt.rcParams['font.family'] = 'IPAexGothic'  # 使用する日本語フォントを指定
plt.rcParams['axes.unicode_minus'] = False   # マイナス記号を正しく表示

# -------
#ある工場では製品の不良率が 5% です。製品を 20 個ランダムに選んだときに、以下の確率を求めてください。
#不良品が 2 個以下である確率
#不良品が 1 個以上 3 個以下である確率
#不良品が 4 個以上である確率

# 二項分布のパラメータ
n = 20      # 試行回数
p = 0.05    # 成功確率

# 1. 不良品が2個以下である確率
prob_2_or_less = binom.cdf(2, n, p)

# 2. 不良品が1個以上3個以下である確率
prob_1_to_3 = binom.cdf(3, n, p) - binom.cdf(0, n, p)

# 3. 不良品が4個以上である確率
prob_4_or_more = 1 - binom.cdf(3, n, p)

# 結果の表示
print("1. 不良品が2個以下である確率 =", prob_2_or_less)
print("2. 不良品が1個以上3個以下である確率 =", prob_1_to_3)
print("3. 不良品が4個以上である確率 =", prob_4_or_more)
# -------
# 二項分布のパラメータ
n = 20      # 試行回数
p = 0.05    # 成功確率

# x軸の値（0から20まで）
x = np.arange(0, 10)

# 各xにおける確率質量関数 (PMF)
pmf_values = binom.pmf(x, n, p)

# プロット
plt.figure(figsize=(12, 6))
plt.bar(x, pmf_values, color='gray', alpha=0.5,width = 0.2, label='確率分布')

# 1. 不良品が2個以下である確率の部分を色付け
plt.bar(x[x <= 2], pmf_values[x <= 2], color='lightblue', width = 0.2 ,label='不良品が2個以下の確率')

# 2. 不良品が1個以上3個以下である確率の部分を色付け
plt.bar(x[(x >= 1) & (x <= 3)], pmf_values[(x >= 1) & (x <= 3)], color='lightgreen',width = 0.2 ,label='不良品が1個以上3個以下の確率')

# 3. 不良品が4個以上である確率の部分を色付け
plt.bar(x[x >= 4], pmf_values[x >= 4], color='grey',width = 0.2 , label='不良品が4個以上の確率')

# グラフのタイトルと軸ラベル
plt.title("不良品の個数ごとの確率分布 (二項分布 B(20, 0.05))")
plt.xlabel("不良品の個数")
plt.ylabel("確率")
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# グラフの表示
plt.show()
