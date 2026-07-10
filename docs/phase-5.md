# Phase 5: Tự Huấn Luyện YOLO

Phase 5 là phần AI cốt lõi của dự án. Mục tiêu không phải chỉ chạy được model, mà phải thể hiện được toàn bộ quy trình chuẩn của một dự án Computer Vision thật: tìm dữ liệu, annotate, chia tập, augment, train, validate, evaluate và export model.

## 1. Mục tiêu của phase

- Tìm và chọn dataset phù hợp cho nhận diện biển số
- Thiết kế quy trình annotation chuẩn
- Chia train/validation/test đúng cách
- Thực hiện data augmentation phù hợp cho object detection
- Huấn luyện YOLO để detect biển số
- Đánh giá bằng mAP, precision, recall, F1 và confusion matrix
- Xuất model để dùng cho inference và webcam demo

## 2. Kiến thức cần có

- Object detection
- Bounding box annotation
- Dataset splitting
- Data augmentation
- Training loop và hyperparameter tuning
- Metrics cho detection
- Overfitting và underfitting
- Model export và inference

## 3. Vì sao phải tự huấn luyện object detection

Trong dự án này, phần phát hiện biển số phải tự huấn luyện vì:

- Nó là thành phần thể hiện năng lực CV thực chiến
- Dữ liệu bối cảnh bãi xe có thể khác dataset công khai
- Mô hình tự huấn luyện cho phép tối ưu theo camera thực tế
- Đây là phần giá trị cao để trình bày trong CV và phỏng vấn

Tuy nhiên OCR không cần huấn luyện từ đầu vì OCR là bài toán rộng, tốn dữ liệu và chi phí nhãn rất lớn. Vì vậy ta dùng PaddleOCR để tập trung sức lực vào phần detection + pipeline tích hợp.

## 4. Dataset strategy

### 4.1 Nguồn dữ liệu

Có thể tìm dataset từ:

- Kaggle
- Roboflow Universe
- GitHub public datasets
- OpenImages nếu phù hợp
- Tự thu thập từ video camera bãi xe

### 4.2 Tiêu chí chọn dataset

- Có bounding box cho biển số
- Ảnh đa dạng góc nhìn, ánh sáng, thời tiết
- Có nhiều kích thước biển số khác nhau
- Có bối cảnh thực tế giống camera giám sát
- Đủ lớn để fine-tune hiệu quả

### 4.3 Khuyến nghị thực tế

Cách tốt nhất cho portfolio là kết hợp:

- Dataset công khai để có dữ liệu ban đầu
- Tự thu thập thêm ảnh demo để tăng tính thực tế
- Annotate lại để thống nhất format và domain

## 5. Annotation workflow

### 5.1 Công cụ annotate

Có thể dùng:

- Roboflow Annotate
- CVAT
- LabelImg
- Label Studio

### 5.2 Quy trình

1. Thu thập ảnh raw
2. Làm sạch ảnh lỗi
3. Gán nhãn bounding box cho biển số
4. Xuất annotation về format YOLO
5. Kiểm tra nhãn bằng visualize script
6. Rà soát nhãn lỗi trước khi train

### 5.3 Quy ước nhãn

Vì bài toán chỉ detect biển số, chỉ cần một class:

- `license_plate`

Nếu sau này muốn mở rộng detect cả xe và biển số, có thể thêm class khác, nhưng giai đoạn này nên giữ đơn giản để tối ưu độ chính xác.

## 6. Chia train/validation/test

### 6.1 Tỷ lệ khuyến nghị

- Train: 70%
- Validation: 20%
- Test: 10%

### 6.2 Nguyên tắc chia

- Không để ảnh cùng một scene xuất hiện ở cả train và test nếu có thể
- Giữ phân phối góc chụp và ánh sáng tương đối đồng đều
- Test set phải là dữ liệu chưa chạm vào trong quá trình tuning

## 7. Data augmentation

### 7.1 Mục tiêu augmentation

Giúp model chịu được:

- Motion blur
- Low light
- Perspective distortion
- Scale variation
- Occlusion nhẹ
- Noise từ camera thực tế

### 7.2 Augmentation đề xuất

- Horizontal flip có kiểm soát
- Random brightness/contrast
- Gaussian blur nhẹ
- Random resize/scale
- Random crop hợp lý
- Perspective transform nhẹ
- HSV jitter

### 7.3 Lưu ý

Không nên augment quá mạnh làm biển số mất cấu trúc. Mục tiêu là tăng robustness, không phải làm dữ liệu vô nghĩa.

## 8. Training

### 8.1 Chọn YOLO

