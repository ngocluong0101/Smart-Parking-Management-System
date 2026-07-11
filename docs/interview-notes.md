# Interview Notes

## 1. One-liner

Smart Parking Management System là hệ thống quản lý bãi đỗ xe thông minh dùng YOLO để detect biển số, PaddleOCR để đọc text và FastAPI + React để xử lý nghiệp vụ gửi xe.

## 2. Vấn đề giải quyết

- Tự động hóa nhận diện xe vào/ra
- Giảm thao tác thủ công khi quản lý bãi xe
- Lưu lịch sử gửi xe và tính phí rõ ràng
- Tạo dashboard cho operator và admin

## 3. Kiến trúc chính

- AI inference tách riêng khỏi backend business logic
- Backend dùng Clean Architecture
- Database chuẩn hóa theo Vehicle, ParkingSession, ParkingLot, ParkingFee, User, Role, AuditLog
- Frontend React + TypeScript cho dashboard quản trị
- Docker Compose và Nginx cho deploy local/production-like

## 4. Điều cần nói về AI

- Phần detection biển số tự huấn luyện để phù hợp domain thực tế
- OCR dùng PaddleOCR thay vì tự train từ đầu vì OCR là bài toán lớn, tốn dữ liệu và không phải trọng tâm của portfolio này
- Pipeline: camera -> YOLO -> crop -> OCR -> normalize -> backend

## 5. Điều cần nói về backend

- Controller chỉ nhận request/response
- Service chứa business logic
- Repository xử lý truy vấn database
- Exception và validation được tách riêng
- Có JWT, logging và health endpoint

## 6. Điều cần nói về testing

- Có unit test cho plate normalization
- Có service test với fake repository
- Có frontend build smoke test
- Có Docker Compose config validation

## 7. Điều cần nói về deployment

- Có Dockerfile cho backend và frontend
- Có compose cho local/dev
- Có Nginx reverse proxy và deploy docs cho Ubuntu
- Có script backup database

## 8. Limitations

- Detection model và OCR pipeline vẫn cần benchmark trên dữ liệu thực tế
- Realtime stream ở mức demo, chưa phải production-grade video processing system
- Multi-camera orchestration là hướng mở rộng tiếp theo

## 9. Future work

- Multi-camera support
- Streaming realtime tối ưu hơn
- Tích hợp payment và invoice
- Dashboard analytics nâng cao
- Role/permission matrix chi tiết hơn
