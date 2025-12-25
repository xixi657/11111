import streamlit as st
import pandas as pd
import os

# 设置页面标题和布局
st.set_page_config(
    page_title="企业数据可视化",
    page_icon="📊",
    layout="wide"
)

# 添加标题和说明
st.title("📊 合并后的企业数据展示")
st.markdown("这是一个基于Streamlit的企业数据可视化应用，展示合并后的企业信息、股票代码、年份和行业数据。")

# 获取当前工作目录
current_dir = os.getcwd()

# 读取合并后的Excel文件
file_path = os.path.join(current_dir, '合并后的企业数据.xlsx')

# 检查文件是否存在
if os.path.exists(file_path):
    df = pd.read_excel(file_path)
    
    # 数据概览
    st.header("数据概览")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("总记录数", len(df))
    with col2:
        st.metric("企业数量", df['企业名称'].nunique())
    with col3:
        st.metric("年份范围", f"{df['年份'].min()}-{df['年份'].max()}")
    
    # 数据筛选
    st.header("数据筛选")
    col4, col5 = st.columns(2)
    
    with col4:
        # 年份选择器
        selected_year = st.multiselect(
            "选择年份",
            options=df['年份'].unique().tolist(),
            default=df['年份'].unique().tolist()
        )
    
    with col5:
        # 行业选择器
        selected_industry = st.multiselect(
            "选择行业",
            options=df['行业名称'].dropna().unique().tolist(),
            default=df['行业名称'].dropna().unique().tolist()
        )
    
    # 应用筛选
    filtered_df = df[df['年份'].isin(selected_year) & df['行业名称'].isin(selected_industry)]
    
    # 数据表格展示
    st.header("企业数据详情")
    st.dataframe(filtered_df, use_container_width=True)
    
    # 行业分布统计
    st.header("行业分布统计")
    industry_counts = filtered_df['行业名称'].value_counts()
    
    # 使用柱状图展示行业分布
    st.bar_chart(industry_counts, use_container_width=True)
    
    # 年份分布统计
    st.header("年份分布统计")
    year_counts = filtered_df['年份'].value_counts().sort_index()
    
    # 使用折线图展示年份分布
    st.line_chart(year_counts, use_container_width=True)
    
    # 数据导出功能
    st.header("数据导出")
    csv = filtered_df.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📥 下载筛选后的数据（CSV格式）",
        data=csv,
        file_name="筛选后的企业数据.csv",
        mime="text/csv"
    )
    
else:
    st.error(f"找不到合并后的数据文件：{file_path}")
    st.info("请确保已成功合并两个Excel文件并生成了'合并后的企业数据.xlsx'文件。")
