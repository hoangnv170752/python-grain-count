# Phát Hiện và So Sánh Số Lượng Hạt (Grain Count Detection)

## Tổng Quan Dự Án (Project Overview)
Đây là ứng dụng Streamlit để phát hiện và đếm số lượng hạt trong hình ảnh sử dụng kỹ thuật thị giác máy tính. Ứng dụng hỗ trợ tải lên và so sánh hai hình ảnh khác nhau.

## DEMO VIDEO
https://www.loom.com/share/4abfc61c849a432abed656d23146e245?sid=9dc3a57a-27a5-4bf2-91d6-0e8967f48141

## Hướng Dẫn Cài Đặt (Setup Instructions)
1. Clone repository
2. Tạo môi trường ảo (virtual environment)
3. Cài đặt các thư viện phụ thuộc:
   ```
   pip install -r requirements.txt
   ```
4. Chạy ứng dụng:
   ```
   streamlit run app.py
   ```

## Các Thành Phần Chính (Key Components)

### 1. Xử Lý Hình Ảnh (Image Processing)
Mô-đun `image_processing.py` chứa logic xử lý hình ảnh:
- Chuyển đổi hình ảnh sang thang độ xám (grayscale)
- Áp dụng làm mờ Gaussian để giảm nhiễu (Gaussian blur)
- Sử dụng ngưỡng thích ứng (adaptive thresholding) để tạo hình ảnh nhị phân

### 2. Đếm Hạt (Grain Counting)
Mô-đun `grain_counter.py` chứa thuật toán đếm hạt:
- Tìm các đường viền (contours) trong hình ảnh đã xử lý
- Lọc các đường viền dựa trên diện tích để loại bỏ nhiễu
- Đếm số lượng đường viền còn lại để xác định số lượng hạt

### 3. Giao Diện Người Dùng (User Interface)
File `app.py` triển khai giao diện người dùng Streamlit:
- Cho phép tải lên hai hình ảnh để so sánh
- Hiển thị hình ảnh gốc và hình ảnh đã xử lý
- Hiển thị số lượng hạt được phát hiện trong mỗi hình ảnh
- Tính toán và hiển thị sự chênh lệch số lượng hạt giữa hai hình ảnh

## Luồng Xử Lý (Processing Flow)
1. Người dùng tải lên hình ảnh từ thiết bị của họ
2. Hình ảnh được đọc và chuyển đổi thành mảng NumPy
3. Hình ảnh được tiền xử lý qua các bước:
   - Chuyển đổi sang thang độ xám
   - Áp dụng làm mờ Gaussian
   - Áp dụng ngưỡng thích ứng
4. Thuật toán tìm đường viền được áp dụng trên hình ảnh đã xử lý
5. Các đường viền được lọc dựa trên diện tích
6. Số lượng đường viền còn lại được đếm và hiển thị
7. Nếu có hai hình ảnh, sự chênh lệch số lượng hạt sẽ được tính toán

## Sử Dụng (Usage)
1. Tải lên hình ảnh thứ nhất từ thanh bên trái
2. Tải lên hình ảnh thứ hai (tùy chọn)
3. Xem hình ảnh gốc và hình ảnh đã xử lý
4. Xem kết quả đếm số lượng hạt
5. Nếu đã tải lên hai hình ảnh, xem sự chênh lệch số lượng hạt