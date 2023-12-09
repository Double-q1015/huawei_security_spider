from bs4 import BeautifulSoup
import pandas as pd
import os


def parse_html_table(html_content, tbody_id='dataTableBody', tr_class='trContent'):
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 选择tbody元素，id为dataTableBody
    tbody_element = soup.find('tbody', id=tbody_id)

    # 在tbody元素中选择所有class为trContent的tr元素
    tr_elements = tbody_element.find_all('tr', class_=tr_class)

    # 初始化一个字典，用于存储每一列的值
    data_dict = {f'Column{str(i)}': [] for i in range(1, len(tr_elements[0].find_all('td')) + 1)}

    # 遍历所有选中的tr元素
    for tr_element in tr_elements:
        # 获取当前tr元素下的所有td元素
        td_elements = tr_element.find_all('td')

        # 遍历所有选中的td元素，将值添加到对应列
        for i, td_element in enumerate(td_elements):
            data_dict[f'Column{str(i + 1)}'].append(td_element.text.strip())

    # 使用字典创建数据框
    df = pd.DataFrame(data_dict)

    return df


# 文件夹路径，包含所有HTML文件
html_folder_path = 'data/page'

# 存储所有数据框的列表
dfs_list = []

# 遍历文件夹中的HTML文件
for filename in os.listdir(html_folder_path):
    if filename.endswith(".html"):
        file_path = os.path.join(html_folder_path, filename)

        # 读取HTML文件
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # 使用封装的函数
        result_df = parse_html_table(html_content)

        # 将数据框添加到列表
        dfs_list.append(result_df)

# 合并所有数据框
final_df = pd.concat(dfs_list, ignore_index=True)

# 保存为CSV文件
final_df.to_csv(r'data/output.csv', index=False)
