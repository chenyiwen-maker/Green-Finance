import pandas as pd
import numpy as np

# 读取数据，假设数据保存在 'data.csv'，并以制表符分隔
df = pd.read_excel('data/dataSALL.xlsx')

# 定义衰减函数
def f(delta_t):
    if 3 - delta_t > 0:
        return np.log(3 - delta_t) / np.log(3)
    else:
        return 0

# 计算权重
w0 = f(0)  # 1
w1 = f(1)  # ln(2)/ln(3)
print("###################")
print(f(1))
print("###################")
W = w0 + w1

# 按地点和时间排序
df = df.sort_values(['Location', 'Time'])

# 初始化 Y 列
df['Y'] = np.nan

# 计算 Y
locations = df['Location'].unique()
for loc in locations:
    df_loc = df[df['Location'] == loc].sort_values('Time').reset_index()
    for i in df_loc.index:
        if df_loc.at[i, 'Time'] == 1990:
            df.at[df_loc.at[i, 'index'], 'Y'] = df_loc.at[i, 's']
        else:
            current_s = df_loc.at[i, 's']
            prev_s = df_loc.at[i-1, 's'] if i-1 >=0 else 0
            Y = (current_s * w0 + prev_s * w1) / W
            df.at[df_loc.at[i, 'index'], 'Y'] = Y

# 保存结果
# df.to_csv('data_with_Y.csv', index=False)
df.to_excel('data/data_with_Y.xlsx', index=False)
print("success")