import csv
import os

# Đường dẫn file CSV chứa điểm thi
file_path = r'C:\Users\Admin\Desktop\BTL_TDA\crawl_data\diem_thi_2019.csv'

# Hàm chuyển đổi SBD từ string -> float -> int
def convert_sbd(sbd):
    try:
       
        sbd_float = float(sbd)
   
        return str(int(sbd_float))
    except ValueError:
        return sbd  

# Kiểm tra nếu file tồn tại
if os.path.exists(file_path):
    # Đọc file CSV, kiểm tra tiêu đề và sửa lại cột 'sbd'
    with open(file_path, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)  # Dùng DictReader để dễ dàng thao tác với các cột

        # Đọc dữ liệu vào list
        rows = list(reader)

    # Kiểm tra nếu cột 'sbd' có tồn tại trong tiêu đề
    if 'sbd' not in rows[0]:
        print("Lỗi: Cột 'sbd' không tồn tại trong tiêu đề.")
        exit()

    # Mở lại file để ghi dữ liệu đã sửa
    with open(file_path, mode='w', encoding='utf-8', newline='') as outfile:
        fieldnames = rows[0].keys()  # Lấy các tên cột từ dòng đầu tiên

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Ghi lại tiêu đề vào file
        writer.writeheader()

        # Đọc từng dòng, sửa cột 'sbd' và ghi lại vào file cũ
        for row in rows:
            print(f"Trước khi sửa: {row['sbd']}")  # In ra giá trị cũ của SBD
            row['sbd'] = convert_sbd(row['sbd'])  # Chuyển đổi cột 'sbd' từ string -> float -> int
            print(f"Sau khi sửa: {row['sbd']}")  # In ra giá trị mới của SBD
            writer.writerow(row)  # Ghi lại dòng đã sửa

    print("Đã chuyển đổi cột SBD và lưu lại vào file cũ.")
else:
    print(f"File {file_path} không tồn tại.")
