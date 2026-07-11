# Phase 6: Tích hợp OCR và Chuẩn hóa biển số

Phase 6 tập trung vào việc kết nối detector (Phase 5) với OCR (PaddleOCR) và chuẩn hóa biển số để backend xử lý nghiệp vụ.

## 1. Mục tiêu của phase

- Crop biển số từ detector
- OCR bằng PaddleOCR
- Chuẩn hóa chữ bằng regex và rule-based
- Tạo endpoint AI ingest để backend nhận dữ liệu từ inference service
- Kiểm tra end-to-end từ detect -> crop -> ocr -> normalize -> backend

## 2. Kiến thức cần có

- Image cropping and coordinate systems
- PaddleOCR inference usage
- Text normalization and regex
- Base64 image transfer over API
- Error handling and fallback for missing OCR dependency

## 3. Luồng chi tiết

1. Detector phát hiện bounding box
2. Crop vùng biển số và gửi image tới OCR
3. OCR trả về văn bản và confidence
4. Chuẩn hóa văn bản
5. Gọi endpoint backend `/api/v1/ai/ingest` để xử lý nghiệp vụ

## 4. Tài liệu và mã mẫu

- `ai/inference/ocr.py`: wrapper cho PaddleOCR với fallback mock
- `ai/inference/crop.py`: hàm crop theo bounding box
- `ai/utils/plate_utils.py`: chuẩn hóa plate và regex
- `backend/app/api/v1/ai.py`: endpoint `POST /api/v1/ai/ingest`

## 5. Checklist

- [ ] Implement crop util
- [ ] Implement OCR wrapper with PaddleOCR fallback
- [ ] Implement plate normalization utils and tests
- [ ] Implement backend ingest endpoint
- [ ] Test end-to-end with a sample image
