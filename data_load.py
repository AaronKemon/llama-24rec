import csv

# 打开CSV文件
with open('dataset/movies.csv', newline='') as csvfile:  # 替换 'your_csv_file.csv' 为你的CSV文件路径
    csv_reader = csv.reader(csvfile)
    
    data_list = []  # 用于存储转换后的数据
    row_count = 0 

    for row in csv_reader:
        # 读取前三列数据
        first_column = row[0]
        second_column = row[1]
        third_column = row[2]
        
        # 转换为字典格式并添加到列表
        data_dict = {
            '第一列数据': first_column,
            '第二列数据': second_column,
            '第三列数据': third_column
        }
        data_list.append(data_dict)
        row_count+=1

# 打印结果
        if row_count<=5:
            print(data_dict)
    
