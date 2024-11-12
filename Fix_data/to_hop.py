import pandas as pd

# Danh sách các file
files = ['diem_thi_2020.csv', 'diem_thi_2021.csv', 'diem_thi_2022.csv', 'diem_thi_2023.csv', 'diem_thi_2024.csv']

# Hàm chuẩn hóa tên cột
def standardize_columns(df):
    column_mapping = {
        'Toán': 'Toán', 'Lý': 'Lý', 'Hoá': 'Hoá', 'Sinh': 'Sinh',
        'Văn': 'Văn', 'Lịch Sử': 'Sử', 'Địa Lý': 'Địa', 'GDCD': 'GDCD', 'Ngoại Ngữ': 'Ngoại Ngữ',
        'toan': 'Toán', 'vat_li': 'Lý', 'hoa_hoc': 'Hoá', 'sinh_hoc': 'Sinh',
        'ngu_van': 'Văn', 'lich_su': 'Sử', 'dia_li': 'Địa', 'gdcd': 'GDCD', 'ngoai_ngu': 'Ngoại Ngữ'
    }
    df = df.rename(columns=column_mapping)
    return df

# Hàm phân loại Tự nhiên và Xã hội
def classify(row):
    try:
        # Các môn Tự nhiên và Xã hội
        natural_subjects = ['Lý', 'Hoá', 'Sinh']
        social_subjects = ['Sử', 'Địa', 'GDCD']
        
        # Kiểm tra điểm của các môn Tự nhiên và Xã hội
        has_natural = any([pd.notna(row[subject]) and row[subject] > 0 for subject in natural_subjects])
        has_social = any([pd.notna(row[subject]) and row[subject] > 0 for subject in social_subjects])
        
        # Phân loại dựa trên các môn thi có điểm
        if has_natural and not has_social:
            return 'Tự nhiên'
        elif has_social and not has_natural:
            return 'Xã hội'
        else:
            return 'Không phân loại'
    except Exception as e:
        print(f"Lỗi trong hàm classify với dữ liệu row: {row}")
        print(f"Lỗi: {e}")
        return 'Lỗi'

# Xử lý từng file
for file in files:
    try:
        file_path = f"D:/BTL_TDA/Data/{file}"
        print(f"Đang xử lý file: {file}")
        df = pd.read_csv(file_path)
        
        # Kiểm tra cột 'phan_loai'
        if 'phan_loai' not in df.columns:
            print(f"File {file} không có cột 'phan_loai'. Bỏ qua file này.")
            continue
        
        # Chuẩn hóa tên cột
        df = standardize_columns(df)
        
        # Áp dụng phân loại và thêm cột 'to_hop' cho thí sinh thi lần đầu
        df['to_hop'] = df.apply(lambda row: classify(row) if row['phan_loai'] == 'thi lan dau' else None, axis=1)
        
        # Ghi lại file đã xử lý
        df.to_csv(file_path, index=False)
        print(f"Đã lưu dữ liệu có cột 'to_hop' vào file {file}")
    
    except Exception as e:
        print(f"Đã xảy ra lỗi khi xử lý file {file}: {e}")
