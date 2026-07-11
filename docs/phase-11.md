# Phase 11: Deploy Trên Ubuntu

Phase 11 đưa hệ thống từ môi trường Docker local sang một cấu trúc deploy thực tế trên Ubuntu/Linux server. Mục tiêu là tái hiện cách một sản phẩm doanh nghiệp được đóng gói, chạy dịch vụ, reverse proxy và giám sát cơ bản.

## 1. Mục tiêu của phase

- Deploy backend, frontend và database trên Ubuntu
- Chạy service với restart policy và auto-start
- Cấu hình Nginx reverse proxy
- Quản lý biến môi trường cho production
- Chuẩn bị checklist production readiness

## 2. Kiến thức cần có

- Linux service management
- systemd
- Nginx reverse proxy
- Docker Compose trên server
- Environment secrets
- Log và basic monitoring

## 3. Kiến trúc deploy

- `backend`: FastAPI chạy qua Docker hoặc systemd tùy môi trường
- `frontend`: Nginx serve static build
- `db`: MySQL container hoặc managed DB
- `nginx`: reverse proxy internet-facing

## 4. Luồng deploy

1. Pull code từ GitHub
2. Copy `.env` production
3. Build images bằng Docker Compose
4. Start stack bằng `docker compose up -d`
5. Kiểm tra health endpoint và website
6. Theo dõi logs và restart policy

## 5. Deliverables

- `deploy/README.md`
- `deploy/systemd/smart-parking.service`
- `deploy/nginx/smart-parking.conf`
- `deploy/production.env.example`
- `deploy/scripts/deploy.sh`
- `deploy/scripts/backup-db.sh`

## 6. Best practice

- Không commit secret production
- Tách env dev và env prod
- Dùng Nginx để terminate HTTP traffic
- Có backup database định kỳ
- Có health check và log strategy
- Dùng non-root user khi có thể

## 7. Các lỗi thường gặp

- Quên set quyền file env hoặc script
- Nginx route sai upstream backend
- Docker Compose dùng biến môi trường không có giá trị
- MySQL start chậm làm backend fail nếu không có healthcheck
- Deploy xong nhưng quên mở port hoặc firewall

## 8. Cách debug

- Kiểm tra `systemctl status`
- Xem logs Nginx và Docker Compose
- Kiểm tra `curl /api/v1/health`
- Xác minh biến môi trường đã load đúng
- Dùng `docker compose ps` để xem trạng thái service

## 9. Checklist hoàn thành

- [ ] Có deploy README
- [ ] Có systemd unit file nếu cần
- [ ] Có Nginx config
- [ ] Có env production mẫu
- [ ] Có script deploy
- [ ] Có script backup DB
- [ ] Có checklist production

## 10. Kết quả đầu ra của phase

Sau phase này, dự án phải có hướng dẫn deploy rõ ràng trên Ubuntu và đủ cấu hình để một reviewer có thể hiểu ngay cách chạy production-like stack.
