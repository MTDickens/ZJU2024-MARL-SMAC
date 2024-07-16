import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

_lambda = 0.4

# 从文件中读取数据
with open(f'results/sacred/{_lambda}_2050000/info.json', 'r') as file:
    data = json.load(file)

# 计算移动平均
def moving_average(data, window_size=5):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# 函数定义：根据名称绘图并保存图片
def plot_and_save(name, _lambda=None, file_name='output.png'):
    # 获取数据
    y_values = data[name]
    x_values = data[f"{name}_T"]
    
    # 创建图形
    plt.figure(figsize=(10, 6), dpi=300)  # 高清图片设置：dpi=300
    
    # 绘制原始数据点（蓝色点）
    plt.scatter(x_values, y_values, color='azure', label='Original Data')
    
    # 绘制拟合线（橙色实线）
    plt.plot(x_values, y_values, color='yellow', label='Fit Line')
    
    # 计算移动平均（五次平均）
    y_ma = moving_average(y_values, window_size=5)
    
    # 移动平均后的 x 值
    x_ma = x_values[:len(y_ma)]
    
    # 绘制平滑的移动平均线（浅灰色虚线）
    plt.plot(x_ma, y_ma, linestyle='--', color='red', label='5-Point Moving Average')
    
    # 添加标题和标签
    plt.title(f'{name}' + (f' (lambda: {_lambda})' if _lambda is not None else ''))
    plt.xlabel(f'{name}_T')
    plt.ylabel(name)
    plt.legend()
    
    # 保存图片
    plt.savefig(file_name, bbox_inches='tight')
    plt.close()

# 使用函数绘制并保存图片
plot_and_save('test_battle_won_mean', _lambda, f'test_battle_won_mean_plot_lambda_{_lambda}.png')