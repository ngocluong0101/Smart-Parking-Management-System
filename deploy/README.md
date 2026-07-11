# Deploy

Tài liệu và script trong thư mục này mô tả cách deploy Smart Parking Management System trên Ubuntu/Linux server.

## Nội dung

- `production.env.example`: biến môi trường production mẫu
- `systemd/smart-parking.service`: unit file để auto-start Docker Compose
- `nginx/smart-parking.conf`: reverse proxy config mẫu
- `scripts/deploy.sh`: script deploy nhanh
- `scripts/backup-db.sh`: script backup database

## Quy trình đề xuất

1. Copy `production.env.example` thành `.env`
2. Cập nhật secret và domain thật
3. Cài Docker, Docker Compose, Nginx
4. Chạy `scripts/deploy.sh`
5. Cấu hình Nginx và kiểm tra health endpoint

## Kiểm tra sau deploy

- Frontend phản hồi qua domain
- Backend `/api/v1/health` trả `200 OK`
- MySQL container đang healthy
- Logs không có lỗi kết nối database
