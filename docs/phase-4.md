# Phase 4: Khởi Tạo Backend

Phase 4 là lúc chuyển kiến trúc thành code thật. Mục tiêu không phải viết hết business logic ngay, mà là dựng được một backend skeleton sạch, có thể mở rộng, có thể test, và đủ chuẩn để gắn AI pipeline sau này.

## 1. Mục tiêu của phase

- Khởi tạo FastAPI project theo Clean Architecture
- Tạo cấu trúc controllers, services, repositories, models, schemas, DTO
- Thiết lập config, logging, middleware, exception handling
- Dựng health check API và versioned router
- Chuẩn bị nền tảng để tích hợp auth, database và AI service

## 2. Kiến thức cần có

- FastAPI
- Pydantic settings
- SQLAlchemy cơ bản
- JWT authentication concept
- API versioning
- Dependency injection
- Logging và error handling

## 3. Kiến trúc backend đề xuất

Backend nên được chia thành các lớp sau:

- api: định nghĩa router và controller layer
- core: config, logging, security, exception, constants
- domain: entity và business interface
- application hoặc services: use case và business logic
- infrastructure: database, repository, external adapters
- schemas: request/response model

### Nguyên tắc

- Controller không chứa logic nghiệp vụ
- Service không truy cập database trực tiếp
- Repository không biết về HTTP
- Schema chỉ dùng cho validate và serialize
- Business rule phải nằm ở một nơi duy nhất

## 4. Luồng hoạt động backend

1. Client gọi API
2. Router chuyển request vào controller
3. Controller validate input bằng schema
4. Service xử lý logic nghiệp vụ
5. Repository đọc hoặc ghi database
6. Response được chuẩn hóa qua schema
7. Exception được xử lý tập trung qua handler

## 5. Các file cần tạo ở phase này

- backend/requirements.txt
- backend/app/main.py
- backend/app/api/v1/router.py
- backend/app/api/v1/health.py
- backend/app/core/config.py
- backend/app/core/logging.py
- backend/app/core/exceptions.py
- backend/app/schemas/common.py
- backend/app/infrastructure/db/session.py
- backend/app/infrastructure/db/base.py

## 6. Best practice

- Dùng environment variables cho mọi config quan trọng
- Khởi tạo logging từ đầu để dễ trace lỗi
- Tách router theo version: /api/v1
- Trả response theo format thống nhất
- Dùng dependency injection cho service và repository
- Không hardcode secret key, DB URL, hoặc đường dẫn file
- Định nghĩa health check sớm để kiểm tra deployment

## 7. Các lỗi thường gặp

- Để logic nghiệp vụ trong router
- Không có structure nên sau vài feature là code rối
- Không tách config nên chạy local và production bị lệch
- Không có exception handler nên response lỗi không đồng nhất
- Không chuẩn hóa dependencies nên service khó test

## 8. Cách debug

- Kiểm tra health endpoint đầu tiên sau khi khởi tạo app
- Bật log level rõ ràng trong local
- Test từng layer một: schema, service, repository, router
- Khi lỗi API, xác định lỗi ở validation, service hay DB
- Dùng request id hoặc correlation id khi debug luồng camera vào/ra sau này

## 9. Checklist hoàn thành

- [ ] Dựng cấu trúc thư mục backend
- [ ] Tạo app FastAPI chạy được
- [ ] Tạo router v1
- [ ] Có health endpoint
- [ ] Có config và logging cơ bản
- [ ] Có exception handler chuẩn hóa
- [ ] Có skeleton cho DB session
- [ ] Cập nhật README và roadmap

## 10. Kết quả đầu ra của phase

Sau phase này, backend phải ở trạng thái scaffold sạch, sẵn sàng nhận model, service và database layer mà không cần tái cấu trúc lớn.
