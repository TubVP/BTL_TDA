import pandas as pd

df = pd.read_csv('diem_thi_2020_2021.csv')

df = df.drop(columns= ['Tên', 'Ngày Sinh', 'Giới tính'])

df.to_csv('diem_thi_2020_2021_updated.csv', index= False)

print('Đã xoá thành công')
df = pd.read_csv('diem_thi_2020_2021_updated.csv')

# Tách dữ liệu cho năm 2020 và 2021
df_2020 = df[df['Year'] == 2020]
df_2021 = df[df['Year'] == 2021]

# Lưu lại hai bảng thành hai file CSV mới
df_2020.to_csv('diem_thi_2020.csv', index=False)
df_2021.to_csv('diem_thi_2021.csv', index=False)

print('Đã tách thành công thành hai bảng cho năm 2020 và 2021')
