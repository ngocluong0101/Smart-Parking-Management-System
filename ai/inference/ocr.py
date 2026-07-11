from typing import List, Tuple
from PIL import Image


class OCRResult:
    def __init__(self, text: str, confidence: float):
        self.text = text
        self.confidence = confidence


class PaddleOCRWrapper:
    def __init__(self, lang: str = "en"):
        try:
            from paddleocr import PaddleOCR

            self._ocr = PaddleOCR(use_angle_cls=True, lang=lang)
            self._available = True
        except Exception:  # pragma: no cover - environment dependent
            self._ocr = None
            self._available = False

    def recognize(self, image: Image.Image) -> OCRResult:
        """
        Run OCR on a PIL image and return OCRResult.

        If PaddleOCR is not installed, return a placeholder with empty text and 0 confidence.
        """
        if not self._available:
            return OCRResult(text="", confidence=0.0)

        # PaddleOCR expects numpy array
        import numpy as np

        img = np.array(image)
        result = self._ocr.ocr(img, cls=True)
        # result structure: list of [ [box], (text, conf) ]
        if not result or len(result) == 0:
            return OCRResult(text="", confidence=0.0)

        # choose the highest confidence text
        best_text = ""
        best_conf = 0.0
        for line in result:
            if len(line) >= 2 and isinstance(line[1], tuple):
                text, conf = line[1]
                try:
                    conf = float(conf)
                except Exception:
                    conf = 0.0
                if conf > best_conf:
                    best_conf = conf
                    best_text = text

        return OCRResult(text=best_text, confidence=best_conf)


# Simple factory

def get_ocr(lang: str = "en") -> PaddleOCRWrapper:
    return PaddleOCRWrapper(lang=lang)
