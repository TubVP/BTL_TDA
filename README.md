
# Lời mở đầu
Repository này sẽ hướng dẫn chi tiết cách mà chúng em tìm, phân tích và so sánh dữ liệu điểm thi thptqg qua các năm, đồng thời dự báo phân bố điểm thi của các năm sau.

# Mục tiêu 
Tìm hiểu các xu hướng trong kết quả thi qua từng năm và đồng thời xây dựng mô hình dự đoán điểm thi cho các năm tiếp theo, hỗ trợ học sinh và giáo viên trong việc đánh giá kết quả học tập.
 
# Dữ liệu sử dụng
Tổng hợp file csv toàn bộ điểm thi thptqg từ năm 2020-2024 được lấy từ nguồn internet chính thống. Mỗi file đều có đầy đủ các thông tin của thí sinh dự thi như: số báo danh, tỉnh/thành phố, dữ liệu điểm,... 

# Công cụ hỗ trợ
- Ngôn ngữ lập trình: Python với các thư viện phân tích dữ liệu như Pandas, NumPy.
- Công cụ trực quan hóa: Matplotlib, Seaborn để tạo biểu đồ và dashboard.
- Quản lý dữ liệu: Google Sheets hoặc Microsoft Excel để lưu trữ và làm sạch dữ liệu.
- Môi trường làm việc: Notebook, Visual Studio Code và Google Docs để lập trình và ghi chú.

# Phương pháp thực hiện
Trước tiên, chúng em tìm kiếm, sao lưu dữ liệu trên internet, bao gồm các file điểm thi thpt quốc gia 2020-2024 về. Trong giai đoạn tiền xử lý dữ liệu, em sẽ lọc bớt các thông tin không cần thiết như tên thí sinh, ngày sinh và giới tính đi vì đây là các thông tin không cần thiết. Đồng thời bổ sung thêm các cột khác như phân loại thí sinh thi môn tự nhiên hoặc xã hội,... Sau khi đã chỉnh sửa các file đầu vào thì chúng em sẽ thu được dữ liệu có dạng như sau: 