YOLOv8 hoặc YOLO11 đều phù hợp. Với portfolio, nên chọn một version và ghi rõ lý do trong README. Nếu ưu tiên hệ sinh thái và tài liệu phổ biến, YOLOv8 là lựa chọn an toàn. Nếu muốn nhấn vào model mới hơn, có thể dùng YOLO11 khi môi trường ổn định.

### 8.2 Quy trình train

1. Chuẩn bị dataset theo format YOLO
2. Tạo file YAML mô tả dataset
3. Chạy train với pretrained weights
4. Theo dõi loss, precision, recall, mAP
5. Lưu best checkpoint
6. Dùng validation để tinh chỉnh hyperparameters

### 8.3 Hyperparameters cần quan tâm

- img size
- batch size
- epochs
- learning rate
- optimizer
- augmentation strength
- patience cho early stopping

## 9. Validation và evaluation

### 9.1 Metrics cần theo dõi

- mAP@0.5
- mAP@0.5:0.95
- Precision
- Recall
- F1 Score
- Confusion Matrix

### 9.2 Ý nghĩa

- Precision cao: ít false positive
- Recall cao: ít bỏ sót biển số
- F1: cân bằng precision và recall
- mAP: metric tổng quát cho object detection
- Confusion matrix: giúp nhìn rõ lỗi theo class nếu có nhiều class

### 9.3 Cách đọc kết quả

- Precision thấp thường do model detect nhầm vùng không phải biển số
- Recall thấp thường do model bỏ sót biển số nhỏ hoặc mờ
- mAP thấp thường do dữ liệu chưa đủ đa dạng hoặc nhãn chưa sạch

## 10. Resume training và fine-tuning

### 10.1 Resume training

Dùng khi train bị dừng giữa chừng hoặc muốn tiếp tục từ checkpoint cũ.

### 10.2 Fine-tuning

Dùng khi:

- Có thêm dataset mới
- Muốn cải thiện trên camera thật
- Muốn đổi input resolution hoặc augmentation

### 10.3 Best practice

- Luôn lưu best và last checkpoint
- Không fine-tune trên test set
- Ghi rõ version của dataset và weights

## 11. Export model

### 11.1 Mục tiêu export

- Dùng model cho inference realtime
- Chuẩn bị cho webcam demo
- Tối ưu deploy sau này

### 11.2 Định dạng xuất

Tùy YOLO version, có thể xuất sang:

- ONNX
- TorchScript
- TensorRT nếu cần tối ưu mạnh

## 12. Inference và webcam demo

### 12.1 Inference image

Chạy model trên ảnh test để kiểm tra chất lượng.

### 12.2 Webcam inference

Dùng webcam hoặc video stream để mô phỏng camera bãi xe.

### 12.3 Mục tiêu demo

- Hiển thị bounding box biển số
- Crop vùng biển số
- Gửi crop sang OCR ở phase sau
- Hiển thị kết quả realtime

## 13. Best practice

- Dùng dataset versioning rõ ràng
- Không train khi annotation chưa được kiểm tra
- Tách script train, eval, infer riêng
- Ghi lại experiment để so sánh model
- Ưu tiên reproducibility: seed, config, weight version
- Lưu ảnh lỗi để cải thiện dữ liệu chứ không chỉ chỉnh model

## 14. Các lỗi thường gặp

- Nhãn không đồng nhất giữa các ảnh
- Chia dataset sai khiến test bị leakage
- Augmentation quá mạnh làm méo biển số
- Chỉ nhìn loss mà không xem metric detection
- Train tốt trên validation nhưng kém ngoài thực tế do domain gap
- Quên lưu version của weights và dataset

## 15. Cách debug

- Visualize annotation trước khi train
- Xem sample prediction trên ảnh validation
- Kiểm tra ảnh false positive và false negative
- So sánh kết quả theo từng camera hoặc điều kiện ánh sáng
- Dùng confusion theo mistake patterns nếu có nhiều class
- Nếu model học kém, kiểm tra lại dữ liệu trước khi tăng epochs

## 16. Checklist hoàn thành

- [ ] Chọn dataset nguồn
- [ ] Annotate và kiểm tra nhãn
- [ ] Chia train/val/test
- [ ] Tạo augmentation strategy
- [ ] Train YOLO baseline
- [ ] Đánh giá metrics
- [ ] Fine-tune model tốt hơn
- [ ] Export weights
- [ ] Chuẩn bị inference và webcam demo

## 17. Kết quả đầu ra của phase

Sau phase này, ta phải có một model detect biển số đủ tốt để chuyển sang Phase 6, tức là crop và OCR trong pipeline thực tế.
