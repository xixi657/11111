import pandas as pd
import os

# 获取当前工作目录
current_dir = os.getcwd()

# 读取两个Excel文件
df1 = pd.read_excel(os.path.join(current_dir, '历年数字化转型指数汇总.xlsx'))
df2 = pd.read_excel(os.path.join(current_dir, '最终数据dta格式-上市公司年度行业代码至2021.xlsx'))

# 查看两个表的列名
print('=== 第一个表列名 ===')
print(df1.columns.tolist())
print('\n=== 第二个表列名 ===')
print(df2.columns.tolist())

# 重命名第二个表的列名，使其与第一个表一致
print('\n=== 重命名第二个表的列名 ===')
df2_renamed = df2.rename(columns={
    '股票代码全称': '股票代码',
    '年度': '年份'
})
print(df2_renamed.columns.tolist())

# 选择需要的列
df1_selected = df1[['企业名称', '股票代码', '年份']]
df2_selected = df2_renamed[['股票代码', '年份', '行业代码', '行业名称']]

# 根据股票代码和年份进行合并
print('\n=== 开始合并表 ===')
merged_df = pd.merge(df1_selected, df2_selected, on=['股票代码', '年份'], how='inner')

# 查看合并后的表信息
print('\n=== 合并后的表信息 ===')
print(merged_df.info())
print('\n=== 合并后的表前10行 ===')
print(merged_df.head(10))

# 保存合并后的表
output_file = os.path.join(current_dir, '合并后的企业数据.xlsx')
merged_df.to_excel(output_file, index=False)
print(f'\n合并后的表已保存到: {output_file}')
print(f'合并后的表行数: {len(merged_df)}')
print(f'合并后的表列数: {len(merged_df.columns)}')
