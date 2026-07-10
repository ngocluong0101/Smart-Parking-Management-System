# Dataset

Thư mục này chứa dữ liệu cho Phase 5. Dataset phải được quản lý chặt để tránh nhầm lẫn giữa ảnh raw, ảnh đã annotate và ảnh đã split.

## Cấu trúc đề xuất

```text
dataset/
├── license_plate/
│   ├── images/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   ├── labels/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   └── README.md
└── raw/
```

## Quy trình dữ liệu

1. Thu thập ảnh raw
2. Làm sạch ảnh lỗi
3. Annotate bounding box biển số
4. Split train/val/test
5. Kiểm tra nhãn bằng visualize script
6. Dùng dataset YAML để train YOLO

## Lưu ý

- Không trộn raw và processed data trong cùng folder
- Dataset phải có version rõ ràng
- Test set phải được giữ nguyên trong quá trình tuning
