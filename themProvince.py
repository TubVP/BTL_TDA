import pandas as pd

# Tạo DataFrame ánh xạ mã tỉnh với tên tỉnh
province_mapping = {
    '01': 'Hà Nội',
    '02': 'TP. Hồ Chí Minh',
    '03': 'Hải Phòng',
    '04': 'Đà Nẵng',
    '05': 'Hà Giang',
    '06': 'Cao Bằng',
    '07': 'Lai Châu',
    '08': 'Lào Cai',
    '09': 'Tuyên Quang',
    '10': 'Lạng Sơn',
    '11': 'Bắc Kạn',
    '12': 'Thái Nguyên',
    '13': 'Yên Bái',
    '14': 'Sơn La',
    '15': 'Phú Thọ',
    '16': 'Vĩnh Phúc',
    '17': 'Quảng Ninh',
    '18': 'Bắc Giang',
    '19': 'Bắc Ninh',
    '21': 'Hải Dương',
    '22': 'Hưng Yên',
    '23': 'Hòa Bình',
    '24': 'Hà Nam',
    '25': 'Nam Định',
    '26': 'Thái Bình',
    '27': 'Ninh Bình',
    '28': 'Thanh Hoá',
    '29': 'Nghệ An',
    '30': 'Hà Tĩnh',
    '31': 'Quảng Bình',
    '32': 'Quảng Trị',
    '33': 'Thừa Thiên - Huế',
    '34': 'Quảng Nam',
    '35': 'Quảng Ngãi',
    '36': 'Kon Tum',
    '37': 'Bình Định',
    '38': 'Gia Lai',
    '39': 'Phú Yên',
    '40': 'Đắk Lắk',
    '41': 'Khánh Hòa',
    '42': 'Lâm Đồng',
    '43': 'Bình Phước',
    '44': 'Bình Dương',
    '45': 'Ninh Thuận',
    '46': 'Tây Ninh',
    '47': 'Bình Thuận',
    '48': 'Đồng Nai',
    '49': 'Long An',
    '50': 'Đồng Tháp',
    '51': 'An Giang',
    '52': 'Bà Rịa - Vũng Tàu',
    '53': 'Tiền Giang',
    '54': 'Kiên Giang',
    '55': 'Cần Thơ',
    '56': 'Bến Tre',
    '57': 'Vĩnh Long',
    '58': 'Trà Vinh',
    '59': 'Sóc Trăng',
    '60': 'Bạc Liêu',
    '61': 'Cà Mau',
    '62': 'Điện Biên',
    '63': 'Đắk Nông',
    '64': 'Hậu Giang',
}

# Chuyển sang DataFrame
province_df = pd.DataFrame(list(province_mapping.items()), columns=['province_code', 'province_name'])

# Danh sách các file điểm thi
file_list = ['diem_thi_thpt_2022.csv', 'diem_thi_thpt_2023.csv', 'diem_thi_thpt_2024.csv']  # Thay thế bằng tên file thực tế của bạn

# Vòng lặp để thao tác với từng file
for file in file_list:
    # Đọc file
    df = pd.read_csv(file)
    
    # Thêm cột province_code
    df['province_code'] = df['sbd'].astype(str).str[:2]
    
    # Kết hợp để thêm cột province_name
    df = df.merge(province_df, on='province_code', how='left')
    
    # Lưu lại file với cột mới
    df.to_csv(file, index=False)

    print(f"Đã thêm cột province_name vào file {file} và lưu lại.")
