import csv
import os
import requests
import time


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


file_path = r'C:\Users\Admin\Desktop\BTL_TDA\crawl_data\diem_thi_2019.csv'


processed_sbd = set()
max_sbd_dict = {} 

if os.path.exists(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sbd = row['sbd']
            province_code = sbd[:2]  
            processed_sbd.add(sbd)
            max_sbd_dict[province_code] = max(max_sbd_dict.get(province_code, 0), int(sbd))

while True:
   
    province_code = input("Nhập mã tỉnh (hoặc 'exit' để thoát): ").zfill(2)
    if province_code.lower() == 'exit':
        print("Kết thúc chương trình.")
        break

    province_name = provinces.get(province_code, None)
    if province_name is None:
        print(f"Mã tỉnh {province_code} không hợp lệ. Vui lòng kiểm tra lại!")
        continue

   
    province_base = int(province_code) * 1_000_000
    max_sbd = max_sbd_dict.get(province_code, province_base - 1)
    start_sbd = max(max_sbd + 1, province_base)

    print(f"Bắt đầu crawl từ SBD: {start_sbd} cho tỉnh {province_name}...")

    no_data_count = 0
    max_no_data = 100 

    for sbd in range(start_sbd, start_sbd + 100000): 
        if str(sbd) in processed_sbd:
            print(f"SBD {sbd} đã được xử lý, bỏ qua.")
            continue

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
                        student.get('sinhHoc'),
                        student.get('lichSu'),
                        student.get('diaLy'),
                        student.get('gdcd'),
                        province_name
                    ]
                    with open(file_path, mode='a', encoding='utf-8', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(row)
                        processed_sbd.add(str(sbd))
                        max_sbd_dict[province_code] = sbd  # Cập nhật SBD lớn nhất
                        no_data_count = 0  # Reset đếm khi có dữ liệu
                else:
                    no_data_count += 1
            else:
                print(f"Lỗi yêu cầu trang SBD {sbd}, mã trạng thái: {response.status_code}")
                no_data_count += 1
        except Exception as e:
            print(f"Lỗi xử lý SBD {sbd}: {e}")
            no_data_count += 1

        # Dừng nếu liên tiếp không có dữ liệu
        if no_data_count >= max_no_data:
            print("Liên tục không có dữ liệu, dừng quét.")
            break

        time.sleep(0.3)  # Tránh gửi quá nhiều yêu cầu trong thời gian ngắn

    print(f"Hoàn tất crawl cho tỉnh {province_name}.") 