from typing import List, Tuple
from PIL import Image


def crop_boxes(image: Image.Image, boxes: List[Tuple[int, int, int, int]]) -> List[Image.Image]:
    """
    Crop given PIL image by list of bounding boxes in (x1, y1, x2, y2) format.

    Returns list of cropped images.
    """
    crops = []
    for box in boxes:
        x1, y1, x2, y2 = box
        x1, y1 = max(0, int(x1)), max(0, int(y1))
        x2, y2 = max(0, int(x2)), max(0, int(y2))
        crops.append(image.crop((x1, y1, x2, y2)))
    return crops
