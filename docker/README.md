# Docker

## Mục đích

Thư mục này chứa toàn bộ cấu hình Docker cho Smart Parking Management System.

## File chính

- `docker-compose.yml`: dựng backend, frontend, MySQL
- `.env.example`: biến môi trường mẫu

## Chạy local

```bash
cp docker/.env.example docker/.env
cd docker
docker compose up --build
```

## Services

- Frontend: http://localhost
- Backend: http://localhost:8000
- MySQL: localhost:3306
