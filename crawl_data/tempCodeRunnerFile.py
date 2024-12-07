import pandas as pd


file_path = r'C:\Users\Admin\Desktop\BTL_TDA\crawl_data\diem_thi_2019.csv'
df = pd.read_csv(file_path, encoding='utf-8')

filtered_df = df.dropna(how='all', subset=['toan', 'van', 'ngoaiNgu', 'vatLy', 'hoaHoc', 'sinhHoc', 'lichSu', 'diaLy', 'gdcd'])

# Giữ dòng đầu tiên làm tiêu đề (giả sử tiêu đề luôn xuất hiện đầu tiên)
if 'sbd' in filtered_df.iloc[0].values:
    header_row = filtered_df.iloc[0]
    filtered_df = filtered_df[1:]  # Loại bỏ dòng tiêu đề tạm thời
else:
    header_row = None

# Loại bỏ các dòng trùng lặp dựa trên 'sbd'
filtered_df = filtered_df.drop_duplicates(subset=['sbd'], keep='first')



# Ghi lại dữ liệu vào file CSV
filtered_df.to_csv(file_path, index=False, encoding='utf-8')
print("Xử lý xong! Các dòng bị trùng đã được xóa.")
