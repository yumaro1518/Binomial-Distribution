import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# パラメータの設定
n = 30  # 試行回数
p = 0.5  # 成功確率

# xの範囲（成功の数）
x = np.arange(0, n + 1)

# 二項分布の確率質量関数 (PMF)
pmf = binom.pmf(x, n, p)

# グラフの描画
plt.figure(figsize=(8, 5))
plt.bar(x, pmf, color='skyblue', alpha=0.7)
plt.title(f'Binomial Distribution (n={n}, p={p})')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.xticks(x)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# グラフの表示
plt.show()
