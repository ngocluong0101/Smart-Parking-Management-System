from ultralytics import YOLO


WEIGHTS_PATH = "weights/best.pt"


def main() -> None:
    model = YOLO(WEIGHTS_PATH)
    model.predict(source=0, show=True, conf=0.25)


if __name__ == "__main__":
    main()
