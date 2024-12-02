import requests
import csv
import time

# Danh sách mã tỉnh và tên tương ứng
provinces = {
    '01': 'Hà Nội', '02': 'TP. Hồ Chí Minh', '03': 'Hải Phòng', '04': 'Đà Nẵng', '05': 'Hà Giang',
    '06': 'Cao Bằng', '07': 'Lai Châu', '08': 'Lào Cai', '09': 'Tuyên Quang', '10': 'Lạng Sơn',
    '11': 'Bắc Kạn', '12': 'Thái Nguyên', '13': 'Yên Bái', '14': 'Sơn La', '15': 'Phú Thọ',
    '16': 'Vĩnh Phúc', '17': 'Quảng Ninh', '18': 'Bắc Giang', '19': 'Bắc Ninh', '21': 'Hải Dương',
    '22': 'Hưng Yên', '23': 'Hòa Bình', '24': 'Hà Nam', '25': 'Nam Định', '26': 'Thái Bình',
    '27': 'Ninh Bình', '28': 'Thanh Hoá', '29': 'Nghệ An', '30': 'Hà Tĩnh', '31': 'Quảng Bình',
    '32': 'Quảng Trị', '33': 'Thừa Thiên - Huế', '34': 'Quảng Nam', '35': 'Quảng Ngãi', '36': 'Kon Tum',
    '37': 'Bình Định', '38': 'Gia Lai', '39': 'Phú Yên', '40': 'Đắk Lắk', '41': 'Khánh Hòa',
    '42': 'Lâm Đồng', '43': 'Bình Phước', '44': 'Bình Dương', '45': 'Ninh Thuận', '46': 'Tây Ninh',
    '47': 'Bình Thuận', '48': 'Đồng Nai', '49': 'Long An', '50': 'Đồng Tháp', '51': 'An Giang',
    '52': 'Bà Rịa - Vũng Tàu', '53': 'Tiền Giang', '54': 'Kiên Giang', '55': 'Cần Thơ', '56': 'Bến Tre',
    '57': 'Vĩnh Long', '58': 'Trà Vinh', '59': 'Sóc Trăng', '60': 'Bạc Liêu', '61': 'Cà Mau',
    '62': 'Điện Biên', '63': 'Đắk Nông', '64': 'Hậu Giang',
}

# Mở file CSV để ghi dữ liệu
with open('diem_thi_2019.csv', mode='a', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    
    # Thêm tiêu đề nếu file rỗng
    try:
        with open('diem_thi_2019.csv', 'r', encoding='utf-8') as check_file:
            if not check_file.read().strip():
                writer.writerow(['sbd', 'toan', 'van', 'ngoaiNgu', 'vatLy', 'hoaHoc', 'lichSu', 'diaLy', 'gdcd', 'province_name'])
    except FileNotFoundError:
        writer.writerow(['sbd', 'toan', 'van', 'ngoaiNgu', 'vatLy', 'hoaHoc', 'lichSu', 'diaLy', 'gdcd', 'province_name'])

    # Chọn mã tỉnh để quét
    province_code = input("Nhập mã tỉnh (VD: '01' cho Hà Nội): ").zfill(2)
    province_name = provinces.get(province_code, "Không xác định")

    if province_name == "Không xác định":
        print("Mã tỉnh không hợp lệ!")
    else:
        print(f"Đang xử lý dữ liệu cho tỉnh {province_name}...")

        for sbd in range(int(province_code) * 1000000 + 1, int(province_code) * 1000000 + 100000):
            scraping_url = f"https://dantri.com.vn/thpt/1/0/99/{sbd}/2019/0.2/search-gradle.htm"
            try:
                response = requests.get(scraping_url, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    student = data.get('student', {})
                    if student:
                        row = [
                            student.get('sbd'),
                            student.get('toan'),
                            student.get('van'),
                            student.get('ngoaiNgu'),
                            student.get('vatLy'),
                            student.get('hoaHoc'),
                            student.get('lichSu'),
                            student.get('diaLy'),
                            student.get('gdcd'),
                            province_name
                        ]
                        writer.writerow(row)
                else:
                    print(f"Lỗi yêu cầu trang SBD {sbd}, mã trạng thái: {response.status_code}")
                time.sleep(0.5)
            except Exception as e:
                print(f"Lỗi xử lý SBD {sbd}: {e}")
        print(f"Hoàn tất xử lý dữ liệu cho tỉnh {province_name}.")
