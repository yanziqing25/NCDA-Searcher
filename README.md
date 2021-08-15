# NCDA-Searcher
## 第九届全国高校数字艺术设计大赛入围作品查询爬虫脚本
本项目由Python3.8.1构建，仅用于查询第九届全国高校数字艺术设计大赛入围作品。

# Dependence
* Beautiful Soup 4
* Requests

# Usage
1. 输入类别代号（大类，如A, B, C, T2等，无需输入后面的数字。具体支持列表见官网公示名单）
2. 直接输入作品名进行模糊查询

# Build
1. `cd NCDA-Searcher`
2. `pip install beautifulsoup4 requests`
3. `python main.py`