import pandas as pd


file_path = r'C:\Users\Admin\Desktop\BTL_TDA\crawl_data\diem_thi_2019.csv'
df = pd.read_csv(file_path, encoding='utf-8')

filtered_df = df.dropna(how='all', subset=['toan', 'van', 'ngoaiNgu', 'vatLy', 'hoaHoc', 'sinhHoc', 'lichSu', 'diaLy', 'gdcd'])


if 'sbd' in filtered_df.iloc[0].values:
    header_row = filtered_df.iloc[0]
    filtered_df = filtered_df[1:]  
else:
    header_row = None


filtered_df = filtered_df.drop_duplicates(subset=['sbd'], keep='first')




filtered_df.to_csv(file_path, index=False, encoding='utf-8')
print("Xử lý xong! Các dòng bị trùng đã được xóa.")
