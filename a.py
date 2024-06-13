# import pandas as pd
# import os

# # 获取当前文件夹路径
# folder_path = os.getcwd()

# # 文件名为a.xlsx
# file = 'a.xlsx'

# # 读取xlsx文件
# df = pd.read_excel(os.path.join(folder_path, file))

# # 输出A列的数据和序号
# for index, data in enumerate(df['A'], start=1):
#     print(f"序号: {index}, 数据: {data}")


import pandas as pd

# 读取a.xlsx文件，默认页签
df = pd.read_excel("a.xlsx")
names0 = df.iloc[:, 0].tolist()
name1 = df.iloc[:, 1].tolist()
names = df.iloc[:, 3].tolist()
a = []
b=[]
for r,i in enumerate(names):
    if i not in names0:
        a.append([r+2,i])
    else:
        b.append(i)
print(a,len(a),'mei')
print(b,len(b))

# for i in df:
#     print(i)

# 输出A列数据
# print(df['A'])