"""
Views controllers for qrcode app
"""


from fastapi import APIRouter, status, Depends
from fastapi.responses import StreamingResponse

from src.qrcode.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)

from src.qrcode.dependencies import get_qrcode_service
from src.qrcode.service import QrCodeService
from src.qrcode.schemas import QrCodeInfo


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_one(
    qrcode_info: QrCodeInfo,
    service: QrCodeService = Depends(get_qrcode_service),
):
    qrcode = await service.generate(qrcode_info)
    return StreamingResponse(qrcode, media_type='image/png')
    