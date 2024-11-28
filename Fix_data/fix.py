import pandas as pd

# Đọc dữ liệu từ các file CSV của năm 2020 và 2021
df1 = pd.read_csv(r'C:\Users\Admin\Desktop\BTL_TDA\Data\diem_thi_2020.csv')
df2 = pd.read_csv(r'C:\Users\Admin\Desktop\BTL_TDA\Data\diem_thi_2021.csv')

# Thay thế 'Thanh Hóa' thành 'Thanh Hoá' trong cột 'province'
df1['province'] = df1['province'].replace('Thanh Hóa', 'Thanh Hoá')
df2['province'] = df2['province'].replace('Thanh Hóa', 'Thanh Hoá')

# Lưu lại dữ liệu vào file CSV sau khi sửa
df1.to_csv(r'C:\Users\Admin\Desktop\BTL_TDA\Data\diem_thi_2020.csv', index=False)
df2.to_csv(r'C:\Users\Admin\Desktop\BTL_TDA\Data\diem_thi_2021.csv', index=False)

print("Đã thay thế 'Thanh Hóa' thành 'Thanh Hoá' và lưu lại ")
