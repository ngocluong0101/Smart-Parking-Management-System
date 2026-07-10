# Software Requirement Specification

## 1. Giới thiệu

### 1.1 Mục đích

Hệ thống Smart Parking Management System dùng Computer Vision để tự động nhận diện xe vào/ra, đọc biển số, quản lý phiên gửi xe và hỗ trợ dashboard quản trị.

### 1.2 Phạm vi

- Nhận diện biển số xe từ camera
- OCR biển số
- Lưu thông tin xe và phiên gửi xe
- Tính phí gửi xe
- Quản lý lịch sử và thống kê
- Cung cấp REST API và web dashboard

### 1.3 Đối tượng sử dụng

- Admin
- Nhân viên vận hành bãi xe
- Hệ thống camera/inference service

## 2. Tác nhân

- Admin: quản lý toàn bộ hệ thống, người dùng, cấu hình
- Operator: vận hành camera, xử lý cảnh báo, xem dashboard
- AI Service: xử lý ảnh, detect biển số, OCR
- Database: lưu dữ liệu giao dịch và lịch sử

## 3. Yêu cầu chức năng

### 3.1 Camera vào

- Phát hiện xe đi vào
- Detect biển số
- OCR biển số
- Kiểm tra biển số trong database
- Nếu chưa có: tạo parking session, lưu thời gian vào, lưu ảnh
- Nếu đã có: hiển thị cảnh báo trùng

### 3.2 Camera ra

- Phát hiện xe đi ra
- OCR biển số
- Kiểm tra session đang mở
- Tính thời gian gửi
- Tính phí
- Lưu lịch sử ra xe
- Cập nhật trạng thái session

### 3.3 Dashboard

- Tổng số xe đang gửi
- Số xe máy, ô tô
- Doanh thu hôm nay
- Số lượt xe
- Biểu đồ thống kê
- Danh sách xe đang trong bãi và xe đã ra

### 3.4 Quản lý xe

- Thêm, sửa, xóa, tìm kiếm
- Tìm theo biển số, loại xe, ngày gửi

### 3.5 Lịch sử

- Hiển thị biển số, giờ vào, giờ ra, thời gian gửi, phí, ảnh xe

### 3.6 Quản trị người dùng

- Đăng nhập, phân quyền theo role
- Quản lý tài khoản nội bộ

## 4. Yêu cầu phi chức năng

- Hiệu năng: đáp ứng xử lý gần realtime ở mức demo thực tế
- Bảo mật: JWT, phân quyền, validate input
- Mở rộng: tách layer rõ ràng để dễ thay thế model AI
- Quan sát: logging, audit log, error tracing
- Tái sử dụng: service/repository tách biệt

## 5. Ràng buộc

- Backend dùng FastAPI
- AI detection tự huấn luyện
- OCR dùng PaddleOCR
- Database dùng MySQL
- Frontend dùng React + TypeScript

## 6. Tiêu chí chấp nhận

- Nhận diện được xe vào/ra từ ảnh/video demo
- Lưu và truy vấn session chính xác
- Dashboard hiển thị số liệu cơ bản
- API có tài liệu Swagger
- Chạy được bằng Docker Compose
