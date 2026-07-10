from ultralytics import YOLO


WEIGHTS_PATH = "weights/best.pt"
DATASET_CONFIG = "training/configs/dataset.yaml"


def main() -> None:
    model = YOLO(WEIGHTS_PATH)
    model.val(data=DATASET_CONFIG)


if __name__ == "__main__":
    main()
