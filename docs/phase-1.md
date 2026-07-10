# Phase 1: Phân Tích Yêu Cầu

Đây là phase quan trọng nhất vì nó quyết định toàn bộ hướng triển khai về sau. Nếu phase này làm tốt, các phase sau sẽ ít đổi kiến trúc, ít nợ kỹ thuật và dễ demo như một dự án doanh nghiệp.

## 1. Mục tiêu của phase

- Chốt bài toán nghiệp vụ của bãi đỗ xe thông minh
- Xác định actor, luồng nghiệp vụ, use case và biên hệ thống
- Định nghĩa rõ phạm vi MVP và phạm vi mở rộng
- Xác định tiêu chí thành công cho từng module: AI, backend, frontend, database
- Chọn stack phù hợp với yêu cầu portfolio và phỏng vấn

## 2. Kiến thức cần có

- Phân tích yêu cầu phần mềm
- UML cơ bản
- Kiến trúc hệ thống high-level
- Domain knowledge về parking management
- Tư duy tách business logic và AI inference

## 3. Kiến trúc ở mức phase 1

Ở phase này chưa viết code sản phẩm chính, nhưng phải chốt kiến trúc logic:

- Camera hoặc video stream đưa frame vào AI service
- YOLO detect biển số
- Crop biển số
- PaddleOCR đọc nội dung
- Regex chuẩn hóa biển số
- FastAPI xử lý nghiệp vụ và giao tiếp database
- React hiển thị dashboard và trang quản trị
- MySQL lưu session, vehicle, fee, user, audit

### Lý do chọn PaddleOCR

Có hai hướng OCR thường gặp:

- Tự huấn luyện OCR từ đầu
- Dùng PaddleOCR và tập trung tối ưu phần detect, crop, normalize, rule business

Chọn PaddleOCR là phương án tốt hơn cho dự án portfolio vì:

- Tự huấn luyện OCR cần dữ liệu lớn và pipeline phức tạp hơn nhiều
- OCR từ đầu tiêu tốn thời gian nhưng không tăng nhiều giá trị trình diễn cho bài toán parking
- PaddleOCR đủ mạnh để tạo demo thực tế và ổn định hơn trong giai đoạn đầu
- Ta có thể tập trung vào phần có giá trị cao hơn: AI detection, tích hợp hệ thống, clean architecture, dashboard và deploy

## 4. Luồng hoạt động

### Camera vào

1. Camera phát hiện xe đi vào
2. Frame được gửi sang detector
3. YOLO phát hiện biển số
4. Crop vùng biển số
5. PaddleOCR đọc ký tự
6. Regex chuẩn hóa biển số
7. Kiểm tra database
8. Nếu chưa có thì tạo parking session mới, lưu ảnh và thời gian vào
9. Nếu đã có thì hiển thị cảnh báo trùng

### Camera ra

1. Camera phát hiện xe đi ra
2. OCR biển số
3. Tra cứu session đang mở
4. Nếu tồn tại thì tính thời gian gửi và phí
5. Lưu lịch sử ra xe
6. Cập nhật trạng thái session
7. Nếu không tồn tại thì ghi nhận lỗi nghiệp vụ

## 5. Best practice

- Chốt một chuẩn biển số thống nhất trước khi code regex
- Xác định rõ trạng thái session: active, closed, duplicate, invalid
- Thiết kế database theo hướng phục vụ query dashboard trước khi implement UI
- Tách AI inference khỏi business logic
- Ưu tiên log đầy đủ từ đầu để debug dễ hơn
- Thiết kế API version ngay từ đầu, ví dụ /api/v1
- Dùng DTO và schema rõ ràng để tránh schema trộn lẫn với model database

## 6. Các lỗi thường gặp

- Chưa chốt requirement nhưng đã bắt đầu code nên phải refactor lại liên tục
- Dùng OCR trước khi ổn định crop region, dẫn đến kết quả rất nhiễu
- Trộn business rule tính phí trực tiếp vào controller
- Thiết kế database thiếu index cho plate_number và check_in_time
- Không phân biệt session đang mở và lịch sử hoàn tất
- Không chuẩn hóa biển số trước khi lưu nên dữ liệu bị loạn format

## 7. Cách debug

- Kiểm tra từng bước của pipeline thay vì debug cả luồng cùng lúc
- Lưu ảnh trung gian: frame gốc, ảnh crop biển số, ảnh OCR input
- So sánh plate raw và plate after regex normalization
- Ghi log request id hoặc session id để lần theo một xe cụ thể
- Test riêng từng case: xe vào hợp lệ, xe vào trùng, xe ra hợp lệ, xe ra không tồn tại
- Khi OCR sai, kiểm tra trước phần detect và crop thay vì đổ lỗi cho OCR ngay

## 8. Checklist hoàn thành

- [ ] Chốt phạm vi MVP
- [ ] Xác định actor và use case
- [ ] Viết SRS
- [ ] Vẽ use case, activity, sequence, class, deployment diagram
- [ ] Chốt luồng camera vào/ra
- [ ] Chốt rule tính phí
- [ ] Chốt chuẩn dữ liệu biển số
- [ ] Chốt stack kỹ thuật

## 9. Kết quả đầu ra của phase

Sau phase này, chúng ta phải có đủ tài liệu để bước sang thiết kế kiến trúc và database mà không phải đoán lại yêu cầu.
