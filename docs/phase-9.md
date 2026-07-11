# Phase 9: Docker Và Môi Trường Triển Khai

Phase 9 đóng gói toàn bộ hệ thống thành môi trường có thể chạy đồng nhất trên máy local, Ubuntu server hoặc VPS. Đây là bước rất quan trọng để dự án trông giống sản phẩm thật và dễ demo trên GitHub.

## 1. Mục tiêu của phase

- Containerize backend, frontend, database
- Dùng Docker Compose để dựng toàn bộ stack local/dev
- Chuẩn bị Nginx reverse proxy
- Tách config theo môi trường qua `.env`
- Đưa project tới trạng thái có thể khởi chạy bằng một lệnh compose

## 2. Kiến thức cần có

- Dockerfile
- Multi-stage build
- Docker Compose
- Networking giữa service
- Environment variables
- Nginx reverse proxy
- Volume và persistent storage

## 3. Kiến trúc deploy

- `backend`: FastAPI app
- `frontend`: React production build served by Nginx
- `db`: MySQL container cho production-like local setup
- `nginx`: reverse proxy cho frontend và backend

## 4. Luồng chạy

1. User vào Nginx
2. Nginx route sang frontend hoặc backend
3. Backend kết nối MySQL qua network nội bộ
4. Frontend gọi backend API qua reverse proxy
5. Toàn bộ stack có thể khởi động lại độc lập bằng Compose

## 5. Deliverables

- `backend/Dockerfile`
- `frontend/Dockerfile`
- `docker/docker-compose.yml`
- `docker/nginx.conf`
- `docker/.env.example`
- `docker/README.md`

## 6. Best practice

- Không đưa secret vào image
- Dùng multi-stage build để giảm size image
- Tách network app và network database nếu cần mở rộng
- Set restart policy cho service quan trọng
- Ghi rõ lệnh chạy local và production

## 7. Các lỗi thường gặp

- Quên expose port giữa container
- Frontend gọi nhầm API host local thay vì service name
- MySQL chưa sẵn sàng nhưng backend đã chạy
- Không có volume nên mất dữ liệu khi restart
- Không cấu hình đúng `VITE_API_BASE_URL`

## 8. Cách debug

- Xem logs từng container riêng
- Kiểm tra network bằng `docker compose exec`
- Kiểm tra biến môi trường trong container
- Test backend health endpoint sau khi compose up
- Xác nhận frontend build xong trước khi serve qua Nginx

## 9. Checklist hoàn thành

- [ ] Có Dockerfile cho backend
- [ ] Có Dockerfile cho frontend
- [ ] Có compose file chạy toàn stack
- [ ] Có Nginx config
- [ ] Có `.env.example`
- [ ] Có README docker
- [ ] Build và up được stack local

## 10. Kết quả đầu ra của phase

Sau phase này, dự án phải có thể chạy dưới Docker Compose với cấu trúc rõ ràng, đủ để chuyển sang Phase 10 kiểm thử và Phase 11 deploy.
