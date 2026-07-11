# Demo Script

Mục tiêu của demo là cho người xem hiểu nhanh dự án, thấy được luồng nghiệp vụ và tin rằng hệ thống có thể chạy thực tế.

## 1. Mở đầu

"Đây là Smart Parking Management System, một hệ thống quản lý bãi đỗ xe thông minh sử dụng Computer Vision để phát hiện biển số, OCR để đọc biển số và FastAPI + React để quản lý nghiệp vụ gửi xe."

## 2. Flow demo

1. Mở dashboard
2. Chỉ vào số liệu tổng quan: xe đang gửi, số lượt xe, doanh thu hôm nay
3. Mở trang Camera Live
4. Giải thích pipeline: camera -> YOLO -> crop biển số -> PaddleOCR -> normalize -> backend
5. Vào trang Vehicle để tìm kiếm theo biển số
6. Vào Parking History để xem vào/ra, thời gian, phí
7. Mở Statistics để nói về biểu đồ và báo cáo
8. Mở Settings/User Management để nhấn vào khả năng quản trị

## 3. Điểm cần nhấn mạnh

- Object detection được tự huấn luyện
- OCR dùng PaddleOCR để giảm thời gian phát triển và tăng độ ổn định
- Backend theo Clean Architecture
- Có MySQL, JWT, Docker, Nginx
- Có test, deployment guide và roadmap rõ ràng

## 4. Những câu hỏi nên chuẩn bị

- Tại sao chọn YOLO?
- Tại sao không tự train OCR từ đầu?
- Làm sao xử lý xe vào trùng biển số?
- Tính phí theo rule nào?
- Nếu camera mờ hoặc biển số khó đọc thì sao?
- Hệ thống mở rộng sang nhiều bãi xe thế nào?

## 5. Kết thúc demo

"Dự án này thể hiện đầy đủ các phần của một hệ thống Computer Vision thực tế: AI, backend, database, frontend, testing và deployment. Trong tương lai có thể mở rộng thêm multi-camera, realtime stream ổn định hơn và tích hợp payment."
