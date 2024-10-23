import pandas as pd

# Step 1: Load the data from Excel
file_path = 'data/dataL.xlsx'  # Replace with the actual file path
data = pd.read_excel(file_path)

# # Step 2: Rename the columns to X1 to X20
# column_mapping = {
#     '人均粮食产量': 'X1',
#     '农业总产值指数(按可比价格计算)': 'X2',
#     '农业机械总动力': 'X3',
#     '粮食单位面积产量': 'X4',
#     '农村节水灌溉面积': 'X5',
#     '农药使用量': 'X6',
#     '森林抚育面积': 'X7',
#     '水土流失治理面积': 'X8',
#     '乡镇卫生院卫生人员数': 'X9',
#     '老年人口抚养比': 'X10',
#     '少年儿童抚养比': 'X11',
#     '农村居民教育文化娱乐消费支出': 'X12',
#     '堤防保护耕地面面积': 'X13',
#     '农村户用沼气池数量': 'X14',
#     '农村太阳灶': 'X15',
#     '农村住户住宅固定资产投资额': 'X16',
#     '农村居民人均可支配收入': 'X17',
#     '城乡居民收入水平对比': 'X18',
#     '农村居民平均每百户年末移动电话拥有量': 'X19',
#     '农村居民人均消费支出': 'X20'
# }
# data_renamed = data.rename(columns=column_mapping)

# Step 3: Define the positive and negative columns
# positive_columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X19', 'X20']
# negative_columns = ['X6', 'X18']
positive_columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X7']
# negative_columns = ['X6', 'X18']
# Step 4: Apply Min-Max normalization
for col in positive_columns:
    data[col] = (data[col] - data[col].min()) / (data[col].max() - data[col].min())

# for col in negative_columns:
#     data_renamed[col] = 1 - ((data_renamed[col] - data_renamed[col].min()) / (data_renamed[col].max() - data_renamed[col].min()))

# Step 5: Save the normalized data to a new Excel file
output_path = 'data/normalized_data.xlsx'  # Change the path if needed
data.to_excel(output_path, index=False)

print(f"Normalized data saved to {output_path}")
