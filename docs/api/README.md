# API Documentation

## Mục tiêu

Tài liệu này mô tả các endpoint chính của hệ thống.

## Nhóm endpoint dự kiến

### Auth

- POST /auth/login
- POST /auth/refresh
- POST /auth/logout

### Vehicles

- GET /vehicles
- POST /vehicles
- PATCH /vehicles/{id}
- DELETE /vehicles/{id}
- GET /vehicles/search

### Parking Sessions

- GET /parking-sessions
- GET /parking-sessions/active
- GET /parking-sessions/history
- POST /parking-sessions/check-in
- POST /parking-sessions/check-out

### Dashboard

- GET /dashboard/summary
- GET /dashboard/statistics

### Users and Roles

- GET /users
- POST /users
- GET /roles
- POST /roles

### Settings

- GET /settings/fees
- PATCH /settings/fees

## Chuẩn response

- success: true/false
- message: mô tả ngắn
- data: payload chính
- errors: chi tiết validate khi có lỗi

## Quy tắc thiết kế

- API versioning qua /api/v1
- Chuẩn hóa lỗi bằng exception handler
- Tất cả endpoint cần auth trừ login và refresh
