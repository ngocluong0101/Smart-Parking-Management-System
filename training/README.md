# Training

Thư mục này chứa toàn bộ tài nguyên cho Phase 5: tìm dataset, annotate, train YOLO, validate, evaluate, export và inference.

## Cấu trúc đề xuất

```text
training/
├── configs/
├── scripts/
├── notebooks/
├── outputs/
├── requirements.txt
└── README.md
```

## Quy trình

1. Thu thập và annotate dataset
2. Chia train/validation/test
3. Train model baseline
4. Đánh giá bằng mAP, precision, recall, F1
5. Fine-tune model tốt hơn
6. Export weights cho inference

## Dataset format

Dùng format YOLO:

- Ảnh nằm trong `images/`
- Nhãn nằm trong `labels/`
- Một file YAML mô tả class và đường dẫn dataset

## Các script sẽ có

- `train.py`: huấn luyện model
- `evaluate.py`: đánh giá model trên validation/test
- `infer.py`: chạy inference trên ảnh hoặc video
- `webcam_infer.py`: chạy demo webcam
- `visualize_labels.py`: kiểm tra annotation

## Mục tiêu kỹ thuật

- Reproducible training
- Rõ version dataset và weights
- Dễ benchmark
- Dễ chuyển sang Phase 6
