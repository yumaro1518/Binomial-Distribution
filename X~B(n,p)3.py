import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# パラメータの設定
n = 100  # 試行回数
p_values = [0.2, 0.5, 0.9]  # 成功確率のリスト

# グラフの設定
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# 各成功確率についてグラフを描画
for i, p in enumerate(p_values):
    x = np.arange(0, n + 1)
    pmf = binom.pmf(x, n, p)

    axes[i].bar(x, pmf, color='skyblue', alpha=0.7)
    axes[i].set_title(f'Binomial Distribution (n={n}, p={p})')
    axes[i].set_xlabel('Number of Successes')
    axes[i].set_ylabel('Probability')
    axes[i].set_xticks(np.arange(0, n + 1, 10))  # x軸の目盛りを10刻みに
    axes[i].grid(axis='y', linestyle='--', alpha=0.7)

# グラフの表示
plt.tight_layout()
plt.show()
