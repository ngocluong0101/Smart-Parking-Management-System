# Phase 7: Xây Dựng API Nghiệp Vụ

Phase 7 là nơi AI pipeline bắt đầu tạo ra giá trị nghiệp vụ thật. Backend sẽ nhận dữ liệu từ OCR/inference, quản lý vehicle, parking session, fee, history và dashboard.

## 1. Mục tiêu của phase

- Quản lý vehicle, parking session, parking fee và lịch sử
- Xử lý check-in/check-out từ camera vào/ra
- Tính phí theo loại xe và thời gian gửi
- Tạo REST API sạch theo Clean Architecture
- Viết unit test cho service layer

## 2. Kiến thức cần có

- CRUD design
- Repository pattern
- Service layer
- Business rules cho parking fee
- Transaction handling
- API response design
- Unit testing với fake repository

## 3. Kiến trúc của phase

Phase này sử dụng các lớp sau:

- `schemas`: request/response model
- `repositories`: đọc/ghi database
- `services`: business logic
- `api`: router và controller
- `core`: dependency injection và exception handling

## 4. Luồng xử lý

### Check-in

1. Nhận plate raw từ OCR hoặc camera
2. Chuẩn hóa biển số
3. Tìm vehicle trong database hoặc tạo mới
4. Kiểm tra session đang active
5. Lấy parking fee phù hợp
6. Tạo parking session active
7. Trả response cho dashboard/backend AI

### Check-out

1. Nhận plate raw
2. Chuẩn hóa biển số
3. Tìm session active
4. Tính thời gian gửi và phí
5. Đóng session
6. Lưu lịch sử và trả kết quả

## 5. Các endpoint chính

- `POST /api/v1/vehicles`
- `GET /api/v1/vehicles`
- `PATCH /api/v1/vehicles/{vehicle_id}`
- `DELETE /api/v1/vehicles/{vehicle_id}`
- `POST /api/v1/parking-sessions/check-in`
- `POST /api/v1/parking-sessions/check-out`
- `GET /api/v1/parking-sessions/active`
- `GET /api/v1/parking-sessions/history`
- `GET /api/v1/parking-fees`
- `POST /api/v1/parking-fees`
- `GET /api/v1/dashboard/summary`

## 6. Best practice

- Không để controller chứa business logic
- Không hardcode phí trong router
- Dùng service layer để tính phí và state transition
- Tách query đọc và command ghi khi cần mở rộng
- Luôn validate plate number trước khi tạo session
- Viết test cho service trước khi thêm UI

## 7. Các lỗi thường gặp

- Cho phép một xe có nhiều session active
- Tính phí ngay trong controller khiến khó test
- Không lưu ảnh hoặc metadata khi check-in/check-out
- Dùng OCR raw text trực tiếp mà không normalize
- Không có transaction cho thao tác tạo session

## 8. Cách debug

- Test service bằng fake repository trước
- Kiểm tra trạng thái active/closed của session
- Log plate raw và plate normalized
- So sánh thời gian gửi với fee rule
- Kiểm tra dữ liệu dashboard bằng một session mẫu

## 9. Checklist hoàn thành

- [ ] Có schema request/response
- [ ] Có repository layer
- [ ] Có service layer
- [ ] Có router vehicles/sessions/fees/dashboard
- [ ] Có fee calculation logic
- [ ] Có unit test cho service
- [ ] API trả response ổn định

## 10. Kết quả đầu ra của phase

Sau phase này, backend phải xử lý được nghiệp vụ gửi xe cơ bản end-to-end từ AI ingest đến lưu session và tính phí.
