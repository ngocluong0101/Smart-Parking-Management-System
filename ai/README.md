# AI

Thư mục này sẽ chứa toàn bộ logic AI của dự án, hiện tại tập trung vào detector biển số trong Phase 5 và sẽ mở rộng sang OCR pipeline ở Phase 6.

## Mục tiêu

- Huấn luyện YOLO để detect biển số
- Chạy inference trên ảnh, video và webcam
- Chuẩn bị crop biển số cho OCR
- Tách AI inference khỏi business logic backend

## Cấu trúc đề xuất

```text
ai/
├── inference/
├── models/
├── utils/
└── README.md
```

## Quy ước

- Detector model và weights phải có version rõ ràng
- Script inference chỉ xử lý AI, không chứa business rule của backend
- Kết quả trả về cần đủ metadata để backend dùng tiếp
