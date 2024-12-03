import csv
import os
import requests
import time
# Đường dẫn file CSV chứa điểm thi
file_path = r'C:\Users\Admin\Desktop\BTL_TDA\crawl_data\diem_thi_2019.csv'

# Đọc danh sách SBD đã xử lý từ file điểm thi (CSV)
processed_sbd = set()
max_sbd = 0  # Biến để lưu SBD lớn nhất đã xử lý

if os.path.exists(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sbd = row['sbd']
            processed_sbd.add(sbd)
            # Cập nhật SBD lớn nhất
            max_sbd = max(max_sbd, int(sbd))

# In ra các SBD đã được xử lý và SBD lớn nhất
print("Các SBD đã xử lý từ file điểm thi:")
for sbd in processed_sbd:
    print(sbd)
print(f"SBD lớn nhất đã xử lý là: {max_sbd}")

# Tiếp tục crawl từ SBD lớn nhất + 1
start_sbd = max_sbd + 1

# Chọn mã tỉnh để quét
province_code = input("Nhập mã tỉnh (VD: '01' cho Hà Nội): ").zfill(2)
province_name = 'Tên tỉnh'  # Thêm mã tỉnh của bạn vào đây nếu cần

print(f"Đang tiếp tục crawl từ SBD {start_sbd} cho tỉnh {province_name}...")

# Crawl dữ liệu bắt đầu từ start_sbd
no_data_count = 0
max_no_data = 100  # Ngưỡng dừng nếu không có dữ liệu cho 100 thí sinh liên tiếp

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

print(f"Hoàn tất tiếp tục crawl từ SBD {start_sbd}.")