![Screenshot 2024-11-30 221954](https://github.com/user-attachments/assets/22335ee8-aed3-4f6f-9ba0-47e97eba1db9)

Với những dữ liệu đã được chỉnh sửa, chúng em sẽ tiến hành đọc file dữ liệu bằng thư viện numpy:

![image](https://github.com/user-attachments/assets/8cefc453-27d4-4c04-93a2-0c269090dfdc)

Kế tiếp, chúng em tổng hợp các thông tin quan trọng khác của từng file như sau:     
Tổng hợp thông tin thủ khoa các môn tổ hợp:

![image](https://github.com/user-attachments/assets/8564ee80-616c-464b-be83-5f526b3f4808)

Tổng hợp thông tin thủ khoa khối:

![image](https://github.com/user-attachments/assets/f7d9251f-cc27-4580-b234-3913f64c15e3)

![image](https://github.com/user-attachments/assets/d51d2655-ee6e-48ea-903b-c80c870136cd)

Tổng hợp số thí sinh đạt điểm tối đa ở các môn:

![image](https://github.com/user-attachments/assets/161510d7-41c3-46de-a0ad-6e6738a5e748)

![image](https://github.com/user-attachments/assets/ebba9583-37d6-4bfc-b53d-67d8bb698459)

Lập biểu đồ phân bố điểm ở các môn:

![image](https://github.com/user-attachments/assets/9d9823f3-0969-4c5b-9127-836576e715ce)
![image](https://github.com/user-attachments/assets/bb6a55f7-a84b-41dc-8f2b-e0322fd238d7)

![Screenshot 2024-11-30 224541](https://github.com/user-attachments/assets/f92d00dc-56bf-4518-932d-dd45491bdf9f)

![Screenshot 2024-11-30 224550](https://github.com/user-attachments/assets/aa80092d-396d-4005-9f7b-8e95f537ce80)

![Screenshot 2024-11-30 224601](https://github.com/user-attachments/assets/c6638282-7b5f-4aef-8362-a0874d9b4a94)

![Screenshot 2024-11-30 224610](https://github.com/user-attachments/assets/482e88ab-79fe-4ee9-9396-a96995e2f242)

![Screenshot 2024-11-30 224618](https://github.com/user-attachments/assets/81fe5acf-6267-45e0-bdc3-0f54d54b78d3)

![Screenshot 2024-11-30 224625](https://github.com/user-attachments/assets/9f973dc2-d7eb-4089-8e92-0d1d08ed98de)

![Screenshot 2024-11-30 224632](https://github.com/user-attachments/assets/482fb1b5-61fb-4c25-a137-c1f789d3798d)

![Screenshot 2024-11-30 224640](https://github.com/user-attachments/assets/7cb14861-f630-4ba3-8922-e74f7d039481)

![Screenshot 2024-11-30 224652](https://github.com/user-attachments/assets/6c3cecde-1643-4db9-859e-c43d2aea6a04)

Lập biểu đồ so sánh mức điểm ở các môn:

![image](https://github.com/user-attachments/assets/13520274-f336-451e-a937-0af8c389ce79)
![image](https://github.com/user-attachments/assets/16a4def7-aa0a-4ee1-b30c-e0c9fd6bc365)

![Screenshot 2024-11-30 225849](https://github.com/user-attachments/assets/3b8ef54e-36b8-4131-9270-dcd7a9eb260a)

![Screenshot 2024-11-30 225856](https://github.com/user-attachments/assets/9fc3a71a-b7ef-40b1-91a2-e4549117a038)

![Screenshot 2024-11-30 225903](https://github.com/user-attachments/assets/e22c9969-daa6-4eab-bc09-832a1e98afa4)

![Screenshot 2024-11-30 225909](https://github.com/user-attachments/assets/f6853985-32ff-4fa1-ba10-f2d449f06e39)

![Screenshot 2024-11-30 225916](https://github.com/user-attachments/assets/aa077669-b131-4676-9d9a-0a3801205a7e)

![Screenshot 2024-11-30 225923](https://github.com/user-attachments/assets/c8774a31-0e89-47a1-acd1-d9592a1d6d9d)

![Screenshot 2024-11-30 225929](https://github.com/user-attachments/assets/442d23a3-504b-48d8-a202-08b6b2e34ecd)

![Screenshot 2024-11-30 225938](https://github.com/user-attachments/assets/17e2dcc5-4747-4934-86db-4449864b3e4d)

![Screenshot 2024-11-30 225943](https://github.com/user-attachments/assets/d4393513-4d46-4f31-a7f6-ed4c8452eba1)

Lập dashboard hiển thị sự khác biệt về điểm số từng khối và chất lượng thí sinh học khối đó theo tỉnh:

![Screenshot 2024-11-30 230903](https://github.com/user-attachments/assets/9d1266dc-deb4-4157-aaaa-5cd06224696e)
![Screenshot 2024-11-30 230923](https://github.com/user-attachments/assets/62ed59ad-788e-43f7-90f8-44a619df1c40)

Tiếp theo là phần dự báo xu hướng điểm chung vị của các khối A, B, C, D,...

![image](https://github.com/user-attachments/assets/d1f14134-4c7e-44d7-82f3-2c6152c10a7d)

Huấn luyện mô hình và dự báo

![image](https://github.com/user-attachments/assets/007a7536-74a4-4cdc-a2f4-bbbd33eaffbe)

Vẽ biểu đồ thể hiện dự báo

![image](https://github.com/user-attachments/assets/2c665419-a840-49d2-af17-6034275d6ae3)

Biểu đồ nhận được:

![image](https://github.com/user-attachments/assets/80b15a5e-fb1d-4b95-9400-ed78c3ad63ce)






# Đóng góp và phản hồi 
Dữ liệu của chúng em tuy đã được nghiên cứu và phân tích tỉ mỉ, nhưng vẫn sẽ còn phải bố sung thêm trong tương lai. Chúng em luôn đón nhận mọi ý kiến đóng góp và phản hồi để cải thiện dự án. Mọi người đều có thể chia sẻ ý kiến qua github ở nhóm tác giả.

# Nhóm tác giả
- [Chu Thanh Tùng](https://github.com/TubVP)
- [Nguyễn Vũ Quang Anh](https://github.com/quanganh6905)
- [Đặng Đức Duy](https://github.com/duylplsn)
