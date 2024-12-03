import requests
import csv
import os
import time

# Danh sách mã tỉnh và tên tương ứng
provinces = {
    '01': 'Hà Nội', '02': 'TP. Hồ Chí Minh', '03': 'Hải Phòng', '04': 'Đà Nẵng', '05': 'Hà Giang',
    # Thêm các mã khác vào đây...
}

# Đường dẫn file CSV
file_path = r'C:\Users\Admin\Desktop\BTL_TDA\crawl_data\diem_thi_2019.csv'

# Đọc danh sách SBD đã xử lý
processed_sbd = set()
if os.path.exists(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            processed_sbd.add(row['sbd'])

# Mở file CSV để ghi dữ liệu
with open(file_path, mode='a', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    # Thêm tiêu đề nếu file rỗng
    if os.stat(file_path).st_size == 0:
        writer.writerow(['sbd', 'toan', 'van', 'ngoaiNgu', 'vatLy', 'hoaHoc', 'sinhHoc', 'lichSu', 'diaLy', 'gdcd', 'province_name'])

    # Chọn mã tỉnh để quét
    province_code = input("Nhập mã tỉnh (VD: '01' cho Hà Nội): ").zfill(2)
    province_name = provinces.get(province_code, "Không xác định")

    if province_name == "Không xác định":
        print("Mã tỉnh không hợp lệ!")
    else:
        print(f"Đang xử lý dữ liệu cho tỉnh {province_name}...")

        # Biến đếm số lần không có dữ liệu liên tiếp
        no_data_count = 0
        max_no_data = 100  # Ngưỡng dừng nếu không có dữ liệu cho 100 thí sinh liên tiếp

        for sbd in range(int(province_code) * 1000000 + 1, int(province_code) * 1000000 + 100000):
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
                        writer.writerow(row)
                        processed_sbd.add(str(sbd))
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

            time.sleep(0.5)  # Tránh gửi quá nhiều yêu cầu trong thời gian ngắn

        print(f"Hoàn tất xử lý dữ liệu cho tỉnh {province_name}.")
