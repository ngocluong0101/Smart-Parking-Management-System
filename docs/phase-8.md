# Phase 8: Xây Dựng Frontend

Phase 8 chuyển backend API thành một website quản trị thực dụng. Frontend không chỉ hiển thị dữ liệu, mà còn phải thể hiện rõ luồng vận hành bãi xe, dashboard realtime, lịch sử, cấu hình, và khả năng mở rộng cho sản phẩm thật.

## 1. Mục tiêu của phase

- Dựng React + TypeScript app theo cấu trúc feature-based
- Thiết kế dashboard quản trị cho xe đang gửi, lịch sử, doanh thu, thống kê
- Xây dựng các màn hình: Login, Dashboard, Camera Live, Vehicle, Parking History, Statistics, Settings, User Management
- Tích hợp API layer để gọi backend cleanly
- Thêm dark mode và responsive layout

## 2. Kiến thức cần có

- React + TypeScript
- Component composition
- State và context
- API service layer
- Responsive design
- Dark mode theming
- Data presentation cho dashboard

## 3. Kiến trúc frontend

Frontend nên chia thành các lớp sau:

- `pages`: màn hình chính
- `components`: thành phần dùng lại
- `layouts`: layout shell và sidebar
- `features`: module theo domain
- `services`: API client
- `hooks`: logic dùng chung
- `types`: kiểu dữ liệu TypeScript
- `styles`: theme, tokens, global CSS

### Nguyên tắc

- Mỗi màn hình là một route riêng
- Component không gọi fetch trực tiếp nếu có service layer
- Tách UI và data logic rõ ràng
- Dùng CSS variables để hỗ trợ dark mode và theme thay đổi
- Giữ thiết kế đủ đẹp để đưa vào portfolio

## 4. Luồng hoạt động UI

1. User mở app và đăng nhập
2. Dashboard hiển thị số xe đang gửi, doanh thu hôm nay, số lượt xe
3. Trang Camera Live hiển thị trạng thái ingest từ AI service
4. Trang Vehicle cho phép CRUD và tìm kiếm theo biển số
5. Trang History hiển thị session vào/ra, thời gian và phí
6. Trang Statistics hiển thị biểu đồ tổng hợp
7. Trang Settings và User Management quản trị hệ thống

## 5. Folder structure đề xuất

```text
frontend/
├── public/
├── src/
│   ├── app/
│   ├── components/
│   ├── features/
│   ├── hooks/
│   ├── layouts/
│   ├── pages/
│   ├── services/
│   ├── styles/
│   ├── types/
│   ├── utils/
│   ├── App.tsx
│   └── main.tsx
├── index.html
├── package.json
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```

## 6. Pages cần có

- Login
- Dashboard
- Camera Live
- Vehicle
- Parking History
- Statistics
- Settings
- User Management

## 7. Best practice

- Dùng TypeScript strict để giảm lỗi runtime
- Định nghĩa types rõ cho API response
- Không hardcode backend URL trong component
- Tách dashboard cards, tables, charts thành component tái sử dụng
- Thiết kế dark mode bằng token system
- Responsive từ đầu, không chỉ tối ưu desktop

## 8. Các lỗi thường gặp

- Dồn toàn bộ API call vào một component
- Không thống nhất kiểu dữ liệu giữa backend và frontend
- Chỉ làm đẹp dashboard mà quên luồng nghiệp vụ
- Không có empty/loading/error state
- Dark mode chỉ đổi màu nền mà không có hệ thống token

## 9. Cách debug

- Kiểm tra từng page độc lập trước khi nối router
- Mock API response khi backend chưa hoàn thiện
- Test responsive bằng các breakpoint khác nhau
- Kiểm tra component tree khi state thay đổi
- Bật log API service nếu response không đúng schema

## 10. Checklist hoàn thành

- [ ] Khởi tạo React + TypeScript app
- [ ] Có layout và navigation
- [ ] Có dashboard cards và tables
- [ ] Có dark mode
- [ ] Có API service layer
- [ ] Có các page chính
- [ ] Có README frontend
- [ ] Cập nhật root docs

## 11. Kết quả đầu ra của phase

Sau phase này, hệ thống phải có một frontend dashboard đủ đẹp, đủ rõ chức năng và đủ sạch về kiến trúc để nối vào backend thật.
