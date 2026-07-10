# Phase 3: Thiết Kế Database

Phase 3 biến yêu cầu nghiệp vụ thành schema có thể chạy thật. Đây là bước rất quan trọng vì database không chỉ để lưu dữ liệu, mà còn quyết định tốc độ dashboard, độ ổn định của session check-in/check-out và khả năng truy vết lịch sử.

## 1. Mục tiêu của phase

- Thiết kế schema chuẩn hóa cho toàn hệ thống
- Đảm bảo lưu được xe đang gửi, lịch sử gửi xe, người dùng, vai trò, phí và audit log
- Thiết kế index để dashboard và lịch sử truy vấn nhanh
- Chốt relationship, primary key, foreign key và constraint
- Chuẩn bị schema để sau này dùng SQLAlchemy migration dễ dàng

## 2. Kiến thức cần có

- ER modeling
- Normalization
- Primary key và foreign key
- Index design
- Transaction và locking cơ bản
- Audit log pattern
- Time-based business rules cho parking fee

## 3. Tư duy thiết kế database

Bài toán bãi đỗ xe không chỉ là CRUD. Nó có các đặc điểm sau:

- Một xe có thể vào và ra nhiều lần
- Một biển số có thể gắn với nhiều session theo thời gian
- Xe đang gửi phải được truy vấn rất nhanh
- Doanh thu hôm nay cần aggregate theo thời gian
- Dữ liệu lịch sử phải giữ nguyên để audit

Vì vậy database cần được thiết kế theo hướng:

- Vehicle là thực thể gốc của biển số xe
- ParkingSession là thực thể trung tâm cho nghiệp vụ vào/ra
- ParkingFee là bảng rule tính phí
- User, Role và AuditLog phục vụ quản trị hệ thống
- ParkingLot giúp mở rộng sang nhiều bãi hoặc nhiều khu vực

## 4. Kiến trúc dữ liệu

### 4.1 Các thực thể chính

- Role: vai trò người dùng
- User: tài khoản nội bộ
- Vehicle: thông tin xe và biển số
- ParkingLot: thông tin bãi đỗ
- ParkingFee: rule tính phí
- ParkingSession: phiên gửi xe
- AuditLog: nhật ký thao tác

### 4.2 Luồng dữ liệu chính

1. Camera vào nhận diện biển số
2. Backend kiểm tra Vehicle theo plate_number
3. Nếu chưa có thì tạo Vehicle
4. Tạo ParkingSession với trạng thái active
5. Khi xe ra, tìm session active của Vehicle
6. Tính thời gian gửi và fee
7. Đóng session, lưu check_out_time và total_fee
8. Ghi audit log cho thao tác quan trọng

## 5. Thiết kế bảng chi tiết

### 5.1 Role

Mục đích:

- Lưu danh sách vai trò hệ thống

Fields:

- id: PK
- name: tên role, unique
- description: mô tả role
- created_at, updated_at

Quan hệ:

- Một Role có nhiều User

### 5.2 User

Mục đích:

- Lưu tài khoản đăng nhập cho admin và operator

Fields:

- id: PK
- role_id: FK -> Role.id
- username: unique
- password_hash: mật khẩu đã hash
- full_name: tên hiển thị
- email: tùy chọn
- is_active: trạng thái tài khoản
- last_login_at: lần đăng nhập gần nhất
- created_at, updated_at

Index:

- username
- role_id

### 5.3 Vehicle

Mục đích:

- Lưu thông tin định danh của xe theo biển số

Fields:

- id: PK
- plate_number: unique, đã chuẩn hóa
- vehicle_type: car, motorbike, bicycle, truck...
- brand: hãng xe
- color: màu xe
- owner_name: tên chủ xe nếu cần
- created_at, updated_at

Index:

- plate_number
- vehicle_type

### 5.4 ParkingLot

Mục đích:

- Lưu thông tin bãi đỗ hoặc khu vực đỗ

Fields:

- id: PK
- name: tên bãi
- location: vị trí
- capacity: sức chứa tối đa
- is_active: trạng thái
- created_at, updated_at

### 5.5 ParkingFee

Mục đích:

- Lưu rule tính phí theo loại xe hoặc cấu hình hệ thống

Fields:

- id: PK
- vehicle_type: loại xe áp dụng
- base_fee: phí cơ bản
- fee_rule: mô tả rule
- unit: theo lượt, theo giờ, theo ngày
- effective_from: ngày hiệu lực
- effective_to: ngày kết thúc hiệu lực
- is_active: trạng thái
- created_at, updated_at

