# Database Design

## 1. Mục tiêu

Database phải hỗ trợ:

- Lưu xe đang gửi
- Lưu lịch sử vào/ra
- Quản lý người dùng và vai trò
- Lưu audit log
- Tối ưu truy vấn dashboard và lịch sử

## 2. Nguyên tắc thiết kế

- Normalize dữ liệu để tránh trùng lặp
- Dùng khóa chính surrogate key bằng bigint để debug và join dễ hơn
- Thêm index cho biển số, thời gian vào/ra, trạng thái session
- Dùng foreign key để đảm bảo toàn vẹn
- Thiết kế bảng lịch sử theo hướng append-only càng nhiều càng tốt
- Lưu snapshot của dữ liệu quan trọng tại thời điểm phát sinh sự kiện

## 3. Mô hình dữ liệu trung tâm

### 3.1 Vehicle

Lưu thông tin nhận diện xe theo biển số đã chuẩn hóa.

Fields chính:

- id
- plate_number
- vehicle_type
- brand
- color
- owner_name
- created_at
- updated_at

### 3.2 ParkingSession

Lưu từng lượt gửi xe, là bảng nghiệp vụ trung tâm.

Fields chính:

- id
- vehicle_id
- parking_lot_id
- parking_fee_id
- check_in_time
- check_out_time
- status
- plate_raw
- plate_normalized
- vehicle_type_snapshot
- entry_image_path
- exit_image_path
- duration_minutes
- total_fee
- notes
- created_at
- updated_at

### 3.3 ParkingLot

Lưu thông tin bãi đỗ hoặc khu vực đỗ.

### 3.4 ParkingFee

Lưu rule tính phí theo loại xe hoặc chính sách bãi xe.

### 3.5 Role

Lưu role cho hệ thống quản trị.

### 3.6 User

Lưu tài khoản nội bộ với phân quyền.

### 3.7 AuditLog

Lưu nhật ký thao tác để truy vết và kiểm toán.

## 4. Relationship

- Role 1-n User
- User 1-n AuditLog
- Vehicle 1-n ParkingSession
- ParkingLot 1-n ParkingSession
- ParkingFee 1-n ParkingSession

## 5. Primary key, foreign key, unique key

### Primary key

- Dùng bigint auto increment cho toàn bộ bảng chính

### Foreign key

- user.role_id -> role.id
- parking_session.vehicle_id -> vehicle.id
- parking_session.parking_lot_id -> parking_lot.id
- parking_session.parking_fee_id -> parking_fee.id
- audit_log.user_id -> user.id

### Unique key

- role.name
- user.username
- vehicle.plate_number

## 6. Index strategy

Index cần ưu tiên cho các query thực tế:

- Tìm xe theo biển số
- Lấy session active gần nhất
- Lọc lịch sử theo thời gian
- Tính doanh thu theo ngày
- Lọc dashboard theo loại xe và trạng thái

Đề xuất:

- vehicle(plate_number)
- parking_session(vehicle_id, status)
- parking_session(check_in_time)
- parking_session(check_out_time)
- parking_session(plate_normalized)
- user(username)
- audit_log(created_at)

## 7. Trạng thái ParkingSession

- active: xe đang gửi
- closed: xe đã ra
- duplicate: phát hiện biển số trùng khi check-in
- invalid: dữ liệu không hợp lệ hoặc không thể xử lý

## 8. Gợi ý truy vấn nghiệp vụ

- Query xe đang gửi: status = active
- Query lịch sử hôm nay: lọc theo check_in_time hoặc check_out_time
- Query doanh thu hôm nay: sum(total_fee) theo ngày check_out_time
- Query xe đang trong bãi: status = active và parking_lot_id tương ứng

## 9. Constraint đề xuất

- total_fee >= 0
- duration_minutes >= 0
- check_out_time >= check_in_time khi session đã closed
- một vehicle chỉ có tối đa một session active tại cùng thời điểm
- plate_number phải được chuẩn hóa trước khi lưu

## 10. Best practice

- Chuẩn hóa biển số trước khi lưu vào vehicle và parking_session
- Tách bảng fee thành rule riêng để thay đổi chính sách không phải sửa code nhiều
- Lưu snapshot vehicle_type và plate_raw trong session để phục vụ audit
- Dùng timestamp đầy đủ để tính phí chính xác
- Không xóa cứng session lịch sử nếu yêu cầu audit còn cần dữ liệu
- Tối ưu query dashboard bằng index và aggregate hợp lý

## 11. Các lỗi thường gặp

- Lưu biển số chưa chuẩn hóa dẫn đến trùng dữ liệu
- Chỉ lưu một bảng session mà không có snapshot, khiến lịch sử khó truy vết
- Không có index cho plate_number nên search chậm
- Thiết kế fee bằng hardcode thay vì bảng cấu hình
- Không phân biệt session active và closed
- Thiếu audit log cho thao tác quan trọng

## 12. Cách debug

- Kiểm tra dữ liệu theo từng bước: vehicle, session, fee, audit
- Test query theo các trường index chính trước
- Dùng dữ liệu mẫu cho ca vào/ra hợp lệ và không hợp lệ
- Kiểm tra một plate_number xuyên suốt toàn bộ vòng đời session
- Quan sát transaction khi tạo session và khi đóng session
- Verify rule tính phí bằng các case thời gian khác nhau

## 13. Kết luận

Schema này là nền cho toàn bộ backend. Khi phase 4 bắt đầu, ta sẽ map trực tiếp schema này sang SQLAlchemy models và migration thay vì thiết kế lại từ đầu.
