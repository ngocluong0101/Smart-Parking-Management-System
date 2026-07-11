from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import base64
from io import BytesIO
from PIL import Image

from ai.utils.plate_utils import normalize_plate, is_valid_plate

router = APIRouter(prefix="/ai")


class IngestRequest(BaseModel):
    plate_raw: Optional[str] = None
    image_base64: Optional[str] = None
    source: Optional[str] = None


class IngestResponse(BaseModel):
    plate_raw: str
    plate_normalized: str
    valid: bool
    message: Optional[str] = None


@router.post("/ingest", response_model=IngestResponse)
async def ingest(payload: IngestRequest):
    """
    Endpoint for AI inference service to post OCR result and optional crop image.

    It will normalize plate and return whether it's a valid plate.
    """
    plate_raw = (payload.plate_raw or "")

    # If image provided, we could run OCR here, but in this minimal endpoint we rely on plate_raw
    if payload.image_base64:
        try:
            img_bytes = base64.b64decode(payload.image_base64)
            image = Image.open(BytesIO(img_bytes)).convert("RGB")
            # placeholder: could run OCR here if needed
        except Exception as exc:
            raise HTTPException(status_code=400, detail=f"Invalid image_base64: {exc}")

    plate_normalized = normalize_plate(plate_raw)
    valid = is_valid_plate(plate_normalized)

    message = None
    if not plate_raw:
        message = "No raw plate provided; returned empty normalization"
    elif not valid:
        message = "Plate normalized but failed basic validation"

    return IngestResponse(
        plate_raw=plate_raw,
        plate_normalized=plate_normalized,
        valid=valid,
        message=message,
    )
