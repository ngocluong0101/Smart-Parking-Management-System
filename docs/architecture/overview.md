# Architecture Overview

## 1. Mục tiêu kiến trúc

Kiến trúc phải đáp ứng 4 yêu cầu chính:

- Dễ mở rộng khi thay đổi model AI hoặc business rule
- Dễ bảo trì nhờ tách layer rõ ràng
- Dễ demo và deploy bằng Docker Compose
- Đủ chuẩn để dùng trong portfolio và phỏng vấn

## 2. Lựa chọn công nghệ

### FastAPI

Ưu điểm:

- Nhanh, nhẹ, chuẩn OpenAPI tự sinh
- Phù hợp làm REST API cho AI product
- Tốt cho async I/O và validation

### SQLAlchemy + MySQL

Ưu điểm:

- ORM phổ biến trong enterprise Python
- Dễ quản lý transaction, relationship, migration
- MySQL phù hợp cho bài toán giao dịch và báo cáo

### YOLOv8/YOLO11

Ưu điểm:

- Hiệu năng tốt cho object detection realtime
- Hệ sinh thái training/export mạnh
- Phù hợp bài toán phát hiện biển số

### PaddleOCR

Lý do chọn PaddleOCR thay vì tự huấn luyện OCR:

- OCR là bài toán rất lớn, cần dữ liệu text đa dạng và pipeline phức tạp
- Tự huấn luyện OCR từ đầu tốn thời gian, dữ liệu và chi phí gán nhãn rất cao
- PaddleOCR đã tối ưu sẵn cho detection + recognition + post-processing
- Ta chỉ cần tập trung phần giá trị cao hơn: phát hiện biển số, chuẩn hóa, và business flow

## 3. Luồng xử lý tổng quát

1. Camera gửi frame sang inference service
2. YOLO detect biển số
3. Crop vùng biển số
4. PaddleOCR đọc ký tự
5. Regex chuẩn hóa biển số
6. Backend kiểm tra database
7. Tạo session hoặc đóng session
8. Dashboard cập nhật trạng thái qua API

## 4. Kiến trúc lớp backend

- Controllers: nhận request, trả response
- Services: xử lý business logic
- Repositories: truy cập database
- Schemas/DTO: validate và serialize dữ liệu
- Models: ánh xạ database
- Middleware: logging, auth, tracing
- Exception handling: chuẩn hóa lỗi trả về

## 5. Nguyên tắc thiết kế

- Single responsibility cho từng module
- Không để controller chứa business logic
- Không để service truy cập SQL trực tiếp
- Tách AI inference khỏi business logic càng nhiều càng tốt
- Dữ liệu nghiệp vụ phải được lưu qua transaction
