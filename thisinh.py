import pandas as pd

df = pd.read_csv('diem_thi_thpt_2024.csv')
df1 = pd.read_csv('diem_thi_thpt_2022.csv')
df2 = pd.read_csv('diem_thi_thpt_2023.csv')
df3 = pd.read_csv('diem_thi_2021.csv')
df4 = pd.read_csv('diem_thi_2020.csv')
def phanloai(row):
     so_mon_thi = sum([1 for mon in ['toan','ngu_van','ngoai_ngu','vat_li','hoa_hoc','sinh_hoc','lich_su','dia_li'] if pd.notna(row[mon]) and row[mon] != 0])
     if so_mon_thi == 3:
          return 'tu do'
     else:
          return 'thi lan dau'

def phanloai1(row):
    so_mon_thi = sum([1 for mon in ['Toán','Văn','Lý','Hoá','Sinh','Lịch Sử','Địa Lý','Ngoại Ngữ'] if pd.notna(row[mon]) and row[mon] != 0])
    if so_mon_thi == 3:
          return 'tu do'
    else:
          return 'thi lan dau'
    

df['phan_loai'] = df.apply(phanloai, axis= 1)
df.to_csv('diem_thi_thpt_2024.csv', index= False)
df1['phan_loai'] = df1.apply(phanloai, axis= 1)
df1.to_csv('diem_thi_thpt_2022.csv', index= False)

df2['phan_loai'] = df2.apply(phanloai, axis= 1)
df2.to_csv('diem_thi_thpt_2023.csv', index= False)

df3['phan_loai'] = df3.apply(phanloai1, axis= 1)
df3.to_csv('diem_thi_2021.csv', index= False)

df4['phan_loai'] = df4.apply(phanloai1, axis= 1)
df4.to_csv('diem_thi_2020.csv', index= False)

print("Đã thêm thành công")