Index:

- vehicle_type
- is_active
- effective_from

### 5.6 ParkingSession

Mục đích:

- Bảng quan trọng nhất, lưu một lượt gửi xe

Fields:

- id: PK
- vehicle_id: FK -> Vehicle.id
- parking_lot_id: FK -> ParkingLot.id
- parking_fee_id: FK -> ParkingFee.id
- check_in_time: thời gian vào
- check_out_time: thời gian ra, nullable
- status: active, closed, duplicate, invalid
- vehicle_type_snapshot: snapshot loại xe tại thời điểm vào
- plate_raw: biển số thô từ OCR
- plate_normalized: biển số sau chuẩn hóa
- entry_image_path: ảnh lúc vào
- exit_image_path: ảnh lúc ra
- duration_minutes: thời gian gửi tính bằng phút
- total_fee: số tiền phải trả
- notes: ghi chú
- created_at, updated_at

Index:

- vehicle_id
- parking_lot_id
- status
- check_in_time
- check_out_time
- plate_normalized

Constraints:

- Một Vehicle chỉ nên có một session active tại một thời điểm
- check_out_time chỉ được có khi status đã closed
- total_fee không âm

### 5.7 AuditLog

Mục đích:

- Ghi nhận thao tác quan trọng để truy vết

Fields:

- id: PK
- user_id: FK -> User.id, nullable nếu action từ system
- action: create, update, delete, check_in, check_out, login...
- entity_name: tên bảng hoặc domain
- entity_id: id của record liên quan
- old_value: dữ liệu cũ dạng json/text
- new_value: dữ liệu mới dạng json/text
- ip_address: địa chỉ IP
- user_agent: thông tin client
- created_at

Index:

- user_id
- action
- entity_name
- created_at

## 6. Relationship

- Role 1-n User
- User 1-n AuditLog
- Vehicle 1-n ParkingSession
- ParkingLot 1-n ParkingSession
- ParkingFee 1-n ParkingSession

## 7. Primary key, foreign key, unique key

### Primary key

- Dùng bigint auto increment hoặc uuid tùy cài đặt cuối cùng
- Với dự án portfolio, bigint dễ đọc và dễ debug hơn

### Foreign key

- user.role_id -> role.id
- parking_session.vehicle_id -> vehicle.id
- parking_session.parking_lot_id -> parking_lot.id
- parking_session.parking_fee_id -> parking_fee.id
- audit_log.user_id -> user.id

### Unique key

- vehicle.plate_number
- user.username
- role.name

## 8. Index strategy

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

## 9. Best practice

- Chuẩn hóa biển số trước khi lưu vào vehicle và parking_session
- Tách bảng fee thành rule riêng để thay đổi chính sách không phải sửa code nhiều
- Lưu snapshot vehicle_type và plate_raw trong session để phục vụ audit
- Dùng timestamp đầy đủ để tính phí chính xác
- Không xóa cứng session lịch sử nếu yêu cầu audit còn cần dữ liệu
- Tối ưu query dashboard bằng index và aggregate hợp lý

## 10. Các lỗi thường gặp

- Lưu biển số chưa chuẩn hóa dẫn đến trùng dữ liệu
- Chỉ lưu một bảng session mà không có snapshot, khiến lịch sử khó truy vết
- Không có index cho plate_number nên search chậm
- Thiết kế fee bằng hardcode thay vì bảng cấu hình
- Không phân biệt session active và closed
- Thiếu audit log cho thao tác quan trọng

## 11. Cách debug

- Kiểm tra dữ liệu theo từng bước: vehicle, session, fee, audit
- Test query theo các trường index chính trước
- Dùng dữ liệu mẫu cho ca vào/ra hợp lệ và không hợp lệ
- Kiểm tra một plate_number xuyên suốt toàn bộ vòng đời session
- Quan sát transaction khi tạo session và khi đóng session
- Verify rule tính phí bằng các case thời gian khác nhau

## 12. Checklist hoàn thành

- [ ] Chốt danh sách bảng
- [ ] Chốt field cho từng bảng
- [ ] Chốt PK, FK, unique key
- [ ] Chốt index
- [ ] Chốt rule session active/closed
- [ ] Chốt rule tính phí
- [ ] Chốt audit log strategy
- [ ] Viết schema SQL ban đầu
- [ ] Cập nhật ER diagram

## 13. Kết quả đầu ra của phase

Sau phase này, database phải đủ rõ để bắt đầu scaffold model SQLAlchemy, migration và repository layer mà không cần đoán schema nữa.
