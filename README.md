# 企业数据可视化应用

这是一个基于Streamlit框架的企业数据可视化应用，用于展示合并后的企业信息、股票代码、年份和行业数据。

## 功能特点

- 📊 **数据概览**：显示总记录数、企业数量和年份范围
- 🔍 **数据筛选**：支持按年份和行业进行多条件筛选
- 📋 **数据表格**：展示详细的企业数据，包括企业名称、股票代码、年份、行业代码和行业名称
- 📈 **数据可视化**：使用柱状图展示行业分布，折线图展示年份分布
- 💾 **数据导出**：支持将筛选后的数据导出为CSV格式

## 项目结构

```
企业数据可视化应用/
├── merge_excel.py          # 数据分析脚本（可选）
├── merge_tables.py         # 表合并脚本（可选）
├── streamlit_app.py        # Streamlit应用主程序
├── requirements.txt        # 项目依赖
├── README.md               # 项目说明文档
├── .gitignore              # Git忽略文件
└── 合并后的企业数据.xlsx     # 合并后的企业数据（可选）
```

## 安装步骤

1. 克隆仓库：
   ```bash
   git clone <仓库地址>
   cd <仓库名称>
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. 确保您的目录中包含`合并后的企业数据.xlsx`文件
2. 运行Streamlit应用：
   ```bash
   streamlit run streamlit_app.py
   ```
3. 在浏览器中访问应用（默认地址：http://localhost:8502）

## 部署到云端

如果您希望将应用部署到云端，让所有人都可以访问，可以考虑以下平台：

- **Streamlit Cloud**：官方提供的免费部署平台
- **Heroku**：支持Python应用的PAAS平台
- **AWS EC2**：可自行配置的云服务器

### Streamlit Cloud部署步骤

1. 在GitHub上创建仓库并推送代码
2. 访问[Streamlit Cloud](https://streamlit.io/cloud)
3. 点击"New app"按钮
4. 选择您的GitHub仓库、分支和主文件（streamlit_app.py）
5. 点击"Deploy"按钮完成部署

## 数据说明

本应用使用的是合并后的企业数据，包含以下字段：
- 企业名称：上市公司的全称
- 股票代码：上市公司的股票代码
- 年份：数据统计的年份
- 行业代码：上市公司所属行业的代码
- 行业名称：上市公司所属行业的名称

## 注意事项

- 如果您没有`合并后的企业数据.xlsx`文件，可以使用`merge_tables.py`脚本生成
- 运行`merge_tables.py`脚本需要原始数据文件：
  - 历年数字化转型指数汇总.xlsx
  - 最终数据dta格式-上市公司年度行业代码至2021.xlsx

## 许可证

本项目采用MIT许可证。
