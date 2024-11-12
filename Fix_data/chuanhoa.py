import pandas as pd

df = pd.read_csv('diem_thi_2020.csv')
df1 = pd.read_csv('diem_thi_2021.csv')
df2 = pd.read_csv('diem_thi_thpt_2022.csv')
df3 = pd.read_csv('diem_thi_thpt_2023.csv')
df4 = pd.read_csv('diem_thi_thpt_2024.csv')


cols_to_convert = ['toan', 'ngu_van', 'ngoai_ngu','vat_li','hoa_hoc','sinh_hoc','lich_su','dia_li','gdcd']
df2[cols_to_convert] = df2[cols_to_convert].apply(pd.to_numeric, errors='coerce').astype(float)

df3[cols_to_convert] = df3[cols_to_convert].apply(pd.to_numeric, errors = 'coerce').astype(float)
df4[cols_to_convert] = df4[cols_to_convert].apply(pd.to_numeric, errors = 'coerce').astype(float)

cols_to_convert1 = ['Toán','Văn','Lý','Hoá','Sinh','Lịch Sử','Địa Lý','GDCD','Ngoại Ngữ']

df[cols_to_convert1] = df[cols_to_convert1].apply(pd.to_numeric, errors='coerce').astype(float)
df1[cols_to_convert1] = df1[cols_to_convert1].apply(pd.to_numeric, errors='coerce').astype(float)

print('Chuẩn hoá thành công')