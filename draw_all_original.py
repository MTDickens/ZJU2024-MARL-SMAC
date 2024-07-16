import json
import numpy as np
import matplotlib.pyplot as plt

lambdas = [0.4, 0.5, 0.6]  # 这里是你的三个 lambda 值

name = 'td_error_abs'

# 从文件中读取数据
data = {}
for _lambda in lambdas:
    with open(f'results/sacred/{_lambda}_2050000/info.json', 'r') as file:
        data[f'{_lambda}'] = json.load(file)

# 计算移动平均
def moving_average(data, window_size=5):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

# 函数定义：根据名称绘图并保存图片
def plot_and_save(name, lambdas, file_name='output.png'):
    colors = ['peachpuff', 'lightcoral', 'lightblue']  # 定义颜色列表
    labels = [f'$\\lambda$ = {l} (moving average of 5)' for l in lambdas]
    
    # 创建图形
    plt.figure(figsize=(10, 6), dpi=300)  # 高清图片设置：dpi=300
    
    for i, _lambda in enumerate(lambdas):
        # 获取数据
        y_values = data[f'{_lambda}'][name]
        x_values = data[f'{_lambda}'][f"{name}_T"]
        
        # # 绘制原始数据点（蓝色点）
        # plt.scatter(x_values, y_values, color='blue', label='Original Data' if i == 0 else "")
        
        # 绘制拟合线（橙色实线）
        plt.plot(x_values, y_values, color=colors[i], label=f'$\\lambda$ = {_lambda}')

        # 绘制后一半数据的平均值
        half_index = len(y_values) // 2
        plt.axhline(y=np.average(y_values[half_index:]), color=colors[i], linestyle='--')
        
        # # 计算移动平均（五次平均）
        # y_ma = moving_average(y_values, window_size=5)
        
        # # 移动平均后的 x 值
        # x_ma = x_values[:len(y_ma)]
        
        # # 绘制平滑的移动平均线
        # plt.plot(x_ma, y_ma, linestyle='--', color=colors[i], label=labels[i])

    # # 绘制红色虚线， y = 0.3
    # plt.axhline(y=0.3, color='red', linestyle='--')

    # plt.axvline(x=5e5, color='red', linestyle='--')
    
    # 添加标题和标签
    plt.title(f'{name}')
    plt.xlabel(f'{name}_T')
    plt.ylabel(name)
    plt.legend()
    
    # 保存图片
    plt.savefig(file_name, bbox_inches='tight')
    plt.close()

# 使用函数绘制并保存图片
plot_and_save(name, lambdas, f'{name}_plot.png')
