# Git Flow

## Branch model

- main: chỉ chứa code ổn định, sẵn sàng release
- develop: nhánh tích hợp tính năng
- feature/\*: phát triển từng chức năng
- hotfix/\*: sửa lỗi gấp trên production
- release/\*: chuẩn bị phát hành

## Quy tắc commit

Dùng Conventional Commits:

- feat: thêm tính năng
- fix: sửa lỗi
- docs: cập nhật tài liệu
- refactor: tái cấu trúc code
- test: thêm hoặc sửa test
- chore: tác vụ bảo trì

## Quy tắc làm việc

- Mỗi feature một branch riêng
- Commit nhỏ, rõ nghĩa
- Không merge trực tiếp vào main
- Luôn review diff trước khi merge

## Gợi ý cho portfolio

- Giữ lịch sử commit sạch và có ý đồ
- Mỗi phase nên kết thúc bằng một milestone tag
- README và docs phải cập nhật cùng code
