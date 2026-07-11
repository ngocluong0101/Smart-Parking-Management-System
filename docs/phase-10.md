# Phase 10: Kiểm Thử

Phase 10 đảm bảo hệ thống đã dựng không chỉ chạy được mà còn có hành vi ổn định. Đây là phase giúp dự án trông chuyên nghiệp hơn vì thể hiện tư duy quality engineering, không chỉ dừng ở việc code xong là đủ.

## 1. Mục tiêu của phase

- Kiểm tra unit, integration, API và smoke test
- Xác nhận backend service logic hoạt động đúng
- Xác nhận frontend build và cấu trúc route không lỗi
- Kiểm tra compose/deploy config ở mức cấu hình
- Ghi nhận các bug và edge case để chuẩn bị deploy

## 2. Kiến thức cần có

- Pytest
- Test pyramid
- Mocking và fake repository
- Smoke test cho frontend build
- Config validation
- Contract testing mindset

## 3. Chiến lược test

- Unit test: test logic nhỏ như plate normalization, fee calculation, service rules
- Service test: test check-in/check-out bằng fake repository
- Build test: test frontend production build
- Config test: validate Docker Compose config
- Integration test: khi có DB thật hoặc container thật

## 4. Phạm vi test hiện tại

- `tests/test_plate_utils.py`
- `tests/test_parking_service.py`
- `frontend npm run build`
- `docker compose config`

## 5. Best practice

- Test phải nhanh và deterministic
- Tách test logic khỏi DB thật khi có thể
- Đặt tên test rõ ràng theo hành vi
- Dùng fake repository cho business logic
- Luôn có smoke test cho frontend build

## 6. Các lỗi thường gặp

- Test phụ thuộc môi trường bên ngoài nên flaky
- Không có fixture riêng cho service
- Chỉ test happy path mà bỏ qua edge cases
- Không kiểm tra build frontend sau khi sửa route hoặc types
- Không kiểm tra compose config trước khi deploy

## 7. Cách debug

- Chạy từng test file riêng khi fail
- In ra input/output của service logic
- Kiểm tra build logs khi frontend lỗi TypeScript
- So sánh compose config render với file gốc
- Dùng `pytest -q` để nhận phản hồi ngắn gọn

## 8. Checklist hoàn thành

- [ ] Có unit test cho plate utils
- [ ] Có service test cho check-in/check-out
- [ ] Có frontend build smoke test
- [ ] Có compose config validation
- [ ] Có tài liệu test strategy
- [ ] Có danh sách lỗi còn lại

## 9. Kết quả đầu ra của phase

Sau phase này, dự án phải có một nền test tối thiểu đủ để chuyển sang Phase 11 deploy mà không bị mù lỗi cấu hình hoặc logic cơ bản.
