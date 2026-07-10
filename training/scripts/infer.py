from ultralytics import YOLO


WEIGHTS_PATH = "weights/best.pt"
INPUT_SOURCE = "dataset/sample.jpg"


def main() -> None:
    model = YOLO(WEIGHTS_PATH)
    results = model.predict(source=INPUT_SOURCE, save=True, conf=0.25)
    print(results)


if __name__ == "__main__":
    main()
