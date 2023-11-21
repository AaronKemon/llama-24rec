import csv

# 打开CSV文件
with open('dataset/movies.csv', newline='') as csvfile:  # 替换 'your_csv_file.csv' 为你的CSV文件路径
    csv_reader = csv.reader(csvfile)
    
    data_dict = {}  # 用于存储转换后的数据

    for row in csv_reader:
        # 读取前三列数据
        key = row[0]
        attribute1 = row[1]
        attribute2 = row[2]
        
        # 检查字典中是否已存在该键，如果存在，将属性添加到该键对应的值中
        if key in data_dict:
            data_dict[key]['属性1'] = attribute1
            data_dict[key]['属性2'] = attribute2
        else:
            # 如果键不存在，创建一个新的字典并添加到 data_dict 中
            data_dict[key] = {
                '属性1': attribute1,
                '属性2': attribute2
            }

# 打印前5行数据用于验证
row_count = 0
for key, value in data_dict.items():
    print(f'键: {key}, 属性1: {value["属性1"]}, 属性2: {value["属性2"]}')
    row_count += 1
    if row_count >= 5:
        break
