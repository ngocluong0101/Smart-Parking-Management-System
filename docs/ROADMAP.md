# Roadmap

Tài liệu này mô tả lộ trình xây dựng hệ thống từ đầu đến cuối theo hướng phù hợp portfolio và có thể mở rộng thành dự án thực tế.

## Phase 1: Phân tích yêu cầu

Mục tiêu:

- Chốt bài toán nghiệp vụ
- Xác định actor, use case, input/output
- Xác định phạm vi MVP và phạm vi mở rộng
- Chọn stack và nguyên tắc kỹ thuật

Kiến thức cần có:

- Phân tích yêu cầu phần mềm
- UML cơ bản
- Thiết kế hệ thống ở mức high-level
- Domain parking management

Deliverables:

- SRS
- Use case diagram
- Activity diagram
- Sequence diagram
- Danh sách requirement phi chức năng

## Phase 2: Thiết kế kiến trúc

Mục tiêu:

- Chốt kiến trúc tổng thể backend, AI, frontend, database, deployment
- Xác định luồng dữ liệu end-to-end
- Định nghĩa boundary giữa các module

Kiến thức cần có:

- Clean Architecture
- Layered architecture
- REST design
- Event flow và state management
- Separation of concerns

Deliverables:

- [Architecture overview](architecture/overview.md)
- [Class diagram](diagrams/class.md)
- [Deployment diagram](diagrams/deployment.md)
- [Folder structure](architecture/folder-structure.md)
- [Phase 2 guide](phase-2.md)

## Phase 3: Thiết kế database

Mục tiêu:

- Thiết kế schema chuẩn hóa
- Tối ưu truy vấn cho dashboard và lịch sử
- Đảm bảo toàn vẹn dữ liệu

Kiến thức cần có:

- ER modeling
- Normalization
- Index design
- Transaction và auditing

Deliverables:

- [Database design](architecture/database.md)
- [ER diagram](diagrams/er-diagram.md)
- [Phase 3 guide](phase-3.md)
- SQL schema
- Migration strategy

## Phase 4: Khởi tạo backend

Mục tiêu:

- Dựng FastAPI project theo Clean Architecture
- Tạo auth, middleware, logging, validation, exception handling
- Dựng repository/service/controller pattern

Kiến thức cần có:

- FastAPI
- Pydantic
- SQLAlchemy
- JWT auth
- API versioning

Deliverables:

- [Phase 4 guide](phase-4.md)
- [Backend skeleton](../backend)
- Core modules
- Auth flow
- Health check API

## Phase 5: Tự huấn luyện YOLO

Mục tiêu:

- Tìm dataset
- Annotate dữ liệu
- Train detector biển số
- Đánh giá mAP, precision, recall, F1

Kiến thức cần có:

- Object detection
- Labeling format
- Data augmentation
- Training loop
- Evaluation metrics

Deliverables:

- Dataset strategy
- Training scripts
- Best weights
- Evaluation report

## Phase 6: Tích hợp OCR

Mục tiêu:

- Crop biển số từ detector
- OCR bằng PaddleOCR
- Chuẩn hóa chuỗi biển số bằng regex
- Tối ưu post-processing

Kiến thức cần có:

- OCR pipeline
- Image preprocessing
- Text normalization
- Rule-based validation

Deliverables:

- OCR module
- Plate normalization utility
- Inference pipeline

## Phase 7: Xây dựng API nghiệp vụ

Mục tiêu:

- Quản lý vehicle, parking session, fee, history
- Xử lý camera vào/ra
- Tính phí theo loại xe và thời gian

Kiến thức cần có:

- CRUD design
- Business rules
- Transaction handling
- Audit logging

Deliverables:

- REST API hoàn chỉnh
- Swagger/OpenAPI
- Unit tests cho service layer

## Phase 8: Xây dựng frontend

Mục tiêu:

- Dashboard quản trị
- Camera live view
- Vehicle management
- Parking history
- Statistics
- Dark mode

Kiến thức cần có:

- React + TypeScript
- State management
- Component design
- Responsive UI
- Charts

Deliverables:

- Frontend app
- Auth pages
- Dashboard pages
- API integration

## Phase 9: Docker và môi trường triển khai

Mục tiêu:

- Containerize backend, frontend, database
- Dùng Docker Compose cho local/dev
- Chuẩn bị Nginx reverse proxy

Kiến thức cần có:

- Dockerfile
- Compose orchestration
- Networking giữa service
- Environment variables

Deliverables:

- Dockerfile
- docker-compose.yml
- Nginx config

## Phase 10: Kiểm thử

Mục tiêu:

- Test unit, integration, API, UI
- Kiểm tra edge cases và lỗi nghiệp vụ

Kiến thức cần có:

- Pytest
- Test strategy
- Mocking
- Contract testing

Deliverables:

- Test suite
- Test report
- Bug list

## Phase 11: Deploy

Mục tiêu:

- Deploy trên Ubuntu/Linux server
- Cấu hình service, logs, restart policy
- Kiểm tra production readiness

Kiến thức cần có:

- Linux service management
- Nginx
- Reverse proxy
- Environment secrets

Deliverables:

- Deployment guide
- Production checklist

## Phase 12: Hoàn thiện tài liệu và portfolio

Mục tiêu:

- Hoàn thiện README
- Viết tài liệu kỹ thuật và demo guide
- Chuẩn bị nội dung CV, GitHub, interview talking points

Deliverables:

- README hoàn chỉnh
- API docs
- Architecture docs
- Demo script
- Interview notes
