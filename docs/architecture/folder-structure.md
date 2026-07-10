# Folder Structure

Tài liệu này mô tả cấu trúc thư mục đề xuất cho repository. Mục tiêu là giữ code rõ ràng theo domain và dễ mở rộng khi dự án lớn dần.

## Nguyên tắc

- Tách rõ backend, frontend, AI, database, training và docs
- Không để logic nghiệp vụ lẫn vào file khởi động ứng dụng
- Không đặt file xử lý trực tiếp trong root nếu có thể tách sang module con
- Ưu tiên cấu trúc theo domain thay vì theo kiểu nhồi mọi thứ vào một thư mục chung

## Cấu trúc đề xuất

```text
Smart-Parking-Management-System/
├── ai/
│   ├── inference/
│   ├── models/
│   ├── utils/
│   └── README.md
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── domain/
│   │   ├── infrastructure/
│   │   ├── schemas/
│   │   └── main.py
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── features/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── styles/
│   │   └── types/
│   └── public/
├── dataset/
├── training/
├── weights/
├── database/
│   ├── schema/
│   └── migrations/
├── docker/
├── scripts/
├── tests/
└── docs/
```

## Giải thích từng thư mục

### ai/

Chứa toàn bộ mã xử lý inference và helper cho YOLO, OCR, crop, normalize.

### backend/

Chứa FastAPI application theo Clean Architecture.

### frontend/

Chứa React + TypeScript app cho dashboard quản trị.

### dataset/

Chứa dữ liệu gốc, cấu hình chia train/val/test, và annotation.

### training/

Chứa scripts train, evaluate, export, resume training.

### weights/

Chứa model weights đã train.

### database/

Chứa schema SQL, migration và tài liệu DB.

### docker/

Chứa Dockerfile, compose, nginx config.

### scripts/

Chứa script tiện ích như seed data, cleanup, export, benchmark.

### tests/

Chứa test độc lập hoặc test tích hợp cross-module.

### docs/

Chứa toàn bộ tài liệu phân tích, kiến trúc, API, diagram và roadmap.

## Best practice

- Duy trì naming nhất quán giữa folder và module
- Khi một thư mục có quá nhiều file, tiếp tục chia nhỏ theo feature
- Tài liệu phải phản ánh đúng folder thực tế
- Trước khi tạo file mới, xác định nó thuộc layer nào và domain nào
