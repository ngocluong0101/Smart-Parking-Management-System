from ultralytics import YOLO


MODEL_NAME = "yolov8n.pt"
DATASET_CONFIG = "training/configs/dataset.yaml"
EPOCHS = 50
IMG_SIZE = 640
BATCH_SIZE = 16
PROJECT_NAME = "smart_parking_lp"
RUN_NAME = "baseline"


def main() -> None:
    model = YOLO(MODEL_NAME)
    model.train(
        data=DATASET_CONFIG,
        epochs=EPOCHS,
        imgsz=IMG_SIZE,
        batch=BATCH_SIZE,
        project=PROJECT_NAME,
        name=RUN_NAME,
        pretrained=True,
    )


if __name__ == "__main__":
    main()